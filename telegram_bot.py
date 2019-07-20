import pyowm
import telebot

owm = pyowm.OWM('a947fe8f44a15afdfa2bd994c0e1b2ec', language = "ru")

bot = telebot.TeleBot("882040436:AAEGJ2K8mfyNxJiJMMPOBE4yqZMvUFr9pGM")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()

	answer = "В городе " + message.text + " сейчас " + str(w.get_detailed_status()) + "\n"
	answer += "Температура сейчас в районе от " + str(w.get_temperature('celsius')["temp_min"]) + "°C  до " + str(w.get_temperature('celsius')["temp_max"]) + "°C\n"
	answer += "Средняя температура: " + str(w.get_temperature('celsius')["temp"]) + "°C\n"
	answer += "Скорость ветра: " + str(w.get_wind()["speed"]) + " м/с\n"
	answer += "Влажность: " + str(w.get_humidity()) + "%"

	bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)
