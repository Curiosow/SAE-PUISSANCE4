import body

class pion:
    def __init__(self, couleur, x, y):
        self.color = couleur
        self.x = x
        self.y = y

    def realColor(self):
        if(self.color == "Jaune"):
            return body.Jaune
        elif(self.color == "Rouge"):
            return body.Rouge
        else:
            return body.Marron