from random import randint,sample
from conjugatefunctions import ConjugationFunctions as cf
from PMatrix import Pmatrix
ConjugateSkillList = [ cf.DisjunctiveSkill, cf.ConjuctiveSkill]
import copy
import numpy as np

class Experiment:

    def __init__(self,guess=0.2,slip=0.1,transfer=0):

        self.qmatrix = {}

        self.no_of_skills = 0
        self.max_skill_items = 0

        self.item2fun={}

        self.guess=guess
        self.slip =slip
        self.transfer=transfer

        self.inx2items = []
        self.inx2student = []
        self.inx2skills = []



    def print(self):
        print("Items  - ", " , ".join(self.inx2skills))
        for key in self.qmatrix:
            print(self.inx2items[key].name +" - " + "\t".join(list(map(str,self.qmatrix[key])))+" - " + self.inx2items[key].function.__name__)

    def buildQmatrix(self,no_of_skills,max_skill_items = 3,single_skill_items=True,type=[]):
        self.qmatrix = {}
        self.no_of_skills = no_of_skills
        self.max_skill_items = max_skill_items
        self.inx2skills = ['skills'+str(i) for i in range(no_of_skills)]

        current_skill_items = 1
        if single_skill_items == True:
            for i in range(self.no_of_skills):
                itemname = "item"+str(i)

                self.qmatrix[i] = [1 if k == i else 0 for k in range(self.no_of_skills)]
                self.item2fun[itemname] = cf.NoneSkill
                item = None
                item = Item(id=len(self.inx2items),name=itemname)
                item.setFunction(cf.NoneSkill)
                self.inx2items.append(copy.copy(item))

        while current_skill_items  < self.max_skill_items:
            current_skill_items  += 1
            for i in range(len(type)):

                for j in range(self.no_of_skills):
                    conjugate_skills = sample(range(0,self.no_of_skills-1),current_skill_items)
                    item_index = len(self.inx2items)
                    itemname = 'item'+str(item_index)
                    self.qmatrix[item_index] = [ 1 if k in conjugate_skills else 0 for k in range(self.no_of_skills)]
                    self.item2fun[itemname] = type[i]
                    item = None
                    item = Item(id=len(self.inx2items),name=itemname)
                    item.setFunction(type[i])
                    self.inx2items.append(copy.copy(item))

    def buildStudents(self,no_of_students):
        for i in range(no_of_students):
            student = None
            student = Student('student'+str(i),id)
            self.inx2student.append(copy.copy(student))

    def buildStudentResponse(self,pmatrix,n=1):
        for st in self.inx2student:
            for item in self.inx2items:
                for kc_list in self.qmatrix[item.id]:
                    kc_mastery = []
                    for kc_id in range(len(kc_list)):
                        if kc_list[kc_id] == 1:
                            kc_mastery.append(pmatrix[st.id][kc_id])
                    mastery
                    self.studentItemResponse(n=n)
                    print(st, item.name,kc_id,)

    def responses(self,p,n ):
        x = p*(1-self.s)+(1-p)*(self.g)
        answers = np.random.binomial(1,x,(n,1))
        return(answers)


class Item:

    def __init__(self,id,name,guess=0.1,slip=0.1):

        self.guess = guess
        self.slip = slip
        self.function = cf.NoneSkill
        self.name  = name
        self.id = id

    def setFunction(self,function):
        self.function = function

    def print(self):
        print("Item Name : ",)

class Student:

    def __init__(self,name,id):
        self.name  = name
        self.studentid = id

    def print(self):
        print(self.name)


if __name__ == '__main__':
    guess = 0.1
    slip = 0.1
    transfer = 0.1
    num_Students = 10
    num_Skills = 10
    max_combined_skills = 1
    use_single_skill = True
    type_of_skills = [cf.ConjuctiveSkill]
    pmatrix_type = Pmatrix._Pmatrix_Constant
    ConstantMasteryValue = 0.5

    expi = Experiment(guess=guess,
                    slip=slip,
                    transfer=transfer
                    )

    expi.buildStudents(no_of_students=num_Students)

    expi.buildQmatrix(no_of_skills=num_Skills,
                    max_skill_items=max_combined_skills,
                    single_skill_items=use_single_skill,
                    type=type_of_skills)

    pm = Pmatrix(exp=expi,type=pmatrix_type)
    pm.build_pmatrix(c=ConstantMasteryValue)

    expi.buildStudentResponse(pm,n=1)
    expi.print()
    pm.print()


















