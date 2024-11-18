# average of tossing a coin n time
from random import randint ,seed
from statistics import mean


print(mean([randint(0,1) for _ in range(10**5)]))
