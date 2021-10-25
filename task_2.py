import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('json_data.json', 'w', encoding='utf-8') as data:
        dict_order = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }

        json.dump(dict_order, data, indent=4, ensure_ascii=False)


write_order_to_json('Монитор', 2, 1200, 'Иван', '10.10.2020')
