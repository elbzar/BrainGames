import json
import os
from datetime import date
DATA_FILE = 'profile.json'
DEFAULT_DATA = {'coins': 100, 'streak': 0, 'last_played': None, 'hint_packs': 3, 'hard_mode_unlocked': False, 'stats': {'queens': {'played': 0, 'won': 0}, 'tango': {'played': 0, 'won': 0}, 'zip': {'played': 0, 'won': 0}}, 'purchases': []}
class StoreManager:
    @staticmethod
    def load_data():
        if not os.path.exists(DATA_FILE): StoreManager.save_data(DEFAULT_DATA); return DEFAULT_DATA
        try:
            with open(DATA_FILE, 'r') as f: return json.load(f)
        except: return DEFAULT_DATA
    @staticmethod
    def save_data(data):
        with open(DATA_FILE, 'w') as f: json.dump(data, f)
    @staticmethod
    def update_streak(data):
        today = str(date.today()); last_played = data.get('last_played')
        if last_played != today:
            if last_played: data['streak'] = (data['streak'] + 1) if (date.today() - date.fromisoformat(last_played)).days == 1 else 1
            else: data['streak'] = 1
            data['last_played'] = today; StoreManager.save_data(data)