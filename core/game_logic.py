import random
class GameLogic:
    @staticmethod
    def generate_queens(diff): size={'Easy':4,'Medium':6,'Hard':8}[diff]; return {'size':size,'board':[[0]*size for _ in range(size)]}
    @staticmethod
    def validate_queens(b): n=len(b); qs=[(r,c) for r in range(n) for c in range(n) if b[r][c]==1]
        if len(qs)!=n: return False
        for i in range(len(qs)): 
            for j in range(i+1,len(qs)): 
                r1,c1=qs[i]; r2,c2=qs[j]
                if r1==r2 or c1==c2 or abs(r1-r2)==abs(c1-c2): return False
        return True
    @staticmethod
    def generate_tango(diff): size=6; b=[[0]*size for _ in range(size)]; return {'size':size,'board':b}
    @staticmethod
    def validate_tango(b): return True
    @staticmethod
    def generate_zip(diff): size=5; b=[[0]*size for _ in range(size)]; return {'size':size,'board':b}
    @staticmethod
    def validate_zip(b): return True