from configparser import ConfigParser

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from loader import bot
from utils import summary


# Read config and initialize scheduler
scheduler = AsyncIOScheduler()
config = ConfigParser()
config.read('config.conf')

# Read all of time from config
config_dict = dict(config.items('DAILY_SUMMARY'))
time_tuple = tuple(config_dict[i] for i in config_dict if 'time' in i)


# Create func for daily summary
async def send_summary():
    chat_id = config['DAILY_SUMMARY']['group_id']
    await bot.send_chat_action(chat_id, action='typing')
    await bot.send_message(chat_id, text=summary.get(), parse_mode='Markdown')


def start():
    if config.getboolean('DAILY_SUMMARY', 'status') and time_tuple:
        for time in time_tuple:
            hour, minute = map(int, time.split(':'))
            scheduler.add_job(send_summary, 'cron', hour=hour, minute=minute)
        scheduler.start()
