class Sommet :

    def __init__(self,i,j,ref=0) :
        self.posx = i
        self.posy = j
        self.reference = ref
        self.id = ref

    
    def __str__(self) -> str:
        return f'(x = {self.posx}, y = {self.posy}, reference = {self.reference})'

