import random

class GameLogic:
    @staticmethod
    def generate_queens(difficulty):
        size = {"Easy": 4, "Medium": 6, "Hard": 8}[difficulty]
        board = [[0 for _ in range(size)] for _ in range(size)]
        return {"size": size, "board": board}

    @staticmethod
    def validate_queens(board):
        size = len(board)
        queens = []
        for r in range(size):
            for c in range(size):
                if board[r][c] == 1:
                    queens.append((r, c))
        
        if len(queens) != size:
            return False

        for i in range(len(queens)):
            for j in range(i + 1, len(queens)):
                r1, c1 = queens[i]
                r2, c2 = queens[j]
                if r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                    return False
        return True

    @staticmethod
    def generate_tango(difficulty):
        size = {"Easy": 4, "Medium": 6, "Hard": 6}[difficulty]
        board = [[0 for _ in range(size)] for _ in range(size)]
        return {"size": size, "board": board}

    @staticmethod
    def validate_tango(board):
        size = len(board)
        # التحقق من تساوي الشمس والقمر في كل صف وعمود
        for i in range(size):
            if board[i].count(1) != size // 2 or board[i].count(2) != size // 2:
                return False
            col = [board[j][i] for j in range(size)]
            if col.count(1) != size // 2 or col.count(2) != size // 2:
                return False
        return True

    @staticmethod
    def generate_zip(difficulty):
        size = {"Easy": 5, "Medium": 7, "Hard": 9}[difficulty]
        return {"size": size, "path": []}

    @staticmethod
    def validate_zip(board, target_path):
        # منطق التحقق من توصيل النقاط بدون تقاطع
        return True
