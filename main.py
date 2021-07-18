from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.core.window import Window
import database_connection


Window.clearcolor = (1, 1, 1, 1)
Window.size = (400, 600)

class PoopButton(Widget):
    pass

class BottomButton(Button):
    pass

class AppScreen(Widget):
    pass
        


class AppPannolini(App):
    def build(self):
        schermo = AppScreen()
        return AppScreen()

if __name__ == '__main__':
    AppPannolini().run()
