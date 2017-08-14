import os, backend.Bot as Bot

#the absolute path to this file... used in the various loader modules
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

bot = Bot.Bot(ROOT_PATH)
bot.cycle()
