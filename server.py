import os
import socket
from typing import NoReturn
import telebot
from wakeonlan import send_magic_packet
from dotenv import load_dotenv
from telebot import types

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
MAC_ADDRESS = os.getenv("MAC_ADDRESS")
BROADCAST_IP = os.getenv("BROADCAST_IP")
CLIENT_IP = os.getenv("CLIENT_IP")

bot = telebot.TeleBot(TOKEN)

def send_command_to_client(command: str) -> str:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((CLIENT_IP, 50000))
            s.sendall(command.encode())
            data = s.recv(1024)
            return data.decode()
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return "Error"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который может включать и выключать ваш компьютер.")
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Включить", callback_data="turn_on"),
               types.InlineKeyboardButton("Выключить", callback_data="turn_off"),
               types.InlineKeyboardButton("Проверить статус", callback_data="status"))
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "turn_on":
        send_magic_packet(MAC_ADDRESS, ip_address=BROADCAST_IP)
        bot.answer_callback_query(call.id, "Включаю компьютер...")
    elif call.data == "turn_off":
        response = send_command_to_client('status')
        if response == "I'm alive!":
            send_command_to_client('turn_off')
            bot.answer_callback_query(call.id, "Выключаю компьютер... ❌")
        else:
            bot.answer_callback_query(call.id, "Ошибка: Компьютер уже выключен. ✅")
    elif call.data == "status":
        response = send_command_to_client('status')
        if response == "I'm alive!":
            bot.answer_callback_query(call.id, "Компьютер включен ✅", show_alert=True)
        else:
            bot.answer_callback_query(call.id, "Ошибка: Компьютер выключен. ❌", show_alert=True)

bot.infinity_polling()
