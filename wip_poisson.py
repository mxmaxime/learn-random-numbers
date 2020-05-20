import numpy as np
import scipy
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from laws.exponential_law import generate_exponential_law

N = 1000

"""# Loi de Poisson
Référence p83 du cours, 3.2 Loi de Poisson.
"""

# def poisson(lamb, k):
#     return (lamb**k) * np.exp(-lamb) / math.factorial(k)

# prob = poisson(10, 7)
# print(' There is a %2.2f %% chance that exactly 7 customers show up at the lunch rush' %(100*prob))

# Génération de ma variable aléatoire qui suit une loi explonentielle
U = np.random.uniform(size=N)

lamb = 1/5
U_expo = generate_exponential_law(lamb, U)

def poisson_generation(exponential_values):
    # begin à t = 0
    event_time = 0

    event_times = []
    event_num = []

    for i, exponential_value in enumerate(exponential_values):
        event_num.append(i)
        event_time += exponential_value
        event_times.append(event_time)
    
    return event_time, event_times, event_num

fig = plt.figure()
fig.suptitle('Times between consecutive events in a simulated Poisson process')
plot, = plt.plot(event_num, U_expo, 'bo-', label='Inter-event time')
plt.legend(handles=[plot])
plt.xlabel('Index of event')
plt.ylabel('Time')
plt.show()

def zz(event_times):
    interval_nums = []
    num_events_in_interval = []

    interval_num = 1

    num_events = 0

    for i, event_time in enumerate(event_times):
        if event_time <= interval_num:
            num_events += 1
        else:
            interval_nums.append(interval_num)
            num_events_in_interval.append(num_events)
            interval_num += 1
            num_events += 1
    
    return interval_nums, num_events_in_interval

interval_nums, num_events_in_interval = zz(event_times)

fig = plt.figure()
plt.bar(interval_nums, num_events_in_interval)
plt.xlabel('Index of interval')
plt.ylabel('Number of events')
plt.show()