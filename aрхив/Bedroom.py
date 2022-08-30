from Room import Room


class Bedroom(Room):
    def __init__(self, leng=2, wid=2, high=2, people=1):
        Room.__init__(self, leng, wid, high)
        self.__people_amount = people  # Количество людей, которые могут разместиться в спальне

    @property
    def people_amount(self):
        return self.__people_amount

    @people_amount.setter
    def people_amount(self, people_amount):
        if people_amount in range(0, 10):
            self.__people_amount = people_amount
        else:
            print("Недопустимое количество людей")

    def display_info(self):
        print("Спальня ")
        Room.display_info(self)
        print("Количество людей: ", self.people_amount, "\n")

    def str_to_file(self):
        return "bedroom {} {} {} {}".format(self.length, self.width, self.height, self.people_amount)
