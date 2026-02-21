from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from core.game_logic import QueensGame, TangoGame, ZipGame

Window.clearcolor = (0.07, 0.07, 0.07, 1)


class DashboardScreen(MDScreen):
    pass


class QueensScreen(MDScreen):
    def on_pre_enter(self):
        self.game = QueensGame()


class TangoScreen(MDScreen):
    def on_pre_enter(self):
        self.game = TangoGame()


class ZipScreen(MDScreen):
    def on_pre_enter(self):
        self.game = ZipGame()


class BrainGamesEliteApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_file("kv/style.kv")

    def animate_success(self, widget):
        Animation(scale=1.1, d=0.15) + Animation(scale=1.0, d=0.15)
        Animation(opacity=1, d=0.2).start(widget)


if __name__ == "__main__":
    BrainGamesEliteApp().run()
