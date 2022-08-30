from Room import Room


class Kitchen(Room):
    def __init__(self, leng=2, wid=2, high=2, tech_amount=0):
        Room.__init__(self, leng, wid, high)
        self.__tech_amount = tech_amount  # Количество техники в кухне

    @property
    def tech_amount(self):
        return self.__tech_amount

    @tech_amount.setter
    def tech_amount(self, tech_amount):
        if tech_amount in range(0, 10):
            self.__tech_amount = tech_amount
        else:
            print("Недопустимое количество техники")

    def __str__(self):
        temp_string = "Кухня\nДлина: {} \t Ширина: {}\t Высота: {}\t \nКоличество техники: {}\n".format(self.length,
                                                                                                        self.width,
                                                                                                        self.height,
                                                                                                        self.tech_amount)
        return temp_string

    def str_to_file(self):
        return "kitchen {} {} {} {}".format(self.length, self.width, self.height, self.tech_amount)
