from tinydb import TinyDB

db = TinyDB('data.json')

data = {
    'user_id': 1,
    'user_name': 'tinydb'
}

db.insert(data)