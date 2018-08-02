# coding=utf-8
from random import randint,randrange
import numpy as np
import random
class Pmatrix:

    _Pmatrix_Binary = 1
    _Pmatrix_Continuous = 2
    _Pmatrix_Zcore = 3
    _Pmatrix_Constant = 4

    def __init__(self, exp,type=_Pmatrix_Binary):
        self.qmatrix = exp.qmatrix
        self.numlearners = len(exp.inx2student)
        self.no_of_skills = exp.no_of_skills
        self.pmatrix = {}
        self.type = type
        self.numItems = len(exp.inx2items)
        self.inx2students = exp.inx2student


    def build_pmatrix(self,c=0):

        for s in range(self.numlearners):
            if self.type == Pmatrix._Pmatrix_Binary:
                self.pmatrix[s] = [randint(0,1) for k in range(self.no_of_skills)]
            elif self.type == Pmatrix._Pmatrix_Continuous:
                self.pmatrix[s] = [round(randrange(0,100,self.no_of_skills)*0.01,2) for k in range(self.no_of_skills)]
            elif self.type == Pmatrix._Pmatrix_Zcore:
                self.pmatrix[s] = [round(randrange(-100,100,self.no_of_skills)*0.01,2) for k in range(self.no_of_skills)]
            elif self.type == Pmatrix._Pmatrix_Constant:
                self.pmatrix[s] = [c for k in range(self.no_of_skills)]

    def print(self):
        for key in self.pmatrix:
            print(self.inx2students[key].name +" - " + "\t".join(list(map(str,self.pmatrix[key]))))

if __name__ == '__main__':
    print("Pmatrix Class")


