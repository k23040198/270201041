import math

class cylinder:

  def __init__(self,height,radius):
    self.height=height
    self.radius=radius

  def getter_height(self):
    return self.height

  def getter_radius(self):
    return self.radius

  def set_height(self,height):
    self.height=height

  def set_radius(self,radius):
    self.radius=radius

  def calculate_base_area(self):
    return (self.radius**2)*math.pi

  def calculate_surface_area(self):
    return 2*math.pi*self.radius*self.height

  def area(self):
    surface_area= self.calculate_surface_area()
    base_area= self.calculate_base_area()
    area= base_area * 2 + surface_area
    return area

  def volume(self):
    return self.calculate_base_area()*self.height


cylinder1= cylinder(4,2)
print(cylinder1.area())

print(cylinder1.volume())
