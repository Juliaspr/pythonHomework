import json
data = {'reg_data': []}
login = input('Введите логин:')
passwrd = input('Введите пароль:')

with open('log.json', 'a') as f:
    json.dump(login, f)


def registr(login, passwrd):
    if login in data.keys():
        print('Логин занят')
    else:
        data[login] = passwrd
        print('Регистрация успешна')

    data['reg_data'].append({'login': 'passwrd'})
    with open('log.json', 'a') as f:
        json.dump(data, f)


