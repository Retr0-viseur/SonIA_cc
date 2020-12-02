class Bot(object):

    def __init__(self):
        pass

    def act(self, xdif, ydif, vel):
        if vel<-7:
            if ydif<50:
                return 1
        if vel>=-7:
            if ydif<55:
                return 1