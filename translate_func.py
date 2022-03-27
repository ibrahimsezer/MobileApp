# -----------------------------------DİLLER-----------------------------------

# {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani',
# 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb':
# 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican',
# 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian',
# 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german',
# 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew',
# 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish',
# 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer',
# 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian',
# 'lb': 'luxembourgish', 'mk': 'macedonian',
# 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi',
# 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto',
# 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm':
# 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala',
# 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish',
# 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur',
# 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
# -----------------------------------DİLLER-----------------------------------


import googletrans
from googletrans import Translator

def Lang_translator(lang_change):
    print(lang_change)
    translator = Translator()
    sentence = str(input("Metin giriniz."))
    global example
    example = translator.translate(sentence, dest=lang_change)
    print(example.text)
    pass
list_fav = []
lang_change = "null"
print(lang_change)
print(googletrans.LANGUAGES)


lang_change = str(input("Çevirilecek Dili seçiniz. (Türkçe olarak dil ismini yazınız.)"))

if lang_change == ("ingilizce"):
        lang_change = "en"

elif lang_change == ("almanca"):
        lang_change ="de"

elif lang_change == ("japonca"):
        lang_change ="ja"

elif lang_change == ("ispanyolca"):
        lang_change ="es"

else:
    print("Bir hata oluştu. Dili tekrar seçiniz.")

Lang_translator(lang_change)
favori = str(input("Metni favori listenize eklemek ister misiniz ? (e/h) \n"))

def List_fav(fav):
    if favori == "e":
        list_fav.append(example.text)
        list_fav.sort()
        print("Mevcut favoriler listesi : ",list_fav)

#Dillerin seçim sıralaması için alfabetik sıralama kullanılabilir.
#dict özelliği işimize yarayabilir
