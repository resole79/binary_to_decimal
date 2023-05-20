from display import MyWindow
from function import *

my_window = MyWindow()

if my_window.r1_v.get() == 1:
    disabled_widgets(my_window.button_dec2bin, my_window.entry_dec2bin, my_window.button_random_decimal)
    enabled_widgets(my_window.button_bin2dec, my_window.entry_bin2dec, my_window.button_random_binary)
else:
    disabled_widgets(my_window.button_bin2dec, my_window.entry_bin2dec, my_window.button_random_binary)
    enabled_widgets(my_window.button_dec2bin, my_window.entry_dec2bin, my_window.button_random_decimal)

my_window.mainloop()
