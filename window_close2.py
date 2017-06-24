# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 15:14:05 2017

@author: Alexander Mitchell
"""

from tkinter import *
from PIL import ImageTk, Image

#----------------------------------------------------------------------

class MainWindow:

    #----------------

    def __init__(self, main):

        # canvas for image
        self.canvas = Canvas(main, width=400, height=500)
        self.canvas.grid(row=0, column=0)

        # images
        self.my_images = img = ImageTk.PhotoImage(file = "test.gif")

        # set first image on canvas
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor = NW, image = self.my_images)

        # button to change image
        self.button = Button(main, text="Change", command=self.onButton)
        self.button.grid(row=1, column=0)


    #----------------

    def page(self, main):

        # canvas for image
        self.canvas = Canvas(main, width=400, height=500)
        self.canvas.grid(row=0, column=0)

        # images
        self.my_images = img = ImageTk.PhotoImage(file = "ball2.gif")

        # set first image on canvas
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor = NW, image = self.my_images)

        # button to change image
        self.button = Button(main, text="ball1", command=self.onButton1 )
        self.button.grid(row=1, column=0)


    def page2(self, main):

        # canvas for image
        self.canvas = Canvas(main, width=400, height=500)
        self.canvas.grid(row=0, column=0)

        # images
        self.my_images = img = ImageTk.PhotoImage(file = "ball1.gif")

        # set first image on canvas
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor = NW, image = self.my_images)

        # button to change image
        self.button = Button(main, text="ball2", command=self.onButton2)
        self.button.grid(row=1, column=0)


    def page3(self, main):

        # canvas for image
        self.canvas = Canvas(main, width=400, height=500)
        self.canvas.grid(row=0, column=0)

        # images
        self.my_images = img = ImageTk.PhotoImage(file = "test.gif")

        # set first image on canvas
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor = NW, image = self.my_images)

        # button to change image
        self.button = Button(main, text="Ferrari", command=self.onButton)
        self.button.grid(row=1, column=0)



    def onButton(self):
        
        self.canvas.destroy()
        self.button.destroy()
        self.page(root)
        # next image
        
    def onButton1(self):
        
        self.canvas.destroy()
        self.button.destroy()
        self.page2(root)
        
    def onButton2(self):
        
        self.canvas.destroy()
        self.button.destroy()
        self.page3(root)
        
        
        
class Page(self,main):
    
    def nextPage(self):
        self.nextPage = nextPage
    
    def file(self):
        self.img_str = img_str
    
    def render(self,main):
        # canvas for image
        self.canvas = Canvas(main, width=400, height=500)
        self.canvas.grid(row=0, column=0)

        # images
        self.my_images = img = ImageTk.PhotoImage(file = img_str)

        # set first image on canvas
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor = NW, image = self.my_images)

        # button to change image
        self.button = Button(main, text="Change", command=self.onButton)
        self.button.grid(row=1, column=0)
        
    def onButton(self):
        
        self.canvas.destroy()
        self.button.destroy()
        self.nextPage(root)
        # next image
    

#----------------------------------------------------------------------

root = Tk()
MainWindow(root)
root.mainloop()