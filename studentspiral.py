import turtle

sides = 2
distance = 100

for _ in range(100*sides):
  turtle.color('white')
  distance += 3
  turtle.forward(distance)
  turtle.right(360/sides+1)
  
for _ in range(100*sides):
  turtle.color('Black')
  distance += 3
  turtle.forward(distance)
  turtle.right(360/sides+1)
  
for _ in range(50*sides):
  turtle.color('white')
  distance += 3
  turtle.forward(distance)
  turtle.right(360/sides+1)
  
for _ in range(25*sides):
  turtle.color('Black')
  distance += 3
  turtle.forward(distance)
  turtle.right(360/sides+1)
