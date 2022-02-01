#Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
#до минуты: <s> сек;
#до часа: <m> мин <s> сек;
#до суток: <h> час <m> мин <s> сек;
#* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
one_minute = 60
one_hour = 3600
one_day = 86400
one_week = 604800

duration = int (input('Укажите продолжительность в секундах: '))

if duration<one_minute:
    print ('{} сек'.format(duration))
elif one_minute <= duration < one_hour:
    me_minute=duration//one_minute
    me_second=duration%one_minute
    print ('{} мин {} сек'.format(me_minute,me_second))
elif one_hour <= duration < one_day:
    me_hour=duration // one_hour
    duration=duration % one_hour
    me_minute = duration // one_minute
    me_second = duration % one_minute
    print ('{} час {} мин {} сек'.format(me_hour,me_minute,me_second))
elif one_day <= duration < one_week:
    me_day = duration // one_day
    duration=duration % one_day
    me_hour = duration // one_hour
    duration = duration % one_hour
    me_minute = duration // one_minute
    me_second = duration % one_minute
    print('{} дн {} час {} мин {} сек'.format(me_day, me_hour, me_minute, me_second))
