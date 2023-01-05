import turtle


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Rectangle:

	def __init__(self, orgin, dimensions):
		self.orgin = orgin
		self.demensions = dimensions


class GuiRectangle(Rectangle):

	def draw_rectangle(self):
		turtle.Screen().bgcolor('black')
		turtle.screensize(canvwidth=300, canvheight=300)
		turtle.pencolor('green')
		turtle.penup()
		turtle.goto(self.orgin.x, self.orgin.y)
		turtle.pendown()
		turtle.forward(self.demensions.x-130)
		turtle.right(90)
		turtle.forward(20)
		turtle.left(90)
		turtle.forward(10)
		turtle.left(90)
		turtle.forward(20)
		turtle.right(90)
		turtle.forward(self.demensions.x-80)
		turtle.right(90)
		turtle.forward(self.demensions.y)
		turtle.right(90)
		turtle.forward(self.demensions.x-80)
		turtle.right(90)
		turtle.forward(20)
		turtle.left(90)
		turtle.forward(10)
		turtle.left(90)
		turtle.forward(20)
		turtle.right(90)
		turtle.forward(self.demensions.x-130)
		turtle.right(90)
		turtle.forward(self.demensions.y)
		turtle.done()


orgin = Point(-100, 60)
dimensions = Point(200, 120)
rectangle = Rectangle(orgin, dimensions)
GuiRectangle = GuiRectangle(orgin, dimensions)
GuiRectangle.draw_rectangle()
