# Approximates burn rate coefficients for a BATES propellant grain, Using method provided by https://www.nakka-rocketry.net/ptburn.html
# By Chet for Ruggggggggers Rocket Propulsion Lab (I do not know how to code at all)
import sys
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Order of config inputs:
#  - Number of propellant segments (N)
#  - Segment outside diameter (D, mm)
#  - Throat area (Ato, mm^2)
#  - Density (g/cm^3)
#  - Initial web thickness (wo, mm)
#  - Inner diameter (do, mm)
#  - Segment initial length (Lo, mm)
#  - Characteristic velocity (c*, m/s)
#  - Initial burn distance guess (s, mm)

if len(sys.argv) != 5:
    print("Usage: python burnRateCalc.py timesFile.txt pressuresFile.txt config.txt output.txt")
    sys.exit(1)

timesFile = sys.argv[1]
pressureFile = sys.argv[2]
configFile = sys.argv[3]
outputFile = sys.argv[4]

pres = np.loadtxt(pressureFile)
times = np.loadtxt(timesFile)

initialS = 0
at = 0
po = 0
dt = 0
ab = 0
alph = 0
d = 0
do = 0
lo = 0
n = 0
rho = 0
wo = 0
charVel = 0
a_opt = 0
n_opt = 0

data = np.loadtxt(configFile, unpack=True)
n, d, at, rho, wo, do, lo, charVel, initialS = data

length = len(pres)
dt = np.zeros(length)
instBurn = np.zeros(length)
instBurnRate = np.zeros(length)
burnTotal = np.zeros(length)
burnAreas = np.zeros(length)

def burn_rate_model(P, a, n):
  return a * np.power(P, n)

def LHS(at, po, st, dt, ab, alph):
  return st - (at * po * dt) / (ab * alph)

def burnArea(d, do, lo, s, n):
  s1 = (d**2 - ((do + (2 * s))**2))
  s2 = (lo - (2 * s)) * (do + 2 * s)
  return np.pi * n * (0.5 * s1 + s2)

def dtArray():
  dt[0] = times[1] - times[0]
  for i in range(1, length):
    dt[i] = times[i] - times[i - 1]

def alpha():
  return rho * charVel

alph = alpha()

dtArray()
burnTotal[0] = initialS
burnAreas[0] = burnArea(d, do, lo, burnTotal[0], n)
print(burnAreas[0])
lhs1 = LHS(at, pres[0], instBurn[0], dt[0], burnAreas[0], alph)
instBurn[0] = (-1 * lhs1)
instBurnRate[0] = instBurn[0] / dt[0]

for i in range(1, length):
  burnTotal[i] = burnTotal[i - 1] + instBurn[i - 1]
  burnAreas[i] = burnArea(d, do, lo, burnTotal[i], n) # check the math here
  lhsVal = LHS(at, pres[i], instBurn[i], dt[i], burnAreas[i], alph)
  instBurn[i] = -1 * lhsVal
  instBurnRate[i] = instBurn[i] / dt[i]

mpaPress = pres / 1000000

popt, pcov = curve_fit(burn_rate_model, mpaPress, instBurnRate)

a_opt, n_opt = popt

sumBurn = burnTotal[-1]

outStr1 = "With function aP^n, a approximated to be " + str(a_opt) + " and n_opt approximated to be " + str(n_opt) 
outStr2 = "Your provided web thickness was " + str(wo) + ". Total burn distance calculated as " + str(sumBurn)

strings_array = np.array([outStr1, outStr2])
print(strings_array)
np.savetxt(outputFile, strings_array, fmt='%s')