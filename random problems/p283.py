# if we throw a dice n time what is the average outcome

from random import randint , seed
from statistics import mean


print(mean([randint(1,6) for i in range (10**5)]))
