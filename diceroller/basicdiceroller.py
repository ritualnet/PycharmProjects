import random


class die:
    """Class for die objects.
        attributes:
            sides (int) : Number of sides the dice has (default is 6)

        methods:
            change_sides(new_side) : changes the number of sides
            roll_die() : returns a random integer from 1 to number of sides

    """
    sides = 6

    def change_sides(self, new_side):
        self.sides = new_side

    def roll_die(self):
        return random.randint(1, self.sides)


dice1 = die()
print(dice1.sides)
print(dice1.roll_die())
dice1.change_sides(10)
print(dice1.sides)
print(dice1.roll_die())
