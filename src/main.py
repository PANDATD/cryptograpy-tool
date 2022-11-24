#!/usr/bin/env python3.10

import flet as ft
from flet import *

def main(page: ft.Page):
    page.title = "Creyptography- Tools"
    page.vertical_alignment = "start"
    page.horizontal_alignment = "start"

    headline = ft.Text("Cryptography Tools",style="headlineMedium") # Create a headline

    t1 = ft.Text("Please Kindly Select an algorithm for Encryption",
                 font_family="Ubuntu",

                 )

    dd = ft.Dropdown(
        options=[ft.dropdown.Option("SHA256"), 
        ft.dropdown.Option("SHA"), 
        ft.dropdown.Option("MD5"), 
        ft.dropdown.Option("SHA224"),
        ft.dropdown.Option("SHA512")],
       
        )
        
    t2 = ft.Text("Please Kindly Select an algorithm for Decryption",
                    font_family="Ubuntu",
                    )

    dd2 = ft.Dropdown(
        options=[ft.dropdown.Option("SHA256"),
        ft.dropdown.Option("SHA"),
        ft.dropdown.Option("MD5"),
        ft.dropdown.Option("SHA224"),
        ft.dropdown.Option("SHA512")],


        )
    t3 = ft.Text("Please Kindly Select an algorithm for Hashing",
                    font_family="Ubuntu",
                    )
    dd3 = ft.Dropdown(
        options=[ft.dropdown.Option("SHA256"),
        ft.dropdown.Option("SHA"),
        ft.dropdown.Option("MD5"),
        ft.dropdown.Option("SHA224"),
        ft.dropdown.Option("SHA512")],
       
        )


    mytabs = ft.Tabs(
        selected_index=3,
        tabs=[
        ft.Tab(
            text="Encryption",   
                    
        ),
        ft.Tab(
            text="Decryption",
            
            
        ),
        ft.Tab(
            text="Hashing",
           
           
        ),
        ft.Tab(
            text="About",
            
        ),
        ]

    )

    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        if  status == "Encryption":
            page.add(t1,dd)
        elif status == "Decryption":
            page.add(t2,dd2)
        elif status == "Hashing":
            page.add(t3,dd3)
        else :
           None
        update()
    
    page.add(headline,mytabs)



def sha256():
    pass
    

def sha():
    pass

def md5():
    pass

def sha224():
    pass

def sha512():
    pass



ft.app(target=main)