import turtle
turtle.bgcolor("green")
t = turtle.Turtle()
t.color("red", "blue")
t.begin_fill()
for i in range(0, 5):
    t.forward(200)
    t.right(144)
t.end_fill()

# def draw_regular_polygon(surface, color, vertex_count, radius, position):
#     n, r = vertex_count, radius
#     x, y = position
#     pygame.draw.polygon(surface, color, [
#         (x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n))
#         for i in range(n)
#     ])
    

#Pentagram Challenge - www.101computing.net/pentagram-challenge/
# import turtle, math
# myPen = turtle.Turtle()
# myPen.shape("arrow")
# myPen.pencolor("purple")
# myPen.pensize(2)
# myPen.speed(1000)

# #A Procedure to draw a polygon from a list of vertices.
# def drawPolygon(polygon):
#  myPen.penup()
#  myPen.goto(polygon[0][0],polygon[0][1])
#  myPen.pendown()
 
#  for i in range(1,len(polygon)):
#     myPen.goto(polygon[i][0],polygon[i][1])
 
#  myPen.goto(polygon[0][0],polygon[0][1])
 
 
# #A polygon can be stored as a list of vertices 
# pentagon=[]
# R = 150
# for n in range(0,5):
#   x = R*math.cos(math.radians(90+n*72))
#   y = R*math.sin(math.radians(90+n*72))
#   pentagon.append([x,y])

# drawPolygon(pentagon)
# myPen.hideturtle()