# Summera alla de tal mellan 10.000 och 100.000 som är jämnt delbara med 3767
# Räkna antalet siffror i talet

sum = 0
for i in range(10000, 100000):
  if i % 3767 == 0:
    sum += i
print(len(str(sum)))
