from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import Config

Config.set('kivy', 'keyboard_load', 'systemanddock')
# Window.size = (720, 1280)
Window.size = (480, 853)


def get_ingridients(mass):
    nitro = str(10 * mass / 1000)
    salt = str(15 * mass / 1000)
    starts = str(0.5 * mass / 1000)
    dextrose = str(5 * mass / 1000)
    time = str(round(mass / 500 * 2))

    return {'nitro': nitro, 'salt': salt, 'starts': starts, 'dextrose': dextrose, 'time': time}


class Container(GridLayout):
    def calculate(self):
        try:
            mass = int(self.text_input.text)
        except:
            mass = 0

        ingridients = get_ingridients(mass)
        self.salt.text = ingridients.get('salt')
        self.nitro.text = ingridients.get('nitro')
        self.dextrose.text = ingridients.get('dextrose')
        self.starts.text = ingridients.get('starts')
        self.time.text = ingridients.get('time')


class MyApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MyApp().run()
