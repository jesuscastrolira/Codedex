#Codedex - Excercise 8 - Quadratic Square

a = int(input('Enter a value: '))
b = int(input('Enter b value: '))
c = int(input('Enter c value: '))

d = (b**2) - (4*a*c)

root1 = (-b + d ** 0.5) / (2 * a)

root2 = (-b - d **0.5) / (2 * a)

print('Result of Root1: ', root1)
print('Result of Root2: ', root2)