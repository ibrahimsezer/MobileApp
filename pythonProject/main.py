from kivy.app import App
from kivy.uix.widget import Widget
import googletrans
from googletrans import Translator
import pandas as pd
class MainWidget(Widget):
    pass
#ÇEVİRİ MODÜLÜ
translator = Translator()
sentence = str(input("Cümle giriniz:"))
example = translator.translate(sentence,dest="tr")

print(example.src)
"tr" # orjinal dil
print(example.dest)
"en" # çevrilen dil
print(example.origin)
"Olmak ya da olmamak"
print(example.text)
"To be or not to be"
#def callback(instance):
    #print('The button <%s> is being pressed' % instance.text)

class TranslatorApp(App):
    pass

TranslatorApp().run()