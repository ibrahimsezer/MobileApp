from googletrans import Translator
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
import googletrans
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown


class Program(App):

    def build(self):
        bgimage = Image(source = "background2.jpg",size_hint_y= None, size_hint_x= None,allow_stretch = True, size = (1080,1080) )
        self.motherboard = BoxLayout()
        self.anaDuzen = BoxLayout(orientation="vertical")  # Elemanların hepsini tutan ana pencere düzenimiz
        self.ilkSatir = BoxLayout()
        self.ikinciSatir = BoxLayout()
        self.ilkSatirsol = BoxLayout(orientation = "vertical")
        self.ilkSatirsag = BoxLayout()
        self.kelime = Label(text="Kelime")
        self.kelimeKutu = TextInput(multiline=False)
        self.cevirici = Label(text="Çevirilmiş hali :",font_size='25sp')
        self.ceviriciKutu = Label(text="")
        self.dil1 = Button(text="İngilizce")
        self.dil1.bind(on_press=self.dil1kontrol)
        self.dil2 = Button(text="Almanca")
        self.dil2.bind(on_press=self.dil2kontrol)
        self.dil3 = Button(text="Fransızca")
        self.dil3.bind(on_press=self.dil3kontrol)
        self.dil4 = Button(text="İspanyolca")
        self.dil4.bind(on_press=self.dil4kontrol)
        self.dil5 = Button(text="Rusça")
        self.dil5.bind(on_press=self.dil5kontrol)
        self.dil6 = Button(text="İtalyanca")
        self.dil6.bind(on_press=self.dil6kontrol)
        self.buton = Button(text="çevir",size_hint = (0.35,0.35),pos_hint ={'x':.32, 'y':.0},font_size = '25sp')

        self.ilkSatirsol.add_widget(self.dil1)
        self.ilkSatirsol.add_widget(self.dil2)
        self.ilkSatirsol.add_widget(self.dil3)
        self.ilkSatirsol.add_widget(self.dil4)
        self.ilkSatirsol.add_widget(self.dil5)
        self.ilkSatirsol.add_widget(self.dil6)
        self.label1 =Label(text="en")
        self.buton.bind(on_press=self.kontrol)  # Butonumuza tıklama olayı ekledik
        self.ilkSatirsag.add_widget(self.kelimeKutu)
        self.ikinciSatir.add_widget(self.cevirici)
        self.ikinciSatir.add_widget(self.ceviriciKutu)
        self.ilkSatir.add_widget(self.ilkSatirsol)
        self.ilkSatir.add_widget(self.ilkSatirsag)
        # Şimdi hepsini ana düzene yerleştiriyoruz
        self.anaDuzen.add_widget(self.ilkSatir)
        self.anaDuzen.add_widget(self.ikinciSatir)
        self.anaDuzen.add_widget(self.buton)

        self.motherboard.add_widget(self.anaDuzen)
        return self.motherboard

    def dil1kontrol(self,on_press):
        self.label1.text = "en"

    def dil2kontrol(self,on_press):
        self.label1.text = "de"

    def dil3kontrol(self,on_press):
        self.label1.text = "fr"

    def dil4kontrol(self, on_press):
        self.label1.text = "es"

    def dil5kontrol(self, on_press):
        self.label1.text = "ru"

    def dil6kontrol(self, on_press):
        self.label1.text = "it"


    def kontrol(self, on_press):

        translator = Translator()
        self.yeni=self.kelimeKutu.text
        self.cuml= translator.translate(self.yeni,dest=self.label1.text)
        self.ceviriciKutu.text=str(self.cuml.text)


Program().run()