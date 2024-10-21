import requests
import telebot
import sys
from telebot import types
from bs4 import BeautifulSoup
from functions import nbu, mizhbank, auction

sys.stdout.reconfigure(encoding='utf-8')

bot = telebot.TeleBot('6458256921:AAGAxdKyOpRxYdhNCoh4KevMRMw9CrEpQ3U')

@bot.message_handler(commands=['start'])
def handle_start(message):
    # Создаем inline-клавиатуру
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)

    button1 = types.KeyboardButton("НБУ")
    button2 = types.KeyboardButton("Міжбанк")
    button3 = types.KeyboardButton("Аукціон")

    # Добавляем кнопки к клавиатуре
    keyboard.add(button1, button2, button3)

    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'НБУ')
def handle_nbu(message):
    # Обработка нажатия кнопки "НБУ"
    url_nbu = 'https://minfin.com.ua/ua/currency/nbu/usd/'
    response_nbu_usd = requests.get(url_nbu)

    url_nbu = 'https://minfin.com.ua/ua/currency/nbu/eur/'
    response_nbu_eur = requests.get(url_nbu)

    nbu_usd_rate = "{:.3f}".format(nbu(response_nbu_usd))
    nbu_eur_rate = "{:.3f}".format(nbu(response_nbu_eur))
    
    # Преобразуйте значения в строки перед отправкой
    bot.send_message(message.chat.id, f"Курс НБУ\nUSD: {nbu_usd_rate} | EUR: {nbu_eur_rate}")

@bot.message_handler(func=lambda message: message.text == 'Міжбанк')
def handle_mizhbank(message):

    # Обработка нажатия кнопки "Міжбанк"
    url_mizhbank = 'https://minfin.com.ua/ua/currency/mb/'
    response_mizhbank = requests.get(url_mizhbank)

    mizhbank_USD_BUY_rate = "{:.2f}".format(mizhbank(response_mizhbank, 0))
    mizhbank_USD_SALE_rate = "{:.2f}".format(mizhbank(response_mizhbank, 1))
    mizhbank_EUR_BUY_rate = "{:.2f}".format(mizhbank(response_mizhbank, 2))
    mizhbank_EUR_SALE_rate = "{:.2f}".format(mizhbank(response_mizhbank, 3))

    bot.send_message(message.chat.id, f"Курс Міжбанк\nUSD Купівля: {mizhbank_USD_BUY_rate} | Продаж: {mizhbank_USD_SALE_rate}\nEUR Купівля: {mizhbank_EUR_BUY_rate} | Продаж: {mizhbank_EUR_SALE_rate}")

