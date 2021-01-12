# Family Name: JuanPablo Sanchez
# Student Number: 
# Course: ITI 1120
# Assignment Number 6
# Due 7 Dec, 2020

class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle:
    '''Class that represents a rectangle'''

    def __init__(self, Point_bot, Point_top, colour):
        '''(Rectangle, object, object, str) -> None
        Initializes point coordinates to (Point_bot, Point_top, colour)
        '''
        self.bottom = Point_bot
        self.top = Point_top
        self.colour = colour

    def get_bottom_left(self):
        '''(Rectangle) -> int
        Gets the bottom left value of the rectangle
        '''
        
        return self.bottom

    def get_top_right(self):
        '''(Rectangle) -> int
        Gets the top right value of the rectangle
        '''
        return self.top

    def get_colour(self):
        '''(Rectangle) -> str
        Gets the colour of the rectangle
        '''
        
        return str(self.colour)

    def reset_colour(self, new_colour):
        '''(Rectangle, str)->None
        Resets the colour of the rectangle to the given colour
        '''
        
        self.colour = new_colour

    def get_perimeter(self):
        '''(Rectange) -> int
        Finds the perimeter of the rectangle
        '''
        
        length = (self.top.x)-(self.bottom.x)
        width = (self.top.y)-(self.bottom.y)
        perimeter = 2*(length + width)

        return perimeter

    def get_area(self):
        '''(Rectangle)-> int
        Finds the area of the rectangle
        '''
        
        length = (self.top.x)-(self.bottom.x)
        width = (self.top.y)-(self.bottom.y)
        area = length*width
        
        return area

    def move(self, xcord = 0, ycord = 0):
        '''(Rectangle, int, int)->None
        Given numbers dx and dy, it moves the rectangle accordingly
        '''
        
        Point.move(self.bottom, xcord, ycord)
        Point.move(self.top, xcord, ycord)

    def intersects(self, other):
        '''(Rectangle, Rectangle) -> bool
        Finds if two rectangles intersect one another at any point
        '''
        
        if self.top.x < other.bottom.x or self.bottom.x > other.top.x:
            return False

        if self.top.y < other.bottom.y or self.bottom.y > other.top.y:
            return False
        
        return True

    def contains(self, xbound, ybound):
        '''(Rectange, int, int) -> bool
        Finds to see if given point is located inside of the rectangle 
        '''

        if (xbound >= self.bottom.x and xbound <= self.top.x) and (ybound >= self.bottom.y and ybound <= self.top.y):
            return True

        return False

    def __eq__(self,other):
        '''(Rectangle, Rectangle)->bool
        Returns True if the all values of the rectangle are the same
        '''

        return self.bottom == other.bottom and self.top == other.top and self.colour == other.colour
        
    def __repr__(self):
        '''(Rectangle)->str
        Returns a nice looking version of all the values of the rectangle
        '''
        
        return 'Rectangle('+str(self.bottom)+','+str(self.top)+ ',' +"'"+str(self.colour)+"'"+ ")"

    def __str__(self):
        '''(Rectangle)->str
        A nice representation of what all of the values of the rectangle are
        '''
        
        return "I am a " + str(self.colour) + " rectangle with bottom left corner at ("+str(self.bottom.x) +',' + str(self.bottom.y) + ") and top right corner at (" + str(self.top.x) + ',' + str(self.top.y) + ').'

class Canvas:

    def __init__(self):
        '''(Canvas)-> None
        Initializes a list as a canvas is a collection of rectangles
        '''

        self.collection = []

    def __len__(self):
        '''(Canvas)->int
        Finds the number of rectangles inside the canvas
        '''
        
        return len(self.collection)

    def __repr__(self):
        '''(Canvas)->str
        Returns a nice looking version of all of the rectangles in the canvas
        '''
        
        return 'Canvas(' + str(self.collection) + ')'

    def add_one_rectangle(self, rectangle):
        '''(Canvas, Rectangle)-> None
        Adds a rectangle to the canvas
        '''
        
        self.collection.append(rectangle)

    def count_same_colour(self, colour):
        '''(Canvas, str)-> int
        Counts the number of times a specific colour appears in the canvas
        '''

        counter = 0
        for i in self.collection:
            if colour == i.get_colour():
                counter += 1 

        return counter

    def total_perimeter(self):
        '''(Canvas)->int
        Calculates the total perimeter of the all the rectangles inside the canvas
        '''

        total_perimeter = 0
        for i in self.collection:
            total_perimeter += i.get_perimeter()

        return total_perimeter

    def min_enclosing_rectangle(self):
        '''(Canvas)-> Rectangle
        Returns an object type Rectangle that contains all the rectangles in the Canvas
        '''
        
        min_x_coordinate = 0
        for i in self.collection:
            if min_x_coordinate > i.get_bottom_left().x:
                min_x_coordinate = i.get_bottom_left().x

        max_x_coordinate = 0
        for i in self.collection:
            if max_x_coordinate < i.get_top_right().x:
                max_x_coordinate = i.get_top_right().x

        min_y_coordinate = 0
        for i in self.collection:
            if min_y_coordinate > i.get_bottom_left().y:
                min_y_coordinate = i.get_bottom_left().y

        max_y_coordinate = 0
        for i in self.collection:
            if max_y_coordinate < i.get_top_right().y:
                max_y_coordinate = i.get_top_right().y

        return Rectangle(Point(min_x_coordinate,min_y_coordinate),Point(max_x_coordinate,max_y_coordinate),"red")

    def common_point(self):
        '''(Canvas) -> bool
        Returns True if there exists a point that intersects all rectangles in the canvas
        '''

        original_rectangle = self.collection[0]
        for i in range(1,len(self.collection)):
            if not(original_rectangle.intersects(self.collection[i])):
                return False

        return True
