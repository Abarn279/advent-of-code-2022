with open('./inp/06.txt') as f:
    signal = f.read()

# Part A
for i in range(len(signal) - 3):
    if len(set(signal[i+x] for x in range(4))) == 4: break
print(i+4)
    
# Part B
for i in range(len(signal) - 13):
    if len(set(signal[i+x] for x in range(14))) == 14: break
print(i+14)