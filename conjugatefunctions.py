# coding=utf-8
import numpy as np

class ConjugationFunctions:


    @staticmethod
    def ConjuctiveSkill(skill_list):
        return np.mean(skill_list)

    @staticmethod
    def DisjunctiveSkill(skill_list):
        return np.max(skill_list)

    @staticmethod
    def ProductSkill(skill_list):
        x = 0
        for skill in skill_list:
            x *= skill
        return x

    @staticmethod
    def NoneSkill(skill_list):
        return np.average(skill_list)

    @staticmethod
    def SquareSkill(skill):
        return skill * skill



