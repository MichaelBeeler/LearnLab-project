import random, numpy, math
class Question:
    def __init__(self,guess,slip):
        #add error handling
        self.g = guess
        self.s = slip
    def responses(self,p,n):
        x = p*(1-self.s)+(1-p)*(self.g)
        answers = numpy.random.binomial(1,x,(n,1))
        return(answers)
def estimate(data,prior,question):
    estimates = []
    estimates.append(prior)
    for i in range(0,len(data)):
        if data[i] == 0:
            estimates.append(estimates[i]*(question.s)/(estimates[i]*(question.s)+(1-estimates[i])*(1-question.g)))
        elif data[i] == 1:
            estimates.append(estimates[i]*(1-question.s)/(estimates[i]*(1-question.s)+(1-estimates[i])*(question.g)))
        else:
            print("data isn't 0 or 1") #add error handling...
    print(estimates)
            Q1 = Question(.2,.2)
r = Q1.responses(.1,20)
estimate(r,.5,Q1)

estimate((0,0,0,1,1,1,0),.5,Q1)

estimate((1,0,0,1,1,0,0),.5,Q1)
