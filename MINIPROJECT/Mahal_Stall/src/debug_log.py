# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 17:13:46 2025

@author: ramus
"""

# debug_log.py
# This file handles debugging and logging activities
# Used during development, testing, and maintenance phases

from datetime import datetime

def _current_time():
    """Returns current date and time"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log_info(message):
    """Logs general information messages"""
    print(f"[INFO] {_current_time()} : {message}")


def log_warning(message):
    """Logs warning messages"""
    print(f"[WARNING] {_current_time()} : {message}")


def log_error(message):
    """Logs error messages"""
    print(f"[ERROR] {_current_time()} : {message}")


def log_booking(room_no, customer):
    """Logs booking-related information"""
    log_info(f"Room {room_no} booked by {customer}")


def log_cancellation(room_no):
    """Logs cancellation-related information"""
    log_info(f"Booking cancelled for Room {room_no}")


def log_invalid_action(action):
    """Logs invalid user actions"""
    log_warning(f"Invalid action attempted: {action}")
