from tinydb import TinyDB

databese = TinyDB('database.json')

databese.truncate()

data = dict()

for i in range(10):
    data = {}
    data['user_id'] = int(input('user_id: '))
    data['username'] = input('username: ')
    data['first_name'] = input('first_name: ')
    data['last_ame'] = input('last_name: ')
    data['birthday'] = input('birthday: ')
    data['email'] = input('email: ')
    data['job'] = input('job: ')
    data['phone'] = input('phono: ')

    databese.insert(data)