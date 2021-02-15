from tinydb import TinyDB

db = TinyDB('data.json')

db.truncate()

data1 = {
    'ID': 101,
    'FIRST_NAME': 'Anvar',
    'LAST_NAME': 'Komilov',
    'BIRTHDAY': '25.03.1990',
    'EMAIL': 'anvarjon@gmail.com',
    'JOB': 'teacher',
    'PHONE': '+998931234569'
}
data2 = {
    'ID': 405,
    'FIRST_NAME': 'Jamila',
    'LAST_NAME': 'Arislonova',
    'BIRTHDAY': '02.04.1965',
    'EMAIL': 'Star.gmail.com',
    'JOB': 'teacher',
    'PHONE': '+99897020032'
}
data3 = {
    'ID': 602,
    'FIRST_NAME': 'Javlon',
    'LAST_NAME': 'Shukurov',
    'BIRTHDAY': '1.10.2000',
    'EMAIL': 'javlonbek@gmail.com',
    'JOB': 'developer',
    'PHONE': '+998996566666'
}
data4 = {
    'ID': 302,
    'FIRST_NAME': 'Alisher',
    'LAST_NAME': 'Nizomov',
    'BIRTHDAY': '05.12.2001',
    'EMAIL': 'alisher@gailm.com',
    'JOB': 'writer',
    'PHONE': '+998995412356'
}
data5 = {
    'ID': 874,
    'FIRST_NAME': 'Djon',
    'LAST_NAME': 'Snow',
    'BIRTHDAY': '01.04.1989',
    'EMAIL': 'snow@gmail.com',
    'JOB': 'actor',
    'PHONE': '+998974587485'
}
data6 = {
    'ID': 600,
    'FIRST_NAME': 'Anna',
    'LAST_NAME': 'Neklyudova',
    'BIRTHDAY': '05.01.1993',
    'EMAIL': 'anna@gmail.',
    'JOB': 'driver',
    'PHONE': '+99894000000'
}
data7 = {
    'ID': 840,
    'FIRST_NAME': 'Svetlana',
    'LAST_NAME': 'Berdichuk',
    'BIRTHDAY': '24.06.2005',
    'EMAIL': 'apple@gamil.com',
    'JOB': 'cooker',
    'PHONE': '+998974152386'
}
data8 = {
    'ID': 654,
    'FIRST_NAME': 'Alex',
    'LAST_NAME': 'Smit',
    'BIRTHDAY': '14.09.1997',
    'EMAIL': 'alex@gmail.com',
    'JOB': 'teacher',
    'PHONE': '+998948789520'
}
data9 = {
    'ID': 103,
    'FIRST_NAME': 'Oleg',
    'LAST_NAME': 'Petrov',
    'BIRTHDAY': '15.11.2006',
    'EMAIL': 'oleg@gmail.com',
    'JOB': 'cooker',
    'PHONE': '+998934569820'
}
data10 = {
    'ID': 204,
    'FIRST_NAME': 'Jasur',
    'LAST_NAME': 'Xondamirov',
    'BIRTHDAY': '02.02.1999',
    'EMAIL': 'jasur@gamil.com',
    'JOB': 'teacher',
    'PHONE': '+998974852356'
}

db.insert_multiple([data1, data2, data3, data4, data5, data6, data7, data8, data9, data10])