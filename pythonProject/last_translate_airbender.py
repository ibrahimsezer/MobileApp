import googletrans
from googletrans import Translator
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Program(App):
    def build(self):
        self.anaDuzen = BoxLayout(orientation="vertical")  # Elemanların hepsini tutan ana pencere düzenimiz

        self.ilkSatir = BoxLayout()
        self.ikinciSatir = BoxLayout()

        self.kelime = Label(text="Kelime")
        self.kelimeKutu = TextInput(multiline=False)

        self.cevirici = Label(text="Çevirilmiş hali :")
        self.ceviriciKutu = Label(text="")

        self.buton = Button(text="çevir")
        self.buton.bind(on_press=self.kontrol)  # Butonumuza tıklama olayı ekledik

        self.ilkSatir.add_widget(self.kelime)
        self.ilkSatir.add_widget(self.kelimeKutu)

        self.ikinciSatir.add_widget(self.cevirici)
        self.ikinciSatir.add_widget(self.ceviriciKutu)

        # Şimdi hepsini ana düzene yerleştiriyoruz

        self.anaDuzen.add_widget(self.ilkSatir)
        self.anaDuzen.add_widget(self.ikinciSatir)
        self.anaDuzen.add_widget(self.buton)

        return self.anaDuzen

    def kontrol(self, on_press):
        translator = Translator()
        self.yeni=self.kelimeKutu.text



        self.cuml= translator.translate(self.yeni,dest="en")

        self.ceviriciKutu.text=str(self.cuml.text)

Program().run()