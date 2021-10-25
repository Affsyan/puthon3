import yaml

DATA = {'vegetables': ['carrot', 'potatoes'],
        'quantity': 2,
        'grade': {
            'carrot': '\u20ac',
            'potatoes': '\u0025'
        }
        }

with open('yaml_data.yaml', 'w', encoding='utf-8') as data:
    yaml.dump(DATA, data, default_flow_style=False, allow_unicode=True)

with open('yaml_data.yaml', 'r', encoding='utf-8') as data_out:
    DATA_OUT = yaml.load(data_out, Loader=yaml.SafeLoader)

print(DATA == DATA_OUT)
