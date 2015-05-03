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

lcd = CharLCD(cols=16, rows=2)


# Test custom chars
lcd.clear()
jos = (0b11111, 0b11111, 0b00000, 0b00000, 0b00000, 0b00000, 0b00000, 0b00000)
sus = (0b00000, 0b00000, 0b00000, 0b00000, 0b00000, 0b00000, 0b11111, 0b11111)
ambele = (0b11111, 0b11111, 0b00000, 0b00000, 0b00000, 0b00000, 0b11111, 0b11111)
punct = (0b00000, 0b00000, 0b00011, 0b00011, 0b00011, 0b00011, 0b00000, 0b00000)


lcd.create_char(0, jos)
lcd.create_char(1, sus)
lcd.create_char(2, ambele)
lcd.create_char(3, punct)

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

while True:
    new_time = datetime.now().strftime('%H%M')
    if new_time!=old_time :
	    digits = str(new_time)
	    tens_hour = disp_number(digits[0], 0)
	    hour = disp_number(digits[1], 4)
	    tens_minutes = disp_number(digits[2], 9)
	    tens_minutes = disp_number(digits[3], 13)
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

