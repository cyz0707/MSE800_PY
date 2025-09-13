class Circle:
    def draw(self):
        return "Drawing a Circle"

class Square:
    def draw(self):
        return "Drawing a Square"

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        if shape_type == "square":
            return Square()
        else:
            return None


factory = ShapeFactory()
shape = factory.create_shape("triangle") 

if shape:
    print(shape.draw())
else:
    print("Invalid shape type")

# It wiill raise an AttributeError since shape is None
# because "triangle" is not a valid shape type in the factory.
# To fix this, we should check if shape is not None before calling draw()
# It will alse cause code duplication if we create multiple shapes without validation.
# A better approach is to validate the shape type before creating the shape object.