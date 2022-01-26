from setting import TG_BOT_TOCKEN_PANGEA
import telebot
import ast
from PIL import Image, ImageDraw
bot = telebot.TeleBot(TG_BOT_TOCKEN_PANGEA)
@bot.message_handler(commands=['start','help'])
def def_reply(message):
    bot.send_message(message.from_user.id,'Please, send me your location, 100% safe :)')
@bot.message_handler(content_types=['text'])
def text_reply(message):
    bot.send_message(message.from_user.id,'Send location, not text')
@bot.message_handler(content_types=['location'])
def get_loc(message):
    resp_dict=ast.literal_eval(str(message.location))
    longitude=resp_dict.get('longitude')
    latitude=resp_dict.get('latitude')
    x = int((800 / 360.0) * (180 + longitude))
    y = int((400 / 180.0) * (90 - latitude))
    r=10
    image = Image.open('def.jpg')
    draw = ImageDraw.Draw(image)
    draw.ellipse((x-r,y-r,x+r,y+r),fill=(255,0,0,0))
    bot.send_photo(message.from_user.id,image)
bot.polling(none_stop=True, interval=0)
