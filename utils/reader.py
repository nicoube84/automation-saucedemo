#En este archivo Programamos el lector de csv
import csv
import json

def read_users_csv():
    with open("data/users.csv",newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)
    #With garantiza que el archivo se abra y se cierre automáticamente al terminar

data = read_users_csv()


"""
[
    {
        'usuario': 'standard_user'
        'password': 'secret_sauce'
    },
    {
        'usuario': 'admin'
        'password': '1234'
    },
    {
        'usuario': 'jose'
        'password': '123'
    }
]
"""