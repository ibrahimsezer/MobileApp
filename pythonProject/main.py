"""
PROGRAMI ÇALIŞTIRMAK İÇİN GEREKLİ OLAN MODÜLLERİ VE FRAMEWORK'U TERMİNELDEN KURUNUZ.

pip install Kivy
pip install googletrans==4.0.0-rc1
pip install googletrans

"""
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

class Çeviri(App):

    def build(self):

        self.AnaDuzen = BoxLayout(orientation="vertical")  # Elemanların hepsini tutan ana pencere düzenimiz
        self.İlkSatir = BoxLayout()
        self.İkinciSatir = BoxLayout()
        self.İlkSatirsol = BoxLayout(orientation = "vertical")
        self.İlkSatirsag = BoxLayout()
        self.Kelime = Label(text="Kelime")
        self.KelimeKutu = TextInput(multiline=False)
        self.Cevirici = Label(text="Çevirilmiş hali :",font_size='25sp')
        self.CeviriciKutu = Label(text="")
        self.Dil1 = Button(text="İngilizce")
        self.Dil1.bind(on_press=self.Dil1kontrol)
        self.Dil2 = Button(text="Almanca")
        self.Dil2.bind(on_press=self.Dil2kontrol)
        self.Dil3 = Button(text="Fransızca")
        self.Dil3.bind(on_press=self.Dil3kontrol)
        self.Dil4 = Button(text="İspanyolca")
        self.Dil4.bind(on_press=self.Dil4kontrol)
        self.Dil5 = Button(text="Rusça")
        self.Dil5.bind(on_press=self.Dil5kontrol)
        self.Dil6 = Button(text="İtalyanca")
        self.Dil6.bind(on_press=self.Dil6kontrol)
        self.buton = Button(text="çevir",size_hint = (0.35,0.35),pos_hint        ={'x':.32, 'y':.0},font_size = '25sp')

        self.İlkSatirsol.add_widget(self.Dil1)
        self.İlkSatirsol.add_widget(self.Dil2)
        self.İlkSatirsol.add_widget(self.Dil3)
        self.İlkSatirsol.add_widget(self.Dil4)
        self.İlkSatirsol.add_widget(self.Dil5)
        self.İlkSatirsol.add_widget(self.Dil6)
        self.label1 =Label(text="en")
        self.buton.bind(on_press=self.kontrol)  # Butonumuza tıklama olayı ekledik
        self.İlkSatirsag.add_widget(self.KelimeKutu)
        self.İkinciSatir.add_widget(self.Cevirici)
        self.İkinciSatir.add_widget(self.CeviriciKutu)
        self.İlkSatir.add_widget(self.İlkSatirsol)
        self.İlkSatir.add_widget(self.İlkSatirsag)
        # Şimdi hepsini ana düzene yerleştiriyoruz
        self.AnaDuzen.add_widget(self.İlkSatir)
        self.AnaDuzen.add_widget(self.İkinciSatir)
        self.AnaDuzen.add_widget(self.buton)


        return self.AnaDuzen

    def Dil1kontrol(self,on_press):
        self.label1.text = "en"

    def Dil2kontrol(self,on_press):
        self.label1.text = "de"

    def Dil3kontrol(self,on_press):
        self.label1.text = "fr"

    def Dil4kontrol(self, on_press):
        self.label1.text = "es"

    def Dil5kontrol(self, on_press):
        self.label1.text = "ru"

    def Dil6kontrol(self, on_press):
        self.label1.text = "it"


    def kontrol(self, on_press):

        translator = Translator()
        self.Yeni=self.KelimeKutu.text
        self.Cuml= translator.translate(self.Yeni,dest=self.label1.text)
        self.CeviriciKutu.text=str(self.Cuml.text)

Çeviri().run()
