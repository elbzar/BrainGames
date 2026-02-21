from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivymd.uix.button import MDFlatButton
from core.data_manager import StoreManager
from core.game_logic import GameLogic
class SplashScreen(Screen): pass
class MenuScreen(Screen): pass
class GameScreen(Screen): pass
class BrainGamesApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette='BlueGray'; self.user_data=StoreManager.load_data(); StoreManager.update_streak(self.user_data)
        with open('ui/main.kv','r') as f: return Builder.load_string(f.read())
    def on_start(self): Clock.schedule_once(lambda dt: self.switch_screen('menu'), 2)
    def switch_screen(self, n): self.root.current=n
    def setup_game(self, n):
        self.current_game=n; s=self.root.get_screen('game'); s.ids.gt.title=n; g=s.ids.grid_layout; g.clear_widgets()
        d=getattr(GameLogic, f'generate_{n.lower()}')('Medium'); self.board_state=d['board']; size=d['size']; g.cols=size
        for r in range(size):
            for c in range(size):
                b=MDFlatButton(text='',size_hint=(1,1),md_bg_color=(0.9,0.9,0.9,1))
                b.bind(on_release=lambda x,row=r,col=c: self.handle_move(row,col,x)); g.add_widget(b)
        self.switch_screen('game')
    def handle_move(self, r, c, b):
        if self.current_game=='Queens': self.board_state[r][c]=1 if self.board_state[r][c]==0 else 0; b.text='Q' if self.board_state[r][c]==1 else ''
    def validate_current_game():
        if getattr(GameLogic, f'validate_{self.current_game.lower()}')(self.board_state): self.switch_screen('menu')
if __name__=='__main__': BrainGamesApp().run()