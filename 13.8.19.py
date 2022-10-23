ticket = int(input('How much tickets do you need '))

age = [int(input('How old are you ')) for i in range(ticket)]
sum = 0
for i in range(len(age)):
    if age [i] <= 18:
        sum += 0        
    elif 18 <= age [i] <= 25:
        sum += 990       
    else:
        sum += 1390
print(sum)
if ticket >= 3:
    sum = sum * 0.9
    print(sum)
        
