class Room:  # вариант 16, у меня комната
    def __init__(self, leng=2, wid=2, high=2):
        self.__length = leng  # устанавливаем длину
        self.__width = wid  # устанавливаем ширину
        self.__height = high  # устанавливаем высоту

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @length.setter
    def length(self, length):
        if length in range(2, 100):
            self.__length = length
        else:
            print("Недопустимая длина")

    @width.setter
    def width(self, width):
        if width in range(2, 100):
            self.__length = width
        else:
            print("Недопустимая ширина")

    @height.setter
    def height(self, height):
        if height in range(2, 1000):
            self.__length = height
        else:
            print("Недопустимая высота")

    def __del__(self):
        pass
     #   print("комната {}x{}x{} удалена из памяти".format(self.__length, self.__width, self.__height))

    def display_info(self):
        print(self.__str__())

    def total_square(self):
        return (self.__length + self.__width) * 2 * self.__height

    def real_square(self):
        return (self.__length + self.__width) * 2 * self.__height - 4.6

    def floor(self):
        return self.__length*self.__width

    def __str__(self):
        return "Длина: {} \t Ширина: {}\t Высота: {}".format(self.__length, self.__width, self.__height)

    def str_to_file(self):
        return "room {} {} {}".format(self.__length, self.__width, self.__height)
