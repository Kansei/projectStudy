import numpy as np

class ConSeqData:
    def __init__(self,end,len,intron,prob,weight):
        self.end = end
        self.len = len
        self.intron = intron #イントロンの始まり/終わり地点
        self.prob = prob/100.0
        self.weight = weight #重み行列

        self.sequence = ""
        self.c_site = []
        self.i_site = []
        self.score = []


con5 = []
con3 = []
con5.append(ConSeqData(5,7,2,53.58,
np.array([
[0.5,0.2,0.15,0.15],
[0.15,0.11,0.7,0.04],
[0,0,1.0,0],
[0,1.0,0,0],
[0.5,0,0.5,0],
[1.0,0,0,0],
[0,0,1.0,0],
])
))

con5.append(ConSeqData(5,6,3,45.10,
np.array([
[0.35,0.09,.016,0.4],
[0.8,0.09,0.06,0.05],
[0.08,0.01,0.91,0],
[0,0,1.0,0],
[0,1.0,0,0],
[0.7,0.08,0.15,0.07],
])
))

con3.append(ConSeqData(3,9,7,64.55,
np.array([
[0.1,0.42,0.12,0.36],
[1.0,0.43,1.0,0.37],
[0.08,0.48,0.07,0.37],
[0.08,0.5,0.08,0.34],
[0.23,0.25,0.24,0.28],
[0,0,0,1.0],
[1.0,0,0,0],
[0,0,1.0,0],
[0.24,0.11,0.48,0.17],
])
))

con3.append(ConSeqData(3,6,4,29.01,
np.array([
[0.1,0.6,0.05,0.25],
[0.2,0.39,0.15,0.26],
[0,1.0,0,0],
[1.0,0,0,0],
[0,0,1.0,0],
[0.25,0.11,0.5,0.14],
])
))

con3.append(ConSeqData(3,7,5,5.98,
np.array([
[0.1,0.59,0.08,0.23],
[0.11,0.6,0.08,0.21],
[0.32,0.3,0.18,0.2],
[0.94,0,0.06,0],
[1.0,0,0,0],
[0,0,1.0,0],
[0.24,0.1,0.51,0.15],
])
))

