people = [input() for _ in range(5)]
line = [''] * 5

for i in range(len(people[0])) :
    people_state = people[0][i] + people[1][i] + people[2][i] + people[3][i] + people[4][i]
    
    if people_state == '.omln' :
        line[0] += 'o'
        line[1] += 'w'
        line[2] += 'l'
        line[3] += 'n'
        line[4] += '.'
        
    elif people_state == 'owln.' :
        line[0] += '.'
        line[1] += 'o'
        line[2] += 'm'
        line[3] += 'l'
        line[4] += 'n'
        
    else :
        line[0] += '.'
        line[1] += '.'
        line[2] += 'o'
        line[3] += 'L'
        line[4] += 'n'
        
for i in line :
    print(i)