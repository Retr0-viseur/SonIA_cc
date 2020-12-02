class Bot(object):

    def __init__(self):
        pass

    def act(self, xdif, ydif, vel):
        if vel<-7:
            if ydif<40:
                return 1
        if 4>vel>=-7:
            if ydif<35:
                return 1