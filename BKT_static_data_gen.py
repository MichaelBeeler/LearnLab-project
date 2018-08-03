
# coding: utf-8

# In[117]:

get_ipython().magic('matplotlib inline')
import random, numpy as np, math, matplotlib.pyplot as plt, pandas as pd


# In[61]:

# class Learner:
#     def __init__(self,ID,skills): #skills is array of 0-1 values for skills
#         skilldict = {}
#         for i in range(len(skills)):
#             skilldict[i] = skills[i]
#         self.numskills = len(skills)
#         self.ID = ID


# In[ ]:

# class GeneralQuestion:
#     def __init__(self,qID,f)
#         self.function = f.function


# In[22]:

# class Pmatrix:
#     def __init__(self,J,K,Type):
#         self.numskills = K
#         self.numlearners = J
#         typedict = {"binary":0,"cts":1,"z":2}
#         self.type = typedict[Type]
#         if self.type == 0:
#             M = numpy.zeros([J,K],dtype="int")
#         if self.type == 1:
#             M = numpy.zeros([J,K],dtype="float")
#         if self.type == 2:
#             M = numpy.zeros([J,K],dtype="float")


# In[ ]:




# In[4]:

class Question:
    def __init__(self,guess,slip):
        #add error handling
        self.g = guess
        self.s = slip
    def responses(self,p,n):
        x = p*(1-self.s)+(1-p)*(self.g)
        answers = numpy.random.binomial(1,x,(n,1))
        return(answers)
        


# In[221]:

def estimate(data,prior,question,pT):
    pT = pT #irrelevant, but want it to accept same argument as estimateWTrans
    estimates = []
    estimates.append(prior)
    for i in range(0,len(data)):
        if data[i] == 0:
            estimates.append(estimates[i]*(question.s)/(estimates[i]*(question.s)+(1-estimates[i])*(1-question.g)))
        elif data[i] == 1:
            estimates.append(estimates[i]*(1-question.s)/(estimates[i]*(1-question.s)+(1-estimates[i])*(question.g)))
        else:
            print("data isn't 0 or 1") #add error handling...
    return(estimates)
    
def estimateWTrans(data,prior,question,pT):
    estimates = []
    estimates.append(prior) 
    for i in range(0,len(data)):
        if data[i] == 0:
            estimates.append(estimates[i]*(question.s)/(estimates[i]*(question.s)+(1-estimates[i])*(1-question.g)))
        elif data[i] == 1:
            estimates.append(estimates[i]*(1-question.s)/(estimates[i]*(1-question.s)+(1-estimates[i])*(question.g)))
        else:
            print("data isn't 0 or 1") #add error handling...
        estimates[i+1] = estimates[i+1]+(1-estimates[i+1])*pT
    return(estimates)
            


# In[254]:

def SimulateAndFit(Nsims,NQuestions,Question,skill_level,transition_prob,sample_period,canTransition,threshold,prior):

    Q = Question
    N = Nsims
    NQ = NQuestions
    p = skill_level
    pT = transition_prob
    t = sample_period
    T = float(pT*canTransition)

    
    sample_t = min(t,NQ)
    E = {}
    if not canTransition:
        est = estimate
    else:
        est = estimateWTrans
        
    count = 0
    Sum = 0
    for i in range(N):
        resp = Q.responses(p,NQ)
        e = est(resp,prior,Q1,pT)
        E[i] = e
        plt.plot(E[i])
        if max(E[i][0:sample_t]) >= threshold:
            count=count+1
        Sum = Sum + E[i][sample_t]
        avg = Sum/N

        #x = p*(1-Q1.s)+(1-p)*(Q1.g)
    
    plt.plot(p*np.ones(NQ+1)) 
    plt.title("Guess="+str(Q.g)+", Slip="+str(Q.s)+", P(L_0)="+str(prior)+", P(T)="+str(T))
    plt.xlabel("Observation t = 1,...,"+str(NQ)+".   "+str(N)+" Simulations.")
    plt.ylabel("BKT Posterior for P(L_t). ")


    #Percent crossing posterior threshold
    percentcrossing = count/N*100
    print("Percent crossing Pr(L)>"+str(threshold)+" by t<"+str(sample_t)+": "+ str(percentcrossing)+"%")
    #Average value at t = min(20,NQ)
    
    print("Average Pr(L) value at t = "+str(sample_t)+": "+str(avg))



        
        


# In[289]:

#Args: Nsims,NQuestions,Question,skill_level,transition_prob,
#sample_period,canTransition,threshold,prior
Q1 = Question(.25,.02)
N = 20
NQ = 1000
p=.7
pT =.2
sample_period = 1000
canTrans = 0
threshold = 0.9
prior = .5
SimulateAndFit(N,NQ,Q1,p,pT,sample_period,canTrans,threshold,prior)


# In[288]:

pT=.2
SimulateAndFit(1,1000,Q1,.49,pT,sample_period,1,threshold,.5)


# In[ ]:




# In[209]:

est = estimate


# In[210]:

est([1,1,1,1],.2,Q1)


# In[ ]:



