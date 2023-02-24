#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import telebot
import untangle

def get_case(value):
    cases = {
        'ec':'Encoberto com Chuvas Isoladas 🌧',
        'ci':'Chuvas Isoladas 🌧',
        'c':'Chuva 🌧',
        'in':'Instavel ⛈',
        'pp':'Possibilidade de Pancadas de Chuva 🌧',
        'cm':'Chuva pela Manha ☔️',
        'cn':'Chuva a Noite 🌧',
        'pt':'Pancadas de Chuva a Tarde ☔️',
        'pm':'Pancadas de Chuva pela Manha 🌧',
        'np':'Nublado e Pancadas de Chuva ☔️',
        'pc':'Pancadas de Chuva ☔️',
        'pn':'Parcialmente Nublado ☁️',
        'cv':'Chuvisco 🌧',
        'ch':'Chuvoso ☔️',
        't':'Tempestade ⛈',
        'ps':'Predominio de Sol ☀️',
        'e':'Encoberto ⛅️',
        'n':'Nublado ☁️',
        'cl':'Ceu Claro 😎',
        'nv':'Nevoeiro 🌫',
        'g':'Geada ❄️',
        'ne':'Neve ❄️',
        'nd':'Nao Definido',
        'pnt':'Pancadas de Chuva a Noite 🌧',
        'psc':'Possibilidade de Chuva 🌧',
        'pcm':'Possibilidade de Chuva pela Manha ☔️',
        'pct':'Possibilidade de Chuva a Tarde ☔️',
        'pcn':'Possibilidade de Chuva a Noite 🌧',
        'npt':'Nublado com Pancadas a Tarde ☔️',
        'npn':'Nublado com Pancadas a Noite ☔️',
        'ncn':'Nublado com Possibilidade de Chuva a Noite ☁️',
        'nct':'Nublado com Possibilidade de Chuva a Tarde ☁️',
        'ncm':'Nublado com Possibilidade de Chuva pela Manha 🌦',
        'npm':'Nublado com Pancadas de Chuva pela Manha 🌦',
        'npp':'Nublado com Possibilidade de Chuva ☁️',
        'vn':'Variacao de Nebulosidade ☁️',
        'ct':'Chuva a Tarde 🌧',
        'ppn':'Possibilidade de Pancadas de Chuva a Noite 🌧',
        'ppt':'Possibilidade de Pancadas de Chuva a Tarde 🌧',
        'ppm':'Possibilidade de Pancadas de Chuva pela Manha 🌦'
    }
    return cases.get(value)

def create_weather_message(city):
    feed = untangle.parse(f'http://servicos.cptec.inpe.br/XML/cidade/{city}/previsao.xml')
    cidade = feed.cidade.nome.cdata
    uf = feed.cidade.uf.cdata
    complete_message = f'🌤 <b>Previsão do tempo\n{cidade} {uf}</b>\n'
    for index in range(0,4):
        dia = feed.cidade.previsao[index].dia.cdata
        tempo = feed.cidade.previsao[index].tempo.cdata
        maxima = feed.cidade.previsao[index].maxima.cdata
        minima  = feed.cidade.previsao[index].minima.cdata
        iuv = feed.cidade.previsao[index].iuv.cdata
        dia = dia.split("-")
        date = (f'<b>Dia: {dia[2]}/{dia[1]}/{dia[0]}</b>')
        message = f'Máxima: {maxima}ºC\nMínima: {minima}ºC\n<i>{get_case(tempo)}</i>'
        complete_message = f'{complete_message}\n{date}\n{message}\n'
    return complete_message

if __name__ == "__main__":
    TOKEN = os.environ.get('BOT_TOKEN')
    CITY = os.environ.get('CITY')
    DEST = os.environ.get('DEST')
    bot = telebot.TeleBot(TOKEN)

    message = create_weather_message(CITY)

    msg = bot.send_message(DEST, message, parse_mode='HTML')
    bot.unpin_all_chat_messages(DEST)
    bot.pin_chat_message(DEST, msg.id, disable_notification=True)
    bot.delete_message(DEST, msg.id+1)
