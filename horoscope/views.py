from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

# Create your views here.
from django.urls import reverse


zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)',
    'taurus': "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)",
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)',
    'leo': "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)",
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)',
    'scorpio': "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)",
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января)',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)',

}


types_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}


def home(request):

    horoscope_redirect_url = reverse('horoscope_index', args=[])
    link_to_horoscope = f"<h2> Hello, my dear friend! <br> <a href='{horoscope_redirect_url}'> Click here to see horoscope page </a> </br> </h2>"

    return HttpResponse(link_to_horoscope)


def index(request):
    zodiacs = list(zodiac_dict) #получаем список КЛЮЧЕЙ словаря zodiak-dict
    # f"<li> <a href='{redirect_path}'>{sign.title()}</a> </li>"
    context = {
        'zodiacs': zodiacs,
        'zodiac_dict': {},
    }
    return render(request, 'horoscope/index.html', context=context)

# def get_info_about_zodiak_type(request):
#     zodiac_types = list(types_dict)
#     li_elem = ''
#     for _type in zodiac_types:
#         li_elem += f"<li> <a href=''>{_type}</a> </li>"
#     response = f"""
#     <ul>
#         {li_elem}
#     </ul>
# """
#     return HttpResponse(response)


def get_info_about_zodiac_sign(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    zodiacs = list(zodiac_dict)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac,
        'sign_name': description.split()[0],
        'zodiacs': zodiacs,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)



def get_info_about_zodiac_sign_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Неверный номер знака зодиака - {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac-1]
    redirect_url = reverse('horoscope_name', args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)



    # if sign_zodiak == 'leo':
    #     return HttpResponse("Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)")
    # elif sign_zodiak == 'scorpio':
    #     return HttpResponse("Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)")
    # elif sign_zodiak == 'taurus':
    #     return HttpResponse("Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)")
    # else:
    #     return HttpResponseNotFound(f"Неизвестный знак зодиака - {sign_zodiak}")
