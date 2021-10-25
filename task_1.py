import csv
import re

from chardet import detect


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    heading = ('Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы')

    for i in range(1, 4):
        with open(f'info_{i}.txt', 'rb') as file:
            content_file = file.read()
            encoding_file = detect(content_file)['encoding']
            data = content_file.decode(encoding_file)
            os_prod_list.append(re.compile(r'Изготовитель системы: \s* \S*').findall(data)[0].split()[2])
            os_name_list.append(re.compile(r'Windows\s* \S*').findall(data)[0])
            os_code_list.append(re.compile(r'Код продукта:\s* \S*').findall(data)[0].split()[2])
            os_type_list.append(re.compile(r'Тип системы:\s* \S*').findall(data)[0].split()[2])

    main_data = list(zip(os_prod_list, os_name_list, os_code_list, os_type_list))
    main_data.insert(0, heading)
    return main_data


def write_to_csv(csv_file_name):
    main_data = get_data()
    with open(csv_file_name, 'w', encoding='windows-1251') as file:
        writer = csv.writer(file)
        for el in main_data:
            writer.writerow(el)


write_to_csv('data_info.csv')


