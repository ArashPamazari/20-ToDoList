import random
import telebot

from datetime import date , time
from khayyam import JalaliDate, JalaliDatetime
from gtts import gTTS
import qrcode
import pysynth 

mybot = telebot.TeleBot('5776158257:AAHxLRHAV-nPPlreXq5FQVVyroY7ky-PC3Y')

#key
mymarkupDownload = telebot.types.ReplyKeyboardMarkup(row_width=3)
btn1 = telebot.types.KeyboardButton('headphone') # dokme paeen
btn2 = telebot.types.KeyboardButton('movie')
btn3 = telebot.types.KeyboardButton('photo')
mymarkupDownload.add(btn1,btn2,btn3)

mymarkupGame = telebot.types.ReplyKeyboardMarkup(row_width=1)
btn1 = telebot.types.KeyboardButton('new game') # dokme paeen
mymarkupGame.add(btn1)
# start
@mybot.message_handler(commands=['start'])
def send_welcome(message):
    user = message.from_user.first_name
    mybot.reply_to(message,f"{user}"' welcome to my bot , enter /help to see menu')

# download
@mybot.message_handler(commands=['download'])
def my_function_4(message):
    mybot.reply_to(message,'which one do you want to download?',reply_markup = mymarkupDownload)

# فال گیری
@mybot.message_handler(commands=['fal'])
def my_function_2(message):
    falha = ['be safar khahi raft','be didar maAshogh khahi raft','be fana khahi raft']
    selected_fal = random.choice(falha)
    mybot.reply_to(message, selected_fal)

#game
randomBotNumber = random.randint(0, 20)

@mybot.message_handler(commands=['game'])
def game(message):
    mybot.reply_to(message, 'guess between 0 - 20')
    mybot.register_next_step_handler(message, checkingBotNumber)

def checkingBotNumber(message):
    if int(message.text) == randomBotNumber:
        mybot.send_message(message.chat.id, 'You Win')
        mybot.number = random.randint(0, 20)
        mes = mybot.send_message(message.chat.id, 'For new game click ', reply_markup=mymarkupGame)
        mybot.register_next_step_handler(mes, game)

    elif int(message.text) > randomBotNumber:
        mybot.send_message(message.chat.id, ' go less ')
        mybot.register_next_step_handler(message, checkingBotNumber)

    elif int(message.text) < randomBotNumber:
        mybot.send_message(message.chat.id, 'go high ')
        mybot.register_next_step_handler(message, checkingBotNumber)

# age
@mybot.message_handler(commands=['age'])
def Birthday(message):
    listt= {}
    mybot.reply_to(message, 'Enter your date birth:(ex: 1352-04-12')
    mybot.register_next_step_handler(message, age)

def age(message):
    listt = message.text.split('-')
    print(listt)
    print(JalaliDatetime.now())
    age = JalaliDatetime.now() - JalaliDatetime(int(listt[0]), int(listt[1]), int(listt[2]))

    mybot.send_message(message.chat.id, f'{age} hours is your age')

#max
@mybot.message_handler(['max'])
def input_nums(message):
    mybot.reply_to(message, 'Enter numbers for max (ex: 5.6.2 than press Enter)')
    mybot.register_next_step_handler(message, find_max)

def find_max(message):
    mynumberes = message.text.split('.')
    list = []
    for i in mynumberes:
        list.append(int(i))
    mybot.send_message(message.chat.id, f'{max(list)} is maximume')

#argmax
@mybot.message_handler(['argmax'])
def input_nums(message):
    mybot.reply_to(message, 'Enter number for argmax (ex: 5.6.2 than press Enter)')
    mybot.register_next_step_handler(message, find_argmax)

def find_argmax(message):
    mynumberes = message.text.split('.')
    list = []
    for i in mynumberes:
        list.append(int(i))
    mybot.send_message(message.chat.id, f'{list.index(max(list))} is argmax')

#qrcode
@mybot.message_handler(['qrcode'])
def inputsen(message):
    mybot.reply_to(message, 'Enter text')
    mybot.register_next_step_handler(message, makeqrcode)

def makeqrcode(message):
    img = qrcode.make(message.text)
    img.save('qrcode.png')
    image = open('qrcode.png', 'rb')
    mybot.send_photo(message.chat.id, image)

# english voice 
@mybot.message_handler(['voice'])
def voice(message):
    mybot.reply_to(message, 'Enter a sentence in English:')
    mybot.register_next_step_handler(message, ConvertTextToVoice)

def ConvertTextToVoice(message):
    language = 'en'
    myobj = gTTS(text=message.text, lang=language, slow=False)
    myobj.save("voice.mp3")
    voice = open('voice.mp3', 'rb')
    mybot.send_voice(message.chat.id, voice)

#help
@mybot.message_handler(commands= ['help'])
def show_max(message):
    mybot.reply_to(message, "Please press the bottom :"
                            "\n/game(guessing number)" 
                            "\n/age (calculate your age)"
                            "\n/voice (reading your text)"
                            "\n/max (find the max number)"
                            "\n/argmax (find the argmax number)"
                            "\nyou can talk with bot (سلام ، خوبی، چطوری جون دل؟")

def music(message):
    mybot.reply_to(message, 'Enter a music score (e.g., "c4 c4 d4 e4"):')
    mybot.register_next_step_handler(message, make_music)

def make_music(message):
    music_score = message.text
    filename = 'music.wav'
    make_wav(music_score, fn=filename)

    audio = open(filename, 'rb')
    mybot.send_audio(message.chat.id, audio)

@mybot.message_handler(commands=['download'])
def download(message):
    mybot.reply_to(message, 'Which one do you want to download?', reply_markup=mymarkupDownload)

    btn4 = telebot.types.KeyboardButton('music')
    mymarkupDownload.add(btn4)




# مکالمه با بات
@mybot.message_handler(func=lambda message: True)
def my_function_3(message):
    if message.text == 'سلام':
        mybot.reply_to(message,'علیک سلام')

    elif message.text == 'خوبی؟':
        mybot.reply_to(message,'نه فقط تو خوبی')

    elif message.text == 'چطوری جون دل؟':
        mybot.reply_to(message,'الهی شکر ')

    elif message.text == 'chi poshidi?':
        photo = open('image.jpg','rb')
        mybot.send_photo(message.chat.id , photo)


    else:
        #mybot.reply_to(message,"نمیفهمم چی میگی")
        mybot.send_message(message.chat.id, 'نمیفهمم چی میگی')  # baraye hamon idi ke dari bahash chat mikoni befrest.    

mybot.polling() # bot ro dar halat run negah dare.

# pip list = list of library that you installed
# dastori ke ba @ shoro mishe behesh migan decorator 
