#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
import tkinter as tk


class App:

    def __init__(self, root):

        frame = tk.Frame(root)
        frame.pack(side=tk.LEFT)

        self.hi_there = tk.Button(frame, text="say hello", fg="blue",
                                  command=self.say_hi)
        self.hi_there.pack(side=tk.RIGHT)

    def say_hi(self):
        print("Good morning")


root = tk.Tk()
app = App(root)

root.mainloop()
