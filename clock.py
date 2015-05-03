#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import sys

from RPLCD import CharLCD
from RPLCD import Alignment, CursorMode, ShiftMode
from RPLCD import cursor, cleared
from time import strftime, sleep
from datetime import datetime

try:
    input = raw_input
except NameError:
    pass

try:
    unichr = unichr
except NameError:
    unichr = chr

old_time = 0
counter = 0
lcd = CharLCD(cols=16, rows=2)


# custom symbols
lcd.clear()
top_line = (0b11111, 0b11111, 0b00000, 0b00000, 0b00000, 0b00000, 0b00000, 0b00000)
bottom_line = (0b00000, 0b00000, 0b00000, 0b00000, 0b00000, 0b00000, 0b11111, 0b11111)
both_lines = (0b11111, 0b11111, 0b00000, 0b00000, 0b00000, 0b00000, 0b11111, 0b11111)
dot = (0b00000, 0b00000, 0b00011, 0b00011, 0b00011, 0b00011, 0b00000, 0b00000)


lcd.create_char(0, top_line)
lcd.create_char(1, bottom_line)
lcd.create_char(2, both_lines)
lcd.create_char(3, dot)

# build big digits

def disp_number(number, position):

    if number=="1" :
        lcd.cursor_pos = (0, position)
        lcd.write_string(unichr(0))
        lcd.write_string(unichr(255))
        lcd.write_string(unichr(254))
        lcd.cursor_pos = (1, position)
        lcd.write_string(unichr(1))
        lcd.write_string(unichr(255))
        lcd.write_string(unichr(1))
		
    elif number=="2" :
        lcd.cursor_pos = (0, position)
        lcd.write_string(unichr(2))
        lcd.write_string(unichr(2))
        lcd.write_string(unichr(255))
        lcd.cursor_pos = (1, position)
        lcd.write_string(unichr(255))
        lcd.write_string(unichr(1))
        lcd.write_string(unichr(1))

    elif number=="3" :
        lcd.cursor_pos = (0, position)
        lcd.write_string(unichr(0))
        lcd.write_string(unichr(2))
        lcd.write_string(unichr(255))
        lcd.cursor_pos = (1, position)
        lcd.write_string(unichr(1))
        lcd.write_string(unichr(1))
        lcd.write_string(unichr(255))

    elif number=="4" :
        lcd.cursor_pos = (0, position)
        lcd.write_string(unichr(255))
        lcd.write_string(unichr(1))
        lcd.write_string(unichr(255))
        lcd.cursor_pos = (1, position)
        lcd.write_string(unichr(254))
        lcd.write_string(unichr(254))
        lcd.write_string(unichr(255))
		
    elif number=="5" :
        lcd.cursor_pos = (0, position)
        lcd.write_string(unichr(255))
        lcd.write_string(unichr(2))
        lcd.write_string(unichr(2))
        lcd.cursor_pos = (1, position)
        lcd.write_string(unichr(1))
        lcd.write_string(unichr(1))
        lcd.write_string(unichr(255))
		
    elif number=="6" :
        lcd.cursor_pos = (0, position)
        lcd.write_string(unichr(255))
        lcd.write_string(unichr(2))
        lcd.write_string(unichr(2))
        lcd.cursor_pos = (1, position)
        lcd.write_string(unichr(255))
        lcd.write_string(unichr(1))
        lcd.write_string(unichr(255))
		
    elif number=="7" :
        lcd.cursor_pos = (0, position)
        lcd.write_string(unichr(0))
        lcd.write_string(unichr(0))
        lcd.write_string(unichr(255))
        lcd.cursor_pos = (1, position)
        lcd.write_string(unichr(254))
        lcd.write_string(unichr(254))
        lcd.write_string(unichr(255))
		
    elif number=="8" :
        lcd.cursor_pos = (0, position)
        lcd.write_string(unichr(255))
        lcd.write_string(unichr(2))
        lcd.write_string(unichr(255))
        lcd.cursor_pos = (1, position)
        lcd.write_string(unichr(255))
        lcd.write_string(unichr(1))
        lcd.write_string(unichr(255))
		
    elif number=="9" :
        lcd.cursor_pos = (0, position)
        lcd.write_string(unichr(255))
        lcd.write_string(unichr(2))
        lcd.write_string(unichr(255))
        lcd.cursor_pos = (1, position)
        lcd.write_string(unichr(1))
        lcd.write_string(unichr(1))
        lcd.write_string(unichr(255))
     
    else :
        lcd.cursor_pos = (0, position)
        lcd.write_string(unichr(255))
        lcd.write_string(unichr(0))
        lcd.write_string(unichr(255))
        lcd.cursor_pos = (1, position)
        lcd.write_string(unichr(255))
        lcd.write_string(unichr(1))
        lcd.write_string(unichr(255))
        
#scroll effect
        
def shift(direction): 
    if direction=="left" :
        for x in range(0, 16):
            lcd.shift_display(-1)
            sleep(0.05)
    else :
        for x in range(0, 16):
            lcd.shift_display(1)
            sleep(0.05)

#main loop

while True:
    counter += 1
    new_time = datetime.now().strftime('%H%M%d')
    month = datetime.now().strftime('%B')
    day_name = datetime.now().strftime('%A')
    if new_time!=old_time :
	    digits = str(new_time)
	    tens_hour = disp_number(digits[0], 0)
	    hour = disp_number(digits[1], 4)
	    tens_minutes = disp_number(digits[2], 9)
	    minutes = disp_number(digits[3], 13)
	    old_time = new_time
	    #lcd.write_string(digits)
    lcd.cursor_pos = (0, 7)
    lcd.write_string(unichr(3))
    lcd.cursor_pos = (1, 7)
    lcd.write_string(unichr(3))
    sleep(0.5)
    lcd.cursor_pos = (0, 7)
    lcd.write_string(unichr(254))
    lcd.cursor_pos = (1, 7)
    lcd.write_string(unichr(254))
    sleep(0.5)
    if counter==15 :    ## date display interval in seconds
        counter = 0
        shift("left")
        tens_day = disp_number(digits[4], 0)
        day = disp_number(digits[5], 4)
        lcd.cursor_pos = (0, 9)
        lcd.write_string('       ')
        lcd.cursor_pos = (1, 9)
        lcd.write_string('       ')
        lcd.cursor_pos = (0, 9)
        lcd.write_string(month)
        lcd.cursor_pos = (1, 9)
        lcd.write_string(day_name)
        shift("right")
        sleep(3)
        shift("left")
        lcd.write_string('       ')
        lcd.cursor_pos = (1, 9)
        lcd.write_string('       ')
        tens_hour = disp_number(digits[0], 0)
        hour = disp_number(digits[1], 4)
        tens_minutes = disp_number(digits[2], 9)
        minutes = disp_number(digits[3], 13)
        shift("right")
        
        

