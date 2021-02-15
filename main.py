from tinydb import TinyDB

db = TinyDB('data.json')

db.truncate()

data1 = {
    'user_id': 101,
    'first_name': 'Anvar',
    'last_name': 'Komilov',
    'birthday': '25.03.1990',
    'email': 'anvarjon@gmail.com',
    'job': 'teacher',
    'phone': '+998931234569'
}
data2 = {
    'user_id': 405,
    'first_name': 'Jamila',
    'last_name': 'Arislonova',
    'birthday': '02.04.1965',
    'email': 'Star.gmail.com',
    'job': 'teacher',
    'phone': '+99897020032'
}
data3 = {
    'user_id': 602,
    'first_name': 'Javlon',
    'last_name': 'Shukurov',
    'birthday': '1.10.2000',
    'email': 'javlonbek@gmail.com',
    'job': 'developer',
    'phone': '+998996566666'
}
data4 = {
    'user_id': 302,
    'first_name': 'Alisher',
    'last_name': 'Nizomov',
    'birthday': '05.12.2001',
    'email': 'alisher@gailm.com',
    'job': 'writer',
    'phone': '+998995412356'
}
data5 = {
    'user_id': 874,
    'first_name': 'Djon',
    'last_name': 'Snow',
    'birthday': '01.04.1989',
    'email': 'snow@gmail.com',
    'job': 'actor',
    'phone': '+998974587485'
}
data6 = {
    'user_id': 600,
    'first_name': 'Anna',
    'last_name': 'Neklyudova',
    'birthday': '05.01.1993',
    'email': 'anna@gmail.',
    'job': 'driver',
    'phone': '+99894000000'
}
data7 = {
    'user_id': 840,
    'first_name': 'Svetlana',
    'last_name': 'Berdichuk',
    'birthday': '24.06.2005',
    'email': 'apple@gamil.com',
    'job': 'cooker',
    'phone': '+998974152386'
}
data8 = {
    'user_id': 654,
    'first_name': 'Alex',
    'last_name': 'Smit',
    'birthday': '14.09.1997',
    'email': 'alex@gmail.com',
    'job': 'teacher',
    'phone': '+998948789520'
}
data9 = {
    'user_id': 103,
    'first_name': 'Oleg',
    'last_name': 'Petrov',
    'birthday': '15.11.2006',
    'email': 'oleg@gmail.com',
    'job': 'cooker',
    'phone': '+998934569820'
}
data10 = {
    'user_id': 204,
    'first_name': 'Jasur',
    'last_name': 'Xondamirov',
    'birthday': '02.02.1999',
    'email': 'jasur@gamil.com',
    'job': 'teacher',
    'phone': '+998974852356'
}

db.insert_multiple([data1, data2, data3, data4, data5, data6, data7, data8, data9, data10])