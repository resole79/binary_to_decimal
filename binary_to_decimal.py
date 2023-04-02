"""
Bin2Dec
Tier: 1-Beginner

Binary is the number system all digital computers are based on. Therefore it's important for developers to understand
binary, or base 2, mathematics. The purpose of Bin2Dec is to provide practice and understanding of how binary
calculations.

Bin2Dec allows the user to enter strings of up to 8 binary digits, 0's and 1's, in any sequence and then displays
its decimal equivalent.

This challenge requires that the developer implementing it follow these constraints:

Arrays may not be used to contain the binary digits entered by the user
Determining the decimal equivalent of a particular binary digit in the sequence must be calculated using a single
mathematical function, for example the natural logarithm. It's up to you to figure out which function to use.

User Stories
 User can enter up to 8 binary digits in one input field
 User must be notified if anything other than a 0 or 1 was entered
 User views the results in a single output field containing the decimal (base 10) equivalent of the binary
  number that was entered
Bonus features
 User can enter a variable number of binary digits

"""
import tkinter as tk
import random
from time import strftime
import math

"""
print(random.__doc__)
print(dir(random))
print(tk.__doc__)
print(dir(tk))
print(strftime.__doc__)
print(dir(strftime))

"""
def get_random_binary():
    binary_int = "0"

    print(entry_header.get())
    for i in range(int(entry_header.get())-1):
        while (i == 0) and (binary_int == "0"):
            binary_int = str(random.randint(0, 1))
        binary_int += str(random.randint(0, 1))
    entry_bin2dec.delete(0, "end")
    entry_bin2dec.insert(0, binary_int)
    print(binary_int)


def a():

    frame_to_disable = r1_v.get()

    if frame_to_disable == 1:
        entry_dec2bin.delete(0, "end")
        entry_bin2dec.delete(0, "end")
        label_dec2bin_result["text"] = ""
        label_bin2dec_result["text"] = ""
        enableChildren(frame_bin2dec)
        enableChildren(frame_header_binary_digit)
        disableChildren(frame_dec2bin)
        button_random_binary["state"] = "normal"
        button_random_decimal["state"] = "disabled"
    else:
        entry_dec2bin.delete(0, "end")
        entry_bin2dec.delete(0, "end")
        label_dec2bin_result["text"] = ""
        label_bin2dec_result["text"] = ""
        enableChildren(frame_dec2bin)
        disableChildren(frame_bin2dec)
        disableChildren(frame_header_binary_digit)
        button_random_binary["state"] = "disabled"
        button_random_decimal["state"] = "normal"


def disableChildren(parent):
    for child in parent.winfo_children():
        wtype = child.winfo_class()
        if wtype not in ('Frame', 'Labelframe', 'TFrame', 'TLabelframe'):
            child.configure(state='disable')
        else:
            disableChildren(child)


def enableChildren(parent):
    for child in parent.winfo_children():
        wtype = child.winfo_class()
        # print (wtype)
        if wtype not in ('Frame', 'Labelframe', 'TFrame', 'TLabelframe'):
            child.configure(state='normal')
        else:
            enableChildren(child)


def binary_to_decimal():
    decimal = 0
    max_digits = 8

    check_max_digits = True
    check_one_zero = True
    binary = entry_bin2dec.get()

    if entry_header.get():
        max_digits = int(entry_header.get())

    print("binary ", binary)
    print("len binary ", len(binary))
    print("max_digits ", max_digits)

    print(f"if {len(binary)} > {max_digits}:")
    if (len(binary)) > max_digits:
        label_error["text"] = f"Error. Sorry, you can't give me more then {max_digits} digit"
        check_max_digits = False
    #else:
    #    label_error["text"] = ""

    try:
        for value in binary:
            if (int(value) == 1) or (int(value) == 0):
                check_one_zero = True
                #label_error["text"] = ""
            else:
                check_one_zero = False
                break
    except Exception as exception:
        label_error["text"] = f"Error. {exception}"

    if binary:
        if not check_one_zero:
            label_error["text"] = "Error. Sorry, your input have invalid number."
            check_one_zero = False

    if check_max_digits and check_one_zero:
        # for power in range(len(binary)):
        # decimal += (int(binary[power]) * math.pow(2, power))

        decimal = int(binary, 2)
        label_bin2dec_result["text"] = f"{int(decimal)}"
        # binary = binary[::-1]
        print(f"\nThe decimal (base 10) equivalent of the {binary} binary (base 2) number is {int(decimal)}")


def dec_to_bin():
    result_decimal_number = ""
    divide = -1
    decimal_number = int(entry_dec2bin.get())
    while decimal_number != 1 and decimal_number != 0:
        divide = decimal_number / 2
        remainder = decimal_number % 2
        result_decimal_number += str(remainder)
        decimal_number = int(divide)
    result_decimal_number += str(int(divide))
    result_decimal_number = result_decimal_number[::-1]
    label_dec2bin_result["text"] = result_decimal_number


def random_decimal():
    decimal_int = random.randint(0, 34359738367)
    entry_dec2bin.delete(0, "end")
    entry_dec2bin.insert(0, decimal_int)
    print(decimal_int)



def time():
    # string = strftime('%H:%M:%S %p')
    string = strftime('%H:%M:%S')
    label_footer.config(text=string)
    label_footer.after(1000, time)


