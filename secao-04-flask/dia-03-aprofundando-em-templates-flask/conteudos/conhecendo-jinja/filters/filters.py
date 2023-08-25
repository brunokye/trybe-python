from jinja2 import Environment, FileSystemLoader
from custom_filters import convert_date, replace_text

loader = FileSystemLoader('filters')
environment = Environment(loader=loader)

environment.filters['convert_date'] = convert_date
environment.filters['replace_text'] = replace_text
template = environment.get_template('filters.html')

data = {
    'name': 'a primeira letra vai ficar maiúscula',
    'to_upper': 'todas as letras vão ficar maiúsculas',
    'to_lower': 'TODAS AS LETRAS VÃO FICAR MINÚSCULAS',
    'my_list': [0, 1, 2, 3, 4, 5],
    'text': 'Esse texto irá ser truncado',
    'date': '2023-05-21'
}

output = template.render(data)

print(output)
