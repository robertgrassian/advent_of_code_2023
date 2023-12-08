import re
import math

# naive approach, do same thing, lets see if we need to optimize

# if I think it out, it could be solved by figuring out the min time it could be held to reach distance
# too much work though

file = open('6.txt', 'r')
lines = file.readlines()

t = int(re.sub(r" +", "",lines[0].split(":")[1].strip()))
d = int(re.sub(r" +", "",lines[1].split(":")[1].strip()))


# determined by solving:
# given time t and distance d, what values of s exist s.t. (t-s)*s > d ?
# this can be solved for s and yields a range which is the answer

a = (t + math.sqrt(t**2 - 4*d)) / 2
b = (t - math.sqrt(t**2 - 4*d)) / 2


print(int(math.ceil(max(a,b)-min(a,b))))
