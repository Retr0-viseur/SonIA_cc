class Bot(object):

    def __init__(self):
        pass

    def act(self, xdif, ydif, vel):
        if vel<-7:
            if ydif<60:
                return 1
        if vel>=-7:
            if ydif<75:
                return 1