from datetime import datetime

from utils.duty import get as duty
from utils.weather import get as weather


def get():
    return '\n'.join([str(datetime.now()), weather(), duty()])