login = 'user.name'
senha = 'Senha123#'

insira_login = input('Insira o Login: ')
insira_senha = input('Insira a senha: ')

if insira_login == login and insira_senha == senha:
    print('Acesso concedido.')

else:
    print('Acesso negado.')