#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import random, argparse, tkinter as tk

class Dice():

    def __init__(self, sides = 6, zero = False):
        self._sides = self.check_sides(sides)
        self._include_zero = zero
        self._result = 0

    def roll(self, throws = 1):
        self._result = []
        try:
            for t in range(0, throws):
                self._result.append(random.randint(0 if self._include_zero else 1, self._sides))
        except :
            raise Exception("Error to perform dice rolling")
        return tuple(self._result)

    def check_sides(self, sides):
        return sides if sides >= 2 else None

class DiceGUI():
    def __init__(self):
        self.root = tk.Tk() #main window and other widgets
        self.root.title('Dices')
        self.root.minsize(360, 240)
        self.root.resizable(True, True)

        # Input
        self.frame_input = tk.Frame(self.root, height = 5)

        ## Sides input
        self.label_sides = tk.Label(self.frame_input, text='Number of sides: ', height=2, width=16 )
        self.spinbox_sides = tk.Spinbox(self.frame_input, from_=2, to=1000, width=5, textvariable=tk.StringVar(value="6"))
        self.label_sides.grid(row=0, column=0, sticky=tk.E+tk.W )
        self.spinbox_sides.grid(row=0, column=1, sticky=tk.W)

        ## Throw input
        self.label_throws = tk.Label(self.frame_input,
                                     text='Number of throws: ',
                                     height=2)
        self.spinbox_throws = tk.Spinbox(self.frame_input,
                                         from_=1,
                                         to=100,
                                         width=5)
        self.label_throws.grid(row=2, column=0, sticky=tk.E+tk.W)
        self.spinbox_throws.grid(row=2, column=1, sticky=tk.W)

        self.frame_input.pack(side="top", fill="y", expand=False)

        # Roll button command
        self.button = tk.Button(cursor='hand2',
            activebackground='green',
            font='bold 16',text="Roll", width=10, height=2,
            command=self.roll)
        self.button.pack(fill="x", expand=False, padx=10)

        # Dice output
        self.string_result = tk.StringVar(value="Results")
        self.label_result = tk.Label(textvariable=self.string_result, font='bold 12')
        self.label_result.pack(fill="both", expand=False)

        self.frame_output = tk.Frame(self.root)
        self.string_dice_output = tk.StringVar()
        self.label_dice_output = tk.Message(self.frame_output, justify="left",textvariable=self.string_dice_output, font='8')
        self.label_dice_output.grid(row=1, sticky=tk.E+tk.W)

        self.frame_output.pack(side="bottom", fill="none",  expand=True)

        self.root.mainloop()

    def roll(self):
        resuls = None
        try:
            d = Dice(sides=int(self.spinbox_sides.get()))
            resuls = d.roll(int(self.spinbox_throws.get()))
        except :
            print("Error to perform dice rolling")
            tk.messagebox.showerror("Error", "Error to perform dice rolling\nCheck sides and throw.")
            return

        digit_len = len(str(abs(max(resuls))))
        self.string_dice_output.set(" - ".join([ '{nb:0>{max_len}}'.format(nb=dd, max_len=digit_len) for dd in resuls ]))

def diceInteractive():
    raw_side = input("Enter the number of sides of the dice (6): ") or "6"
    try:
        d = Dice(int(raw_side))
        raw_throw = input("Enter the number dice throws (1): ") or "1"
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
                        help='Number the dice rolls (default: 1)')
    parser.add_argument("-s", "--sides", default=6, type=int,
                        help='Number of sides of the dice (default: 6)')

    args = parser.parse_args()

    if args.interactive:
        diceInteractive()
    elif args.gui:
        DiceGUI()
    else:
        diceCLI(args.sides, args.throws )

