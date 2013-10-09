##importation
import random as rand
import math as math

##initialize necessary values
pi = math.pi
n = 0
d = 0
ratios = []
xs = []
ys = []
inputting = True # use as sentinel
simulating = True # use as a sentinel

while inputting:
    ##prompts
    #for convergence criterion
    temp = raw_input('Please enter a convergence criterion: \t')
    try:
        convcrit = float(temp)
    except ValueError:
        print "\nError: convergence criterion is not a number"
        break
    temp = []
    #for looping limit
    temp = raw_input('Please enter an iteration limit: \t')
    try:
        iterlimit = int(temp)
    except ValueError:
        print "\nError: iteration limit is not a number"
        break
    temp = []
    #for verbosity, because I'm tired of all the printout
    temp = raw_input('Would you like verbose output [y/N]? \t')
    ylist = ['y', 'Y', 'yes', 'Yes', 'YES']
    if temp in ylist:
        verbose = True
    else:
        verbose = False
    break

print '\nSimulating. Please wait...'

while simulating:
    try:
        verbose == False
    except NameError:
        print '\nSimulation failed due to invalid parameters!'
        break
    x = rand.random()
    y = rand.random()
    xs.append(x)
    ys.append(y)
    if x**2 + y**2 <= 1.0:
        n += 1
    d += 1
    ratio = 4 * n * 1./d
    if verbose == True:
        print ratio
    ratios.append(ratio)
    if abs(ratio-pi) / pi <= convcrit:
        print "\n \t Convergence Successful!"
        print "\t Draws needed: ", d
        break
    if d == iterlimit:
        print "\n \t Convergence criterion unattainable in", d, "iterations."
        print "\t (try increasing the iteration limit or decreasing the convergence criterion)"
        break
