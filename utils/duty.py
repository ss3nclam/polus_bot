import datetime
from configparser import ConfigParser

import gspread


config = ConfigParser()
config.read('config.conf')
cred = dict(config.items('GOOGLE_API'))

MONTHS = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]


def get():
    day, month, year = ((datetime.datetime.now() - datetime.timedelta(hours=7)).strftime("%d.%m.%Y")).split(".")
    sheet = gspread.service_account_from_dict(cred).open(year)

    try:
        today = list(filter(lambda x: x['Дата'] == int(day),sheet.worksheet(MONTHS[int(month) - 1]).get_all_records()))[0]
        person = ''.join(n[0] for n in filter(lambda x: 'х' in x, today.items()))
        return f'Дежурит *{person}*' if person else 'График дежурств не заполнен 🤷‍♂️'

    except gspread.exceptions.WorksheetNotFound:
        return 'График дежурств не заполнен 🤷‍♂️'
