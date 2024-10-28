import json
data = {'reg_data': []}
question1 = input('Вход или регистрация: ')
login = input('Введите логин: ')
passwrd = input('Введите пароль: ')


def login_function(login, passwrd):
      with open('log.json') as f:
          data = json.load(f)

      if login in data.keys():
         if data[login] == passwrd:
           print('Успешный вход')
         else:
             print('Неверный пароль')
      else:
        print('Пользователя с таким логином не существует')


def registr(login, passwrd):
      if login in data.keys():
         print('Логин занят')
      else:
         data[login] = passwrd
         print('Регистрация успешна')

      data['reg_data'].append({'login': 'passwrd'})
      with open('log.json', 'a') as f:
          json.dump(data, f)


if question1 == 'вход':
    login_function(login, passwrd)
elif question1 == 'регистрация':
    registr(login, passwrd)
else:
    print(' ')




