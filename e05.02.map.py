##importation
import random as rand
import math as math

print '\nSimulating. Please wait...'
def piSimulation(convcrit):
    ##initialize necessary values
    pi = math.pi
    n = 0
    d = 0
    ratios = []
    simulating = True # use as a sentinel
    
    while simulating:
        x = rand.random()
        y = rand.random()
        if x**2 + y**2 <= 1.0:
            n += 1
        d += 1
        ratio = 4 * n * 1./d

        if abs(ratio-pi) / pi <= convcrit:
            break
    return d

def experiment(number, convcrit):
    results = []
    iterations = range(number)
    for i in iterations:
        results.append(piSimulation(convcrit))
    return results

convcritlist = [.01, .001, .0001, .00001, .000001]
iterations = [10, 10, 10, 10, 10]

results = map(experiment, iterations, convcritlist)
print 'The following list of lists is the number of iterations it took to generate pi at varying confidence levels:\n', results

def avg(l):
    return float(sum(l))/len(l)

def sd(l):
    mean = avg(l)
    meanlist = []
    length = range(len(l))
    for i in length:
        meanlist.append(mean)
    nums = (map(lambda x,y: (x-y)**2, l, meanlist))
    num = sum(nums)
    denom = len(l) - 1
    return (num / denom)**.5

results_averages = map(avg, results)
print 'The averages of our results list was:\n', results_averages
results_sds = map(sd, results)
print 'The standard deviations of our results list was:\n', results_sds
