import turtle


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Rectangle:

	def __init__(self, point1, point2):
		self.point1 = point1
		self.point2 = point2


class GuiRectangle(Rectangle):

	def draw_rectangle(self):
		turtle.screensize(canvwidth=300, canvheight=300)
		turtle.penup()
		turtle.goto(self.point1.x, self.point1.y)
		turtle.pendown()
		turtle.goto(self.point2.x, self.point1.y)
		turtle.goto(self.point2.x, self.point2.y)
		turtle.goto(self.point1.x, self.point2.y)
		turtle.goto(self.point1.x, self.point1.y)
		turtle.done()


point1 = Point(0, 0)
point2 = Point(200, 120)
rectangle = Rectangle(point1, point2)
GuiRectangle = GuiRectangle(point1, point2)
GuiRectangle.draw_rectangle()