@bot.message_handler(func=lambda message: message.text == 'Аукціон')
def handle_auction(message):

    sum_USD_buy = 0
    sum_USD_sale = 0
    sum_EUR_buy = 0
    sum_EUR_sale = 0

    count_USD_buy = 0
    count_USD_sale = 0
    count_EUR_buy = 0
    count_EUR_sale = 0

    count = 0
    # Обработка нажатия кнопки "Аукціон"
    url_auction = 'https://minfin.com.ua/ua/currency/auction/usd/buy/kiev/'
    response_auction = requests.get(url_auction)

    auction_KIEV_USD_BUY_rate = (auction(response_auction, 0))
    if auction_KIEV_USD_BUY_rate != 0:
        sum_USD_buy += auction_KIEV_USD_BUY_rate
        count_USD_buy = count_USD_buy + 1
    auction_KIEV_USD_SALE_rate = (auction(response_auction, 1))
    if auction_KIEV_USD_SALE_rate != 0: 
        sum_USD_sale += auction_KIEV_USD_SALE_rate
        count_USD_sale = count_USD_sale + 1

    url_auction = 'https://minfin.com.ua/ua/currency/auction/eur/buy/kiev/'
    response_auction = requests.get(url_auction)

    auction_KIEV_EUR_BUY_rate =(auction(response_auction, 0))
    if auction_KIEV_EUR_BUY_rate != 0: 
        sum_EUR_buy += auction_KIEV_EUR_BUY_rate
        count_EUR_buy = count_EUR_buy + 1
    auction_KIEV_EUR_SALE_rate = (auction(response_auction, 1))
    if auction_KIEV_EUR_SALE_rate != 0: 
        sum_EUR_sale += auction_KIEV_EUR_SALE_rate
        count_EUR_sale = count_EUR_sale + 1

    url_auction = 'https://minfin.com.ua/currency/auction/usd/buy/odessa/'
    response_auction = requests.get(url_auction)

    auction_ODESSA_USD_BUY_rate = (auction(response_auction, 0))
    if auction_ODESSA_USD_BUY_rate != 0:
        sum_USD_buy += auction_ODESSA_USD_BUY_rate
        count_USD_buy = count_USD_buy + 1
    auction_ODESSA_USD_SALE_rate = (auction(response_auction, 1))
    if auction_ODESSA_USD_SALE_rate != 0: 
        sum_USD_sale += auction_ODESSA_USD_SALE_rate
        count_USD_sale = count_USD_sale + 1

    url_auction = 'https://minfin.com.ua/currency/auction/eur/buy/odessa/'
    response_auction = requests.get(url_auction)

    auction_ODESSA_EUR_BUY_rate = (auction(response_auction, 0))
    if auction_ODESSA_EUR_BUY_rate != 0: 
        sum_EUR_buy += auction_ODESSA_EUR_BUY_rate
        count_EUR_buy = count_EUR_buy + 1
    auction_ODESSA_EUR_SALE_rate = (auction(response_auction, 1))
    if auction_ODESSA_EUR_SALE_rate != 0: 
        sum_EUR_sale += auction_ODESSA_EUR_SALE_rate
        count_EUR_sale = count_EUR_sale + 1

    url_auction = 'https://minfin.com.ua/currency/auction/usd/buy/lvov/'
    response_auction = requests.get(url_auction)

    auction_LVOV_USD_BUY_rate = (auction(response_auction, 0))
    if auction_LVOV_USD_BUY_rate != 0: 
        sum_USD_buy += auction_LVOV_USD_BUY_rate
        count_USD_buy = count_USD_buy + 1
    auction_LVOV_USD_SALE_rate = (auction(response_auction, 1))
    if auction_LVOV_USD_SALE_rate != 0: 
        sum_USD_sale += auction_LVOV_USD_SALE_rate
        count_USD_sale = count_USD_sale + 1

    url_auction = 'https://minfin.com.ua/currency/auction/eur/buy/lvov/'
    response_auction = requests.get(url_auction)

    auction_LVOV_EUR_BUY_rate = (auction(response_auction, 0))
    if auction_LVOV_EUR_BUY_rate != 0: 
        sum_EUR_buy += auction_LVOV_EUR_BUY_rate
        count_EUR_buy = count_EUR_buy + 1
    auction_LVOV_EUR_SALE_rate = (auction(response_auction, 1))
    if auction_LVOV_EUR_SALE_rate != 0: 
        sum_EUR_sale += auction_LVOV_EUR_SALE_rate
        count_EUR_sale = count_EUR_sale + 1

    url_auction = 'https://minfin.com.ua/currency/auction/usd/buy/kharkov/'
    response_auction = requests.get(url_auction)

    auction_KHARKOV_USD_BUY_rate = (auction(response_auction, 0))
    if auction_KHARKOV_USD_BUY_rate != 0:
        sum_USD_buy += auction_KHARKOV_USD_BUY_rate
        count_USD_buy = count_USD_buy + 1
    auction_KHARKOV_USD_SALE_rate = (auction(response_auction, 1))
    if auction_KHARKOV_USD_SALE_rate != 0: 
        sum_USD_sale += auction_KHARKOV_USD_SALE_rate
        count_USD_sale = count_USD_sale + 1

    url_auction = 'https://minfin.com.ua/currency/auction/eur/buy/kharkov/'
    response_auction = requests.get(url_auction)

    auction_KHARKOV_EUR_BUY_rate = (auction(response_auction, 0))
    if auction_KHARKOV_EUR_BUY_rate != 0: 
        sum_EUR_buy += auction_KHARKOV_EUR_BUY_rate
        count_EUR_buy = count_EUR_buy + 1
    auction_KHARKOV_EUR_SALE_rate = (auction(response_auction, 1))
    if auction_KHARKOV_EUR_SALE_rate != 0: 
        sum_EUR_sale += auction_KHARKOV_EUR_SALE_rate
        count_EUR_sale = count_EUR_sale + 1

    url_auction = 'https://minfin.com.ua/currency/auction/usd/buy/zaporozhye/'
    response_auction = requests.get(url_auction)

    auction_ZAPOROZHYE_USD_BUY_rate = (auction(response_auction, 0))
    if auction_ZAPOROZHYE_USD_BUY_rate != 0: 
        sum_USD_buy += auction_ZAPOROZHYE_USD_BUY_rate
        count_USD_buy = count_USD_buy + 1
    auction_ZAPOROZHYE_USD_SALE_rate = (auction(response_auction, 1))
    if auction_ZAPOROZHYE_USD_SALE_rate != 0:
        sum_USD_sale += auction_ZAPOROZHYE_USD_SALE_rate
        count_USD_sale = count_USD_sale + 1

    url_auction = 'https://minfin.com.ua/currency/auction/eur/buy/zaporozhye/'
    response_auction = requests.get(url_auction)

    auction_ZAPOROZHYE_EUR_BUY_rate = (auction(response_auction, 0))
    if auction_ZAPOROZHYE_EUR_BUY_rate != 0: 
        sum_EUR_buy += auction_ZAPOROZHYE_EUR_BUY_rate
        count_EUR_buy = count_EUR_buy + 1
    auction_ZAPOROZHYE_EUR_SALE_rate = (auction(response_auction, 1))
    if auction_ZAPOROZHYE_EUR_SALE_rate != 0: 
        sum_EUR_sale += auction_ZAPOROZHYE_EUR_SALE_rate
        count_EUR_sale = count_EUR_sale + 1

    url_auction = 'https://minfin.com.ua/currency/auction/usd/buy/chernigov/'
    response_auction = requests.get(url_auction)

    auction_CHERNIGOV_USD_BUY_rate = (auction(response_auction, 0))
    if auction_CHERNIGOV_USD_BUY_rate != 0: 
        sum_USD_buy += auction_CHERNIGOV_USD_BUY_rate
        count_USD_buy = count_USD_buy + 1
    auction_CHERNIGOV_USD_SALE_rate = (auction(response_auction, 1))
    if auction_CHERNIGOV_USD_SALE_rate != 0:
        sum_USD_sale += auction_CHERNIGOV_USD_SALE_rate
        count_USD_sale = count_USD_sale + 1

    url_auction = 'https://minfin.com.ua/currency/auction/eur/buy/chernigov/'
    response_auction = requests.get(url_auction)

    auction_CHERNIGOV_EUR_BUY_rate = (auction(response_auction, 0))
    if auction_CHERNIGOV_EUR_BUY_rate != 0: 
        sum_EUR_buy += auction_CHERNIGOV_EUR_BUY_rate
        count_EUR_buy = count_EUR_buy + 1
    auction_CHERNIGOV_EUR_SALE_rate = (auction(response_auction, 1))
    if auction_CHERNIGOV_EUR_SALE_rate != 0: 
        sum_EUR_sale += auction_CHERNIGOV_EUR_SALE_rate
        count_EUR_sale = count_EUR_sale + 1

    url_auction = 'https://minfin.com.ua/currency/auction/usd/buy/rovno/'
    response_auction = requests.get(url_auction)

    auction_ROVNO_USD_BUY_rate = (auction(response_auction, 0))
    if auction_ROVNO_USD_BUY_rate != 0: 
        sum_USD_buy += auction_ROVNO_USD_BUY_rate
        count_USD_buy = count_USD_buy + 1
    auction_ROVNO_USD_SALE_rate = (auction(response_auction, 1))
    if auction_ROVNO_USD_SALE_rate != 0:
        sum_USD_sale += auction_ROVNO_USD_SALE_rate
        count_USD_sale = count_USD_sale + 1

    url_auction = 'https://minfin.com.ua/currency/auction/eur/buy/rovno/'
    response_auction = requests.get(url_auction)

    auction_ROVNO_EUR_BUY_rate = (auction(response_auction, 0))
    if auction_ROVNO_EUR_BUY_rate != 0: 
        sum_EUR_buy += auction_ROVNO_EUR_BUY_rate
        count_EUR_buy = count_EUR_buy + 1
    auction_ROVNO_EUR_SALE_rate = (auction(response_auction, 1))
    if auction_ROVNO_EUR_SALE_rate != 0: 
        sum_EUR_sale += auction_ROVNO_EUR_SALE_rate
        count_EUR_sale = count_EUR_sale + 1

    url_auction = 'https://minfin.com.ua/currency/auction/usd/buy/vinnitsa/'
    response_auction = requests.get(url_auction)

    auction_VINNITSA_USD_BUY_rate = (auction(response_auction, 0))
    if auction_VINNITSA_USD_BUY_rate != 0: 
        sum_USD_buy += auction_VINNITSA_USD_BUY_rate
        count_USD_buy = count_USD_buy + 1
    auction_VINNITSA_USD_SALE_rate = (auction(response_auction, 1))
    if auction_VINNITSA_USD_SALE_rate != 0:
        sum_USD_sale += auction_VINNITSA_USD_SALE_rate
        count_USD_sale = count_USD_sale + 1

    url_auction = 'https://minfin.com.ua/currency/auction/eur/buy/vinnitsa/'
    response_auction = requests.get(url_auction)

    auction_VINNITSA_EUR_BUY_rate = (auction(response_auction, 0))
    if auction_VINNITSA_EUR_BUY_rate != 0: 
        sum_EUR_buy += auction_VINNITSA_EUR_BUY_rate
        count_EUR_buy = count_EUR_buy + 1
    auction_VINNITSA_EUR_SALE_rate = (auction(response_auction, 1))
    if auction_VINNITSA_EUR_SALE_rate != 0: 
        sum_EUR_sale += auction_VINNITSA_EUR_SALE_rate
        count_EUR_sale = count_EUR_sale + 1

    url_auction = 'https://minfin.com.ua/currency/auction/usd/buy/dnepropetrovsk/'
    response_auction = requests.get(url_auction)

    auction_DNEPROPETROVSK_USD_BUY_rate = (auction(response_auction, 0))
    if auction_DNEPROPETROVSK_USD_BUY_rate != 0: 
        sum_USD_buy += auction_DNEPROPETROVSK_USD_BUY_rate
        count_USD_buy = count_USD_buy + 1
    auction_DNEPROPETROVSK_USD_SALE_rate = (auction(response_auction, 1))
    if auction_DNEPROPETROVSK_USD_SALE_rate != 0: 
        sum_USD_sale += auction_DNEPROPETROVSK_USD_SALE_rate
        count_USD_sale = count_USD_sale + 1

    url_auction = 'https://minfin.com.ua/currency/auction/eur/buy/dnepropetrovsk/'
    response_auction = requests.get(url_auction)

    auction_DNEPROPETROVSK_EUR_BUY_rate = (auction(response_auction, 0))
    if auction_DNEPROPETROVSK_EUR_BUY_rate != 0:
        sum_EUR_buy += auction_DNEPROPETROVSK_EUR_BUY_rate
        count_EUR_buy = count_EUR_buy + 1
    auction_DNEPROPETROVSK_EUR_SALE_rate = (auction(response_auction, 1))
    if auction_DNEPROPETROVSK_EUR_SALE_rate != 0:
        sum_EUR_sale += auction_DNEPROPETROVSK_EUR_SALE_rate
        count_EUR_sale = count_EUR_sale + 1

    middle_value_USD_buy = "{:.2f}".format(sum_USD_buy / count_USD_buy)

    middle_value_USD_sale = "{:.2f}".format(sum_USD_sale / count_USD_sale)

    middle_value_EUR_buy = "{:.2f}".format(sum_EUR_buy / count_EUR_buy)

    middle_value_EUR_sale = "{:.2f}".format(sum_EUR_sale / count_EUR_sale)
    
    message_text = (
    "Аукціон\n<b><i>Київ</i></b>\n"
        f"USD Купівля: <b>{auction_KIEV_USD_BUY_rate}</b> | Продаж: <b>{auction_KIEV_USD_SALE_rate}</b>\n"
        f"EUR Купівля: <b>{auction_KIEV_EUR_BUY_rate}</b> | Продаж: <b>{auction_KIEV_EUR_SALE_rate}</b>\n"
        "<b><i>Одеса</i></b>\n"
        f"USD Купівля: <b>{auction_ODESSA_USD_BUY_rate}</b> | Продаж: <b>{auction_ODESSA_USD_SALE_rate}</b>\n"
        f"EUR Купівля: <b>{auction_ODESSA_EUR_BUY_rate}</b> | Продаж: <b>{auction_ODESSA_EUR_SALE_rate}</b>\n"
        "<b><i>Львів</i></b>\n"
        f"USD Купівля: <b>{auction_LVOV_USD_BUY_rate}</b> | Продаж: <b>{auction_LVOV_USD_SALE_rate}</b>\n"
        f"EUR Купівля: <b>{auction_LVOV_EUR_BUY_rate}</b> | Продаж: <b>{auction_LVOV_EUR_SALE_rate}</b>\n"
        "<b><i>Харків</i></b>\n"
        f"USD Купівля: <b>{auction_KHARKOV_USD_BUY_rate}</b> | Продаж: <b>{auction_KHARKOV_USD_SALE_rate}</b>\n"
        f"EUR Купівля: <b>{auction_KHARKOV_EUR_BUY_rate}</b> | Продаж: <b>{auction_KHARKOV_EUR_SALE_rate}</b>\n"
        "<b><i>Запоріжжя</i></b>\n"
        f"USD Купівля: <b>{auction_ZAPOROZHYE_USD_BUY_rate}</b> | Продаж: <b>{auction_ZAPOROZHYE_USD_SALE_rate}</b>\n"
        f"EUR Купівля: <b>{auction_ZAPOROZHYE_EUR_BUY_rate}</b> | Продаж: <b>{auction_ZAPOROZHYE_EUR_SALE_rate}</b>\n"
        "<b><i>Чернігів</i></b>\n"
        f"USD Купівля: <b>{auction_CHERNIGOV_USD_BUY_rate}</b> | Продаж: <b>{auction_CHERNIGOV_USD_SALE_rate}</b>\n"
        f"EUR Купівля: <b>{auction_CHERNIGOV_EUR_BUY_rate}</b> | Продаж: <b>{auction_CHERNIGOV_EUR_SALE_rate}</b>\n"
        "<b><i>Рівне</i></b>\n"
        f"USD Купівля: <b>{auction_ROVNO_USD_BUY_rate}</b> | Продаж: <b>{auction_ROVNO_USD_SALE_rate}</b>\n"
        f"EUR Купівля: <b>{auction_ROVNO_EUR_BUY_rate}</b> | Продаж: <b>{auction_ROVNO_EUR_SALE_rate}</b>\n"
        "<b><i>Вінниця</i></b>\n"
        f"USD Купівля: <b>{auction_VINNITSA_USD_BUY_rate}</b> | Продаж: <b>{auction_VINNITSA_USD_SALE_rate}</b>\n"
        f"EUR Купівля: <b>{auction_VINNITSA_EUR_BUY_rate}</b> | Продаж: <b>{auction_VINNITSA_EUR_SALE_rate}</b>\n"
        "<b><i>Дніпро</i></b>\n"
        f"USD Купівля: <b>{auction_DNEPROPETROVSK_USD_BUY_rate}</b> | Продаж: <b>{auction_DNEPROPETROVSK_USD_SALE_rate}</b>\n"
        f"EUR Купівля: <b>{auction_DNEPROPETROVSK_EUR_BUY_rate}</b> | Продаж: <b>{auction_DNEPROPETROVSK_EUR_SALE_rate}</b>\n"
        "<b><i>Середнє значення</i></b>\n"
        f"USD Купівля: <b>{middle_value_USD_buy}</b> | Продаж: <b>{middle_value_USD_sale}</b>\n"
        f"EUR Купівля: <b>{middle_value_EUR_buy}</b> | Продаж: <b>{middle_value_EUR_sale}</b>\n"
        
    )

    bot.send_message(message.chat.id, message_text, parse_mode='HTML')

bot.infinity_polling()