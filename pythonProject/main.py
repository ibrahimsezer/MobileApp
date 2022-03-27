
############################################################
#-------Terminal üzerinden kurmamız gereken modüller -------
#pip install googletrans==4.0.0-rc1
#pip install kivy
#pip install pandas
############################################################
from kivy.app import App
from kivy.uix.widget import Widget
import googletrans
from googletrans import Translator
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
import pandas as pd
class MainWidget(Widget):
    pass


#ÇEVİRİ MODÜLÜ
translator = Translator()
sentence = str(input("Cümle giriniz:"))
example = translator.translate(sentence,dest="en")

print(example.src)
#"tr" # orjinal dil
print(example.dest)
#"en" # çevrilen dil
print(example.origin)
#"Olmak ya da olmamak"
print(example.text)
#"To be or not to be"
def callback(instance):
    print('The button <%s> is being pressed' % instance.text)

class TranslatorApp(App):
    pass


TranslatorApp().run()