# 34359738367
window = tk.Tk()

window.title("Converter")
window.geometry("500x645")
window.resizable(width=0, height=0)

menubar = tk.Menu(window)

# Adding File Menu and commands
# Adding Help Menu
help_ = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help_)
help_.add_command(label='Tk Help', command=None)
help_.add_command(label='Demo', command=None)
help_.add_separator()
help_.add_command(label='About Tk', command=None)
help_.add_command(label='Exit', command=window.destroy)


frame = tk.LabelFrame(window, relief="groove", bd=3, width=480, height=590)
frame.place(x=10, y=10)

frame_header = tk.LabelFrame(frame, relief="groove", bd=0, width=445, height=140)
frame_header.place(x=15, y=15)

r1_v = tk.IntVar()
r1_v.set(1)
frame_header_choice_convert = tk.LabelFrame(frame_header, text="Active", relief="groove", labelanchor="ne", bd=1, width=210, height=130)
frame_header_choice_convert.place(x=2, y=2)

radiobutton_header = tk.Radiobutton(frame_header_choice_convert, text="Bin2Dec", variable=r1_v, value=1)
radiobutton_header.place(x=15, y=0)
radiobutton_header1 = tk.Radiobutton(frame_header_choice_convert, text="Dec2Bin", variable=r1_v, value=2)
radiobutton_header1.place(x=15, y=25)

button_radiobutton_header = tk.Button(frame_header_choice_convert, text="Choice", width=8, command=a)
# button_radiobutton_header = tk.Button(frame_header, text="Choice", width=8, command=binary_to_decimal)
button_radiobutton_header.place(x=20, y=55)


frame_header_binary_digit = tk.LabelFrame(frame_header, relief="groove", bd=1, width=210, height=130)
frame_header_binary_digit.place(x=230, y=2)

label_header = tk.Label(frame_header_binary_digit, text="Number of binary digits")
label_header.place(x=20, y=10)

entry_header = tk.Entry(frame_header_binary_digit, width=19)
entry_header.place(x=20, y=40)

button_entry_header = tk.Button(frame_header_binary_digit, text="Send", width=8)
button_entry_header.place(x=50, y=70)

frame_bin2dec = tk.LabelFrame(frame, text="Bin2Dec", relief="groove", labelanchor="n", bd=3, width=445, height=150)
frame_bin2dec.place(x=15, y=170)

label_bin2dec = tk.Label(frame_bin2dec, text="Binary Number")
label_bin2dec.place(x=15, y=20)

entry_bin2dec = tk.Entry(frame_bin2dec, width=25)
entry_bin2dec.place(x=120, y=20)

button_bin2dec = tk.Button(frame_bin2dec, text="Convert", width=5, command=binary_to_decimal)
button_bin2dec.place(x=340, y=20)

label_Binary_Number = tk.Label(frame_bin2dec, text="Decimal Number")
label_Binary_Number.place(x=15, y=80)

label_bin2dec_result = tk.Label(frame_bin2dec)
# label_bin2dec_result["font"] = font
label_bin2dec_result.place(x=135, y=80)


frame_dec2bin = tk.LabelFrame(frame, text="Dec2Bin", relief="groove", labelanchor="n", bd=3, width=445, height=150)
frame_dec2bin.place(x=15, y=330)

label_dec2bin = tk.Label(frame_dec2bin, text="Decimal Number")
label_dec2bin.place(x=15, y=20)

entry_dec2bin = tk.Entry(frame_dec2bin, width=25)
entry_dec2bin.place(x=130, y=20)

button_dec2bin = tk.Button(frame_dec2bin, text="Convert", width=5, command=dec_to_bin)
button_dec2bin.place(x=350, y=20)

label_dec2bin_result = tk.Label(frame_dec2bin, text="Binary Number")
label_dec2bin_result.place(x=15, y=80)

label_dec2bin_result = tk.Label(frame_dec2bin, text="11111111111111111111111111111111111")
label_dec2bin_result.place(x=120, y=80)

frame_random = tk.LabelFrame(frame, relief="groove", labelanchor="n", bd=3, width=445, height=40)
frame_random.place(x=15, y=490)

button_random_binary = tk.Button(frame_random, text="Random Binary", width=12, command=get_random_binary)
button_random_binary.place(x=80, y=2)

button_random_decimal = tk.Button(frame_random, text="Random Decimal", width=12, command=random_decimal)
button_random_decimal.place(x=220, y=2)


frame_error = tk.LabelFrame(frame, relief="groove", bd=3, width=445, height=40)
frame_error.place(x=15, y=535)

label_error = tk.Label(frame_error, fg="#FF0000")
label_error.place(x=5, y=5)

frame_footer = tk.LabelFrame(window, relief="groove", bg="#d9d9d9", bd=2, labelanchor="ne", width=500, height=45, font=('calibri', 10, 'bold'))
frame_footer.place(x=0, y=605)

label_footer = tk.Label(frame_footer, justify=tk.RIGHT, width=110, font=('calibri', 12, 'bold'))
label_footer.place(x=0, y=10)

enableChildren(frame_bin2dec)
disableChildren(frame_dec2bin)
button_random_decimal["state"] = "disabled"

time()
window.config(menu=menubar)
window.mainloop()
