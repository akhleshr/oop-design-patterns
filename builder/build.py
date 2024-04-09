from car_builder import CarBuilder

if __name__ == "__main__":
    car_builder = CarBuilder()
    car = (car_builder.set_make("Toyota")
                     .set_model("Camry")
                     .set_year(2020)
                     .set_color("Red")
                     .build())
    print(car)

# Output: Car: Toyota Camry, 2020, Red