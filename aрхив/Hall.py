from Room import Room


class Hall(Room):
    def __init__(self, leng=2, wid=2, high=2, seat=3):
        Room.__init__(self, leng, wid, high)
        self.__seat = seat  # Количество посадочных мест

    @property
    def seat(self):
        return self.__seat

    @seat.setter
    def seat(self, seat):
        if seat in range(0, 20):
            self.__seat = seat
        else:
            print("Недопустимое количество посадочных мест")

    def display_info(self):
        print("Гостиная ")
        print(self)
        print("количество посадочных мест: ", self.__seat, "\n")

    def str_to_file(self):
        return "hall {} {} {} {}".format(self.length, self.width, self.height, self.seat)
