#10 sec timer
import time
print("10 second timer", end="")
time.sleep(10)
print("\rTime-Up")
#we can use range also
'''
print("Timer started", end="")

for i in range(11):
  print("\r", i, end="")
  time.sleep(1)

print("\rTimer finished")
'''
