import turtle


sides = 10
distance = 0.1

colors = ["white", "red", "white"]
count = 0.01

for _ in range(185*sides):
    count += 0.0015
    turtle.color(colors[int(count)])
    distance += 0.1
    turtle.forward(distance)
    turtle.right(360 / sides + 1)
