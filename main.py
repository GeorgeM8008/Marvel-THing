#-----------------------------------------------------------------------------
# Title: Make and use a Module
# Coders: George Lase
# Version: 001
#-----------------------------------------------------------------------------
''' Example Code - Storing Your Functions and Data in Modules.

    Syntax for accessing module.
        import [module]
    
    When a function from a module is called, you use the following syntax.
        module_name.function_name()
        
    When a variable from a module is called, you use the following syntax.
        module_name.variable_name
    
'''
#-----------------------------------------------------------------------------
# Imports and Global Variables -----------------------------------------------

import heros

# Functions ------------------------------------------------------------------
def choose_char():
    
    print("What character whould you to be?")
    for key in heros.Marvel_Superheros:
      print(f"  - {key}")
    choice = input("Choice: ")
    heros.Hero = choice

# Main -----------------------------------------------------------------------
print("Welcome to my example.\n")
choose_char()
print(f"/nYou choose to be {heros.Hero}!")
print("Finished!\n\n")

