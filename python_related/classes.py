class Car:
    def __init__(self,brand,model,color,price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
mycar = Car('BMD','series 4','yellow',450000)
yourcar = Car('volvo','XXX','pink',650000)

print(mycar.color)
print(yourcar.model)