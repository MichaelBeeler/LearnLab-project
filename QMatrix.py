from random import randint
from conjugatefunctions import ConjugationFunctions as cf

ConjugateSkillList = [cf.ProductSkill, cf.SumSkill, cf.OrSkill]


class Qmatrix:

    def __init__(self,no_of_skills,max_skill_items = 3):

        self.qmatrix = {}
        self.inx2items = []
        self.no_of_skills = no_of_skills
        self.max_skill_items = max_skill_items
        self.item2fun={}
        self.inx2skills = ['skills'+str(i) for i in range(no_of_skills)]


    def buildQmatrix(self):
        self.qmatrix = {}

        current_skill_items = 1

        for i in range(self.no_of_skills):
            itemname = "item"+str(i)
            self.inx2items.append(itemname)
            self.qmatrix[i] = [1 if k == i else 0 for k in range(self.no_of_skills)]
            self.item2fun[itemname] = cf.NoneSkill

        if current_skill_items + 1 <= self.max_skill_items:
            current_skill_items  += 1

            for i in range(len(ConjugateSkillList)):

                for j in range(self.no_of_skills):# still unsure how many items should i create per conjugate skill with different item numbers
                    conjugate_skills = [ randint(0,self.no_of_skills-1) for i in range(current_skill_items)]
                    item_index = len(self.inx2items)
                    itemname = 'item'+str(item_index)
                    self.inx2items.append(itemname)
                    self.qmatrix[item_index] = [ 1 if k in conjugate_skills else 0 for k in range(self.no_of_skills)]
                    self.item2fun[itemname] = ConjugateSkillList[i]


    def manualQmatrix(self,no_of_items_per_function = {}): # getting the information manually
        current_skill_items = 1
        self.qmatrix = {}
        for i in range(self.no_of_skills):
            itemname = "item"+str(i)
            self.inx2items.append(itemname)
            self.qmatrix[i] = [1 if k == i else 0 for k in range(self.no_of_skills)]
            self.item2fun[itemname] = cf.NoneSkill

        if current_skill_items + 1 <= self.max_skill_items:
            current_skill_items  += 1

            for i in range(len(ConjugateSkillList)):

                for j in range(self.no_of_skills):# still unsure how many items should i create per conjugate skill with different item numbers
                    conjugate_skills = [ randint(0,self.no_of_skills-1) for i in range(current_skill_items)]
                    item_index = len(self.inx2items)
                    itemname = 'item'+str(item_index)
                    self.inx2items.append(itemname)
                    self.qmatrix[item_index] = [ 1 if k in conjugate_skills else 0 for k in range(self.no_of_skills)]
                    self.item2fun[itemname] = ConjugateSkillList[i]






if __name__ == '__main__':

    qm = Qmatrix(20,2)

