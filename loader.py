import logging
from configparser import ConfigParser
from datetime import date

from aiogram import Bot, Dispatcher

from utils.db import engine


# Read config
config = ConfigParser()
config.read('config.conf')

# Configure logging
app_verbose = logging.basicConfig(
    filename = f'logs/{date.today()}.log' if config['LOGS']['verbose_to_file'] == 'true' else None,
    encoding = 'utf-8',
    format = '%(asctime)s:%(name)s:%(levelname)s:%(message)s',
    datefmt = '%H:%M:%S',
    level = eval('logging.{}'.format(config['LOGS']['verbose_level']))
    )

# Initialize bot and dispatcher
bot = Bot(token = config['INIT']['token'])
dp = Dispatcher(bot)

# Create DB Engine
db_engine = engine.create(config)