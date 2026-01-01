# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 17:13:21 2025

@author: ramus
"""
# utils.py

def pause():
    """Pauses the screen until user presses Enter"""
    input("\nPress Enter to continue...")


def print_header(title):
    """Prints a formatted header"""
    print("\n" + "=" * 40)
    print(title.center(40))
    print("=" * 40)


def get_integer_input(message):
    """
    Safely gets integer input from user
    Avoids program crash due to wrong input
    """
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("❌ Please enter a valid number")


def confirm_action(message):
    """
    Asks user for Yes/No confirmation
    Returns True or False
    """
    choice = input(f"{message} (y/n): ").lower()
    return choice == "y"


def format_currency(amount, currency):
    """Formats amount with currency symbol"""
    return f"{currency}{amount}"
