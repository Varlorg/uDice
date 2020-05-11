#!/usr/bin/env python3

import random, argparse, tkinter as tk


class Dice():

    def __init__(self, sides = 6, zero = False):
        self._sides = self.check_sides(sides)
        self._include_zero = zero
        self._result = 0

    def roll(self, throws = 1):
        self._result = []
        for t in range(0, throws):
            self._result.append(random.randint(0 if self._include_zero else 1, self._sides))
        return tuple(self._result)

    def check_sides(self, sides):
        return sides if sides >= 2 else None


# Interface : nb de face, include zero, nombre de lancé
class DiceGUI():
    def __init__(self):
        self.root = tk.Tk() #main window and other widgets
        self.root.title('Dices')
        self.root.resizable(False, False)

        # Input
        self.label_minutes = tk.Label(text='Time for Backup (Minutes): ', height=2)
        self.spinbox_minutes = tk.Spinbox(from_=1, to=100, width=5)
        self.label_minutes.grid(row=0, column=1, sticky=tk.W)

        # Roll button command
        self.button = tk.Button(cursor='hand2', activebackground='green',
            font='bold 16',text="Roll", command=self.roll)
        self.button.grid(row=1, padx=20, pady=10)

        # Dice output
        self.label_res = tk.StringVar(value="Results")
        self.label = tk.Label( textvariable=self.label_res)
        self.label.grid(row=1, sticky=tk.E)

        self.label_dice_output = tk.StringVar()
        self.label = tk.Label( textvariable=self.label_dice_output)
        self.label.grid(row=1, column=1, sticky=tk.W)

        self.root.mainloop()

    def roll(self):
        d = Dice()
        self.label_dice_output.set(d.roll())

def diceInteractive():
    raw_side = input("Enter the number of sides of the dice : ")
    try:
        d = Dice(int(raw_side))
        raw_throw = input("Enter the number dice throws : ")
        print("Results : ", d.roll(int(raw_throw)))
    except:
        print("Error to perform dice rolling")

def diceCLI(sides=6, throws=1):
    print("Results : ", Dice(int(sides)).roll(int(throws)))

if __name__== '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--gui", required=False, action="store_true",
                    help='Launch GUI interface')
    parser.add_argument("-i", "--interactive", action="store_true",
                    help='Launch CLI interface')
    parser.add_argument("-t", "--throws", default=1, type=int,
                    help='Number the dice rolls')
    parser.add_argument("-s", "--sides", default=6, type=int,
                    help='Number of sides of the dice')

    args = parser.parse_args()
    print(args)

    # Possibility to launch with arg number of dice and numbre of throw ?
    if args.interactive:
        diceInteractive()
    elif args.gui:
        DiceGUI()
    else:
        diceCLI(args.sides, args.throws )



