class Rectangle:
    def __init__(self, w = 1, h = 1):
        self.width = w
        self.height = h
    
    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        self.area = self.width * self.height
        return self.area
    
    def get_perimeter(self):
        self.perimeter = 2 * (self.width + self.height)
        return self.perimeter
    
    def get_diagonal(self):
        self.diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return self.diagonal
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            s = ""
            for i in range(self.height):
                s += "*" * self.width + "\n"
            return s
    
    def get_amount_inside(self, rectangle):
        amount_inside = int(self.get_area() / rectangle.get_area())
        return amount_inside
    
    def __str__(self):
        s = f"Rectangle(width={self.width}, height={self.height})"
        return s

class Square(Rectangle):
    def __init__(self, s=1):
        self.width = s
        self.height = s

    def set_width(self, s):
        self.width = s
        self.height = s

    def set_height(self, s):
        self.width = s
        self.height = s

    def set_side(self, s):
        self.width = s
        self.height = s
    def __str__(self):
        s = f"Square(side={self.width})"
        return s