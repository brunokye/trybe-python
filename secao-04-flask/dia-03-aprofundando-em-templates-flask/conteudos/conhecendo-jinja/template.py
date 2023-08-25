from jinja2 import Template

# template_string = "Eu sou um {{ nome }}!"
# template = Template(template_string)

# output = template.render(nome='template')

template_file = open('index.html').read()
template = Template(template_file)

data = {
    'saudacao': 'Eu sou um template HTML',
    'informacao': 'E essa é uma das formas de se passar múltiplas '
    'informações para o template',
    'contexto': 'Isso é possível através da criação de um contexto'
}

output = template.render(data)

print(output)
