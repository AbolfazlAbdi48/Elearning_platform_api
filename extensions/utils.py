from string import digits, ascii_lowercase, ascii_uppercase
from random import choice as random_choice
from . import jalali


def jalali_converter(time):
    jmonths = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد',
               'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']

    time_to_str = f'{time.year},{time.month},{time.day}'
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list = list(time_to_tuple)

    for index, month in enumerate(jmonths):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break

    output = f'{time_to_list[2]} {time_to_list[1]} {time_to_list[0]} '

    return output


def slug_generator(size: int = 10, char: str = digits + ascii_uppercase + ascii_lowercase) -> str:
    return "".join(random_choice(char) for _ in range(size))
