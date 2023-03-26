class Client :

    def __init__(self,x,y,ref=0) :
        self.posx = x
        self.posy = y
        self.reference = ref
        print("x : " + str(x) + " , y : " + str(y))