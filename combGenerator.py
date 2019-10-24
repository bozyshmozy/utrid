import itertools

s=  input("sheiyvanet sityva: ")

t=list(itertools.permutations(s, len(s)))
text_file = open("output.txt", "w")

for i in range(0, len(t)):
    print (''.join(t[i]))
    text_file.write(''.join(t[i]) + "\n")

print(i)
