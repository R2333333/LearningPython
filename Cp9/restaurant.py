class Restaurant():
    """docstring for Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        # super(Restaurant, self).__init__()
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name: " + self.restaurant_name)
        print("Cuisine type: " + self.cuisine_type)

    def open(self):
        print('Restaurant is opening')

res = Restaurant('Roy\'s BBQ', 'Earth')
res.describe_restaurant()
res.open()
