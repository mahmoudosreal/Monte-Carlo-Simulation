import numpy as np

s = 100 ## spot price
t = 1 ## Time trading
r = 0.07 ## Discount rate
sigma = 0.2 ## volatility
nSimulations = 5000 ## Number of simulation 5000
nSteps = 250 ## Daily Movement 250
K = 100 ## Strike Price 

dt = t / nSteps

drift = (r - ((sigma**2)/2))*dt
a =  sigma * np.sqrt(dt)
x = np.random.normal(0, 1, (nSimulations, nSteps))

sMat = np.zeros((nSimulations, nSteps))
sMat[:, 0] += s
for i in range (1, nSteps):
  sMat[:, i] += sMat[:, i-1] * np.exp(drift + (a * x[:, i]))

q = sMat[:,-1] - K
for i in range(len(q)):
  if q[i] < 0:
    q[i] = 0
  else:
    q[i] = q[i]

p = K - sMat[:,-1]
for i in range(len(p)):
  if p[i] < 0:
    p[i] = 0
  else:
    p[i] = p[i]

payOffCall = np.mean(q)
payOffPut = np.mean(p)

call = payOffCall*np.exp(-r * t)
put = payOffPut*np.exp(-r * t)

please make a markdown for github 
