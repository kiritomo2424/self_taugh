#1
import statistics

nums = []

for i in range(0,100):
    nums.append(i)

a = statistics.pvariance(nums)
print(a)

#2
import cubed

x = cubed.cube(3)
print(x)
