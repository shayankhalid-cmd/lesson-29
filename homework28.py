class bmw():
    def fuel_type(self):
        print("BMW cars use petrol as fuel")
    def max_speed(self):
        print("BMW cars can reach a maximum speed of 190 mp/h")
class ferrari():
    def fuel_type(self):
        print("Ferrari cars use petrol as fuel")
    def max_speed(self):
        print("Ferrari cars can reach a maximum speed of 290 mp/h")
for car in (bmw(), ferrari()):
    car.fuel_type()
    car.max_speed()