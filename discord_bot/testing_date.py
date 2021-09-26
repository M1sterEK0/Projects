from datetime import datetime, timedelta
from time import sleep
from words import *


active = True



# Расчет разницы в 30 минут
def delta_30():
    return datetime.now() - timedelta(minutes=90)

# Расчет разницы в 30 минут
def delta_15():
    return datetime.now() - timedelta(minutes=105)




# Функция проверки времени от дня недели
def check_time(day:str):
    if datetime.strftime(delta_30(), '%H:%M') in respawn[day]:                    # Проверка времени в таблице респа
        x = datetime.strftime(delta_30, '%H:%M')                                  # Приведение разницы во времени к формату '12:00'
        
        return('Время сейчас:' + datetime.strftime(datetime.now(), '%H:%M') + 'Через 30 минут реснется' + respawn[day][x])                         # Возврат имени босса из таблицы респа
            
    elif datetime.strftime(delta_15(), '%H:%M') in respawn[day]:
        x = datetime.strftime(delta_15, '%H:%M')

        return('Время сейчас:' + datetime.strftime(datetime.now(), '%H:%M') + 'Через 15 минут реснется' + respawn[day][x])




# Основная проверка времени до респа
def check_date():
    global active
    
    now = datetime.strftime(datetime.now(), '%A')
    
    # Цикл проверки времени перед респом боссов(За 30 минут и за 15 минут)
    while active:
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
            sleep(60)