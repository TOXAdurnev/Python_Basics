# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час

def convert_time_format(duration):

    dd = duration // 86400
    hh = (dd * 86400) // 3600
    mm = duration % 86400 % 3600 // 60
    ss = duration % 86400 % 3600 % 60

    if dd > 0:
        return f'{dd} дн {hh} час {mm} мин {ss} сек'
    elif hh > 0:
        return f'{hh} час {mm} мин {ss} сек'
    elif mm > 0:
        return f'{mm} мин {ss} сек'
    return f'{ss} сек'


duration = 168943236
print(convert_time_format(duration))
