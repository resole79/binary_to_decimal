from tkinter import *
from random import randint
from function import *

WIDTH = 500
HEIGHT = 615
WINDOW_GEOMETRY = f"{WIDTH}x{HEIGHT}"


# Class MyWindow
class MyWindow(Tk):
    """
    # Class MyWindow
    method:
    converter_swap, check_number, binary_to_decimal, is_binary, decimal_to_binary, get_random_decimal
    """
    def __init__(self):
        super().__init__()
        self.r1_v = IntVar()
        self.r1_v.set(1)
        self.title("Converter")
        self.geometry(WINDOW_GEOMETRY)
        self.minsize(WIDTH, HEIGHT)
        self.maxsize(WIDTH, HEIGHT)
        self.container_frame = LabelFrame(self, bd=0, width=480, height=600)
        self.container_frame.place(x=10, y=10)
        
        # Header Frame
        self.header_frame = LabelFrame(self.container_frame, bd=0, width=465, height=140)
        self.header_frame.place(x=10, y=10)
        
        # Choice converter Frame
        self.frame_header_choice_convert = LabelFrame(self.header_frame, text="Active", relief="groove")
        self.frame_header_choice_convert.configure(labelanchor="ne", bd=3, width=210, height=135)
        self.frame_header_choice_convert.place(x=10, y=0)
        self.radiobutton_header = Radiobutton(self.frame_header_choice_convert, text="Bin2Dec")
        self.radiobutton_header.configure(variable=self.r1_v, value=1)
        self.radiobutton_header.place(x=10, y=0)
        self.radiobutton_header1 = Radiobutton(self.frame_header_choice_convert, text="Dec2Bin")
        self.radiobutton_header1.configure(variable=self.r1_v, value=2)
        self.radiobutton_header1.place(x=10, y=25)
        self.button_radiobutton_header = Button(self.frame_header_choice_convert, text="Choice", width=8)
        self.button_radiobutton_header.configure(command=self.converter_swap)
        self.button_radiobutton_header.place(x=20, y=55)
        
        # Digit Number Input Frame
        self.frame_header_binary_digit = LabelFrame(self.header_frame, relief="groove", bd=3, width=210, height=130)
        self.frame_header_binary_digit.place(x=250, y=2)
        label_header = Label(self.frame_header_binary_digit, text="Number of binary digits")
        label_header.place(x=20, y=10)
        self.entry_header = Entry(self.frame_header_binary_digit, width=19)
        self.entry_header.place(x=20, y=40)
        self.button_entry_header = Button(self.frame_header_binary_digit, text="Send", width=8)
        self.button_entry_header.configure(command=self.check_number)
        self.button_entry_header.place(x=50, y=70)
        
        # Bin2Dec Frame
        self.frame_bin2dec = LabelFrame(self.container_frame, text="Bin2Dec", relief="groove", labelanchor="n", bd=3)
        self.frame_bin2dec.configure(width=465, height=150)
        self.frame_bin2dec.place(x=10, y=170)
        label_bin2dec = Label(self.frame_bin2dec, text="Binary Number")
        label_bin2dec.place(x=10, y=20)
        self.entry_bin2dec = Entry(self.frame_bin2dec, width=31)
        self.entry_bin2dec.place(x=120, y=20)
        self.button_bin2dec = Button(self.frame_bin2dec, text="Convert", width=5, command=self.binary_to_decimal)
        self.button_bin2dec.place(x=380, y=17)
        label_binary_number = Label(self.frame_bin2dec, text="Decimal Number")
        label_binary_number.place(x=10, y=80)
        self.label_bin2dec_result = Label(self.frame_bin2dec)
        self.label_bin2dec_result.place(x=135, y=80)
        
        # Dec2Bin Frame
        self.frame_dec2bin = LabelFrame(self.container_frame, text="Dec2Bin", relief="groove", labelanchor="n", bd=3)
        self.frame_dec2bin.configure(width=465, height=150)
        self.frame_dec2bin.place(x=10, y=335)
        label_dec2bin = Label(self.frame_dec2bin, text="Decimal Number")
        label_dec2bin.place(x=15, y=20)
        self.entry_dec2bin = Entry(self.frame_dec2bin, width=28)
        self.entry_dec2bin.place(x=140, y=20)
        self.button_dec2bin = Button(self.frame_dec2bin, text="Convert", width=5, command=self.decimal_to_binary)
        self.button_dec2bin.place(x=380, y=17)
        label_dec2bin_result = Label(self.frame_dec2bin, text="Binary Number")
        label_dec2bin_result.place(x=15, y=80)
        self.label_dec2bin_result = Label(self.frame_dec2bin)
        self.label_dec2bin_result.place(x=120, y=80)
        
        # Random Number Frame
        self.frame_random = LabelFrame(self.container_frame, bd=0, width=465, height=40)
        self.frame_random.place(x=10, y=500)
        self.button_random_binary = Button(self.frame_random, text="Random Binary", width=12)
        self.button_random_binary.configure(command=self.get_random_binary)
        self.button_random_binary.place(x=100, y=2)
        self.button_random_decimal = Button(self.frame_random, text="Random Decimal", width=12)
        self.button_random_decimal.configure(command=self.get_random_decimal)
        self.button_random_decimal.place(x=240, y=2)
        
        # Error Frame
        self.frame_error = LabelFrame(self.container_frame, relief="groove", bd=0, width=465, height=40)
        self.frame_error.place(x=10, y=550)
        self.label_error = Label(self.frame_error, fg="#FF0000", font=("Arial", 12, "bold"))
        self.label_error.place(x=5, y=0)
    
    # Method converter_swap
    def converter_swap(self):
        """
        # Method converter_swap
        disabled or enabled widgets depend on choice of converter use
        """
        frame_to_disable = self.r1_v.get()
        
        if frame_to_disable == 1:
            clear_widget(
                self.entry_dec2bin,
                self.label_dec2bin_result,
                self.label_error
            )
            disabled_widgets(self.button_dec2bin, self.entry_dec2bin, self.button_random_decimal)
            enabled_widgets(
                self.button_bin2dec, self.entry_bin2dec,
                self.button_random_binary,
                self.entry_header,
                self.button_entry_header
            )
        
        else:
            clear_widget(
                self.entry_header,
                self.entry_bin2dec,
                self.label_bin2dec_result,
                self.label_error
            )
            disabled_widgets(
                self.button_bin2dec,
                self.entry_bin2dec,
                self.button_random_binary,
                self.entry_header,
                self.button_entry_header
            )
            enabled_widgets(self.button_dec2bin, self.entry_dec2bin, self.button_random_decimal)
    
    # Method check_number
    def check_number(self):
        """
        # Method check_number
        check entry_header if is empty, numeric, greater than 23 or less than 2 digit
        """
        max_digits = 23
        min_digits = 2
        message = ""
        
        if self.entry_header.get() == "":
            message = "Error. Sorry, your input can't be empty."
            clear_widget(self.entry_bin2dec, self.label_bin2dec_result)
            disabled_widgets(self.button_bin2dec, self.button_random_binary)
        
        elif not self.entry_header.get().isnumeric():
            message = "Error. Sorry, your input has invalid character."
            clear_widget(self.entry_bin2dec, self.label_bin2dec_result)
            disabled_widgets(self.button_bin2dec, self.button_random_binary)
        
        elif int(self.entry_header.get()) > max_digits:
            message = f"Error. Sorry, you can't give me more than {max_digits} digit"
            clear_widget(self.entry_bin2dec, self.label_bin2dec_result)
            disabled_widgets(self.button_bin2dec, self.button_random_binary)
            
        elif int(self.entry_header.get()) <= min_digits:
            message = f"Error. Sorry, you can't give me less than or equal to {min_digits} digit"
            clear_widget(self.entry_bin2dec, self.label_bin2dec_result)
            disabled_widgets(self.button_bin2dec, self.button_random_binary)
        
        else:
            enabled_widgets(self.button_bin2dec, self.button_random_binary)
        
        write_message(self.label_error, message)
    
    # Method binary_to_decimal
    def binary_to_decimal(self):
        """
        # Method binary_to_decimal
        convert binary number to decimal
        """
        message = ""
        binary = self.entry_bin2dec.get()
        
        if self.entry_header.get() != "":
            max_digits = int(self.entry_header.get())
        else:
            max_digits = 8

        if not binary:
            message = "Error. Sorry, your input can't be empty."
            clear_widget(self.label_bin2dec_result)
        elif not binary.isnumeric():
            message = "Error. Sorry, your input has invalid character."
            clear_widget(self.label_bin2dec_result)
        elif not self.is_binary():
            message = "Error. Sorry, your input has invalid number."
            clear_widget(self.label_bin2dec_result)
        elif (len(binary)) > max_digits:
            message = f"Error. Sorry, you can't give me more than {max_digits} digit"
            clear_widget(self.label_bin2dec_result)
        else:
            decimal = int(binary, 2)
            write_message(self.label_bin2dec_result, int(decimal))
        
        write_message(self.label_error, message)
    
    # Method is_binary
    def is_binary(self):
        """
        # Method is_binary
        check if the number is binary
        """
        check_one_zero = True
        binary = self.entry_bin2dec.get()
        for value in binary:
            if (int(value) != 1) and (int(value) != 0):
                check_one_zero = False
        
        return check_one_zero
    
    # Method decimal_to_binary
    def decimal_to_binary(self):
        """
        # Method decimal_to_binary
        convert decimal number to binary
        """
        max_digits = 11
        message = ""
        result_decimal_number = ""
        divide = -1

        if not self.entry_dec2bin.get():
            message = "Error. Sorry, your input can't be empty."
        elif not self.entry_dec2bin.get().isnumeric():
            message = "Error. Sorry, your input has invalid character."
        elif (len(self.entry_dec2bin.get())) > max_digits:
            message = f"Error. Sorry, you can't give me more than {max_digits} digit"
        else:
            decimal_number = int(self.entry_dec2bin.get())

            while decimal_number != 1 and decimal_number != 0:
                divide = decimal_number // 2
                remainder = decimal_number % 2
                result_decimal_number += str(remainder)
                decimal_number = int(divide)

            result_decimal_number += str(int(divide))
            result_decimal_number = result_decimal_number[::-1]
            self.label_dec2bin_result["text"] = result_decimal_number
        
        write_message(self.label_error, message)
    
    # Method get_random_binary
    def get_random_binary(self):
        """
        # Method get_random_binary
        get a random binary number
        """
        if self.entry_header.get() != "":
            max_digits = int(self.entry_header.get())
        else:
            max_digits = 8
        
        binary_int = [str(randint(0, 1)) for _ in range(0, max_digits)]
        write_message(self.entry_bin2dec, "".join(binary_int))
    
    # Method get_random_decimal
    def get_random_decimal(self):
        """
        # Method get_random_decimal
        get a random decimal number
        """
        max_digits = 12
        decimal_int = [str(randint(0, 9)) for _ in range(1, max_digits)]
        write_message(self.entry_dec2bin, "".join(decimal_int))
