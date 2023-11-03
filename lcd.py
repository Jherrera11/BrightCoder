class NumberDrawing:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def draw_top(self):
        pass

    def draw_middle(self):
        pass

    def draw_bottom(self):
        pass

class One(NumberDrawing):
    def draw_top(self):
        print("")

    def draw_bottom(self):
        for i in range(self.height):
            print(" " * self.width, end="")
            print("|")

class Two(NumberDrawing):
    def draw_top(self):
        for i in range(self.width):
            print("_", end="")
        print("")

    def draw_middle(self):
        for i in range(self.height):
            print(" " * self.width, end="")
            print("|")
        for i in range(self.width):
            print("—", end="")
        print(" ")

    def draw_bottom(self):
        for i in range(self.height):
            print("|  ")
        for i in range(self.width):
            print("—", end="")

class Three(NumberDrawing):
    def draw_top(self):
        for i in range(self.width):
            print("_", end="")
        print("")

    def draw_middle(self):
        for i in range(self.height):
            print(" " * self.width, end="")
            print("|")
        for i in range(self.width):
            print("—", end="")
        print("")

    def draw_bottom(self):
        for i in range(self.height):
            print(" " * self.width, end="")
            print("|")
        for i in range(self.width):
            print("—", end="")

class Four(NumberDrawing):
    def draw_top(self):
        print("")

    def draw_middle(self):
        for i in range(self.height):
            print("|", end="")
            print(" " * (self.width - 1), end="")
            print("|  \n", end="")
        for i in range(self.width):
            print("—", end="")

    def draw_bottom(self):
        print("")
        for i in range(self.height):
            print(" " * (self.width - 2), end="")
            print("  |")


class Five(NumberDrawing):
    def draw_top(self):
        for i in range(self.width):
            print("_", end="")
        print("")

    def draw_middle(self):
        for i in range(self.height):
            print("|")
        for i in range(self.width):
            print("—", end="")
        print("")

    def draw_bottom(self):
        for i in range(self.height):
            print(" " * (self.width - 1), end="")
            print("|")
        for i in range(self.width):
            print("—", end="")


class Six(NumberDrawing):
    def draw_top(self):
        for i in range(self.width):
            print("_", end="")
        print("")

    def draw_middle(self):
        for i in range(self.height):
            print("|")
        for i in range(self.width):
            print("—", end="")
        print("")

    def draw_bottom(self):
        for i in range(self.height):
            print("|", end="")
            print(" " * (self.width - 1), end="")
            print("|  \n", end="")
        print("—" * self.width, end="")


class Seven(NumberDrawing):
    def draw_top(self):
        for i in range(self.width):
            print("_", end="")
        print("")

    def draw_bottom(self):
        for i in range(self.height):
            print(" " * self.width, end="")
            print("|")

        for i in range(self.height):
            print(" " * self.width, end="")
            print("|")


class Eight(NumberDrawing):
    def draw_top(self):
        for i in range(self.width):
            print("_", end="")
        print("")

    def draw_middle(self):
        for i in range(self.height):
            print("|", end="")
            print(" " * (self.width - 1), end="")
            print("|  \n", end="")
        print("—" * self.width)

    def draw_bottom(self):
        for i in range(self.height):
            print("|", end="")
            print(" " * (self.width - 1), end="")
            print("|  \n", end="")
        print("—" * self.width)

class Nine(NumberDrawing):
    def draw_top(self):
        for i in range(self.width):
            print("_", end="")
        print("")

    def draw_middle(self):
        for i in range(self.height):
            print("|", end="")
            print(" " * (self.width - 1), end="")
            print("|  \n", end="")
        print("—" * self.width)

    def draw_bottom(self):
        for i in range(self.height):
            print(" " * self.width, end="")
            print("|")
        for i in range(self.width):
            print("_", end="")

def main():
    number = int(input("Give a number from 1 to 9: "))
    height = int(input("Give the height: "))
    width = int(input("Give a width: "))

    if 1 <= number <= 9:
        number_instance = None

        if number == 1:
            number_instance = One(height, width)
        elif number == 2:
            number_instance = Two(height, width)
        elif number == 3:
            number_instance = Three(height, width)
        elif number == 4:
            number_instance = Four(height, width)
        elif number == 5:
            number_instance = Five(height, width)
        elif number == 6:
            number_instance = Six(height, width)
        elif number == 7:
            number_instance = Seven(height, width)
        elif number == 8:
            number_instance = Eight(height, width)
        elif number == 9:
            number_instance = Nine(height, width)

        number_instance.draw_top()
        number_instance.draw_middle()
        number_instance.draw_bottom()

    else:
        print("ERROR: Only numbers 1 to 9 are allowed.")

if __name__ == "__main__":
    main()
