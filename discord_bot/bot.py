import discord
import asyncio
from datetime import datetime, timedelta
from time import sleep

import config

from words import *



# Расчет разницы в 30 минут
def delta_30():
    return datetime.now() - timedelta(minutes=90)

# Расчет разницы в 15 минут
def delta_15():
    return datetime.now() - timedelta(minutes=105)

# Расчет самого респа
def delta_5():
    return datetime.now() - timedelta(minutes=115)




# Функция проверки времени от дня недели
def check_time(day):
    if datetime.strftime(delta_30(), '%H:%M') in respawn[day]:                    # Проверка времени в таблице респа
        x = datetime.strftime(delta_30(), '%H:%M')                                  # Приведение разницы во времени к формату '12:00'
        
        return('Время сейчас: ' + datetime.strftime(datetime.now(), '%H:%M') + '\nЧерез 30 минут реснется ' + respawn[day][x])                         # Возврат сообщения за 30 минут до респа

    
    elif datetime.strftime(delta_15(), '%H:%M') in respawn[day]:                                                                                       # Возврат сообщения за 15 минут до респа
        x = datetime.strftime(delta_15(), '%H:%M')

        return('Время сейчас: ' + datetime.strftime(datetime.now(), '%H:%M') + '\nЧерез 15 минут реснется ' + respawn[day][x])

    
    elif datetime.strftime(delta_5(), '%H:%M') in respawn[day]:                                                                                       # Возврат сообщения за 5 минут до респа
        x = datetime.strftime(delta_5(), '%H:%M')

        return('Время сейчас: ' + datetime.strftime(datetime.now(), '%H:%M') + '\nЧерез 5 минут реснется ' + respawn[day][x])
    

    
    


# Основная проверка времени до респа
def check_date():
    
    
    now = datetime.strftime((datetime.now() - timedelta(minutes=57)), '%A')
    
    # Цикл проверки времени перед респом боссов(За 30 минут и за 15 минут)
    while True:
        if now == 'Monday':                                       # Проверка дня недели
            return check_time('Monday')
        
        elif now == 'Tuesday':
            return check_time('Tuesday')
        
        elif now == 'Wednesday':
            return check_time('Wednesday')
        
        elif now == 'Thursday':
            return check_time('Thursday')
        
        elif now == 'Friday':
            return check_time('Friday')
        
        elif now == 'Saturday':
            return check_time('Saturday')
        
        elif now == 'Sunday':
            return check_time('Sunday')
        
        else:
            print('check_false')
            return 'Failed check!'
            

################################################################
##########################EKO-BOT###############################


client = discord.Client()


async def my_background_task():
    
    await client.wait_until_ready()
    
    channel = client.get_channel(289826825054715914)
    while True:
        message = check_date()
        
        if message == '' or message == None:
            pass
            print('60sec pass')
            
        else:
            await channel.send(message, file=discord.File('img/' + message.split(' ')[-1].replace('/', '') + '.png'))          #Отправка сообщения в чат и следом файл, название которого зависит от имени босса
            print(message)
        
        await asyncio.sleep(60) # task runs every 60 seconds

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(my_background_task())
client.run(config.TOKEN)