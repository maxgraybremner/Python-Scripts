## scores01.py ##

path = './scores.txt'
teams = {}
f = open(path, 'r')
for line in f:
    
    if "Round" in line:
        continue
    
    words = line.split()
    
    s1 = 0
    s2 = 0
    
    for i in range(len(words)):
        if s1 ==  0 and words[i].isdigit():
            s1 = i
        elif s1 != 0 and words[i].isdigit():
            s2 = i
    
    t1 = []
    t2 = []
    
    for i in range(len(words)):

        if i < s1:
            t1.append(words[i])
        elif i > s2:
            t2.append(words[i])
        
    s1 = int(words[s1])
    s2 = int(words[s2])

    t1 = ' '.join(t1)
    t2 = ' '.join(t2)

    if t1 not in teams:
        teams[t1] = s1
        teams[t2] = s2
    elif t1 in teams:
        teams[t1] += s1
        teams[t2] += s2

x = [(teams.get(a), a) for a in teams]

x.sort(reverse=True)

for a, b in x:
    print('{1:<24}  {0:>4}'.format(a, b))
