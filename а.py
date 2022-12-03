from itertools import islice

f1 = open('Test.txt')
f2 = open('Output.txt', 'a')

bunch = 500
lines = list(islice(f1, bunch))
f2.writelines(lines)

f1.close()
f2.close()