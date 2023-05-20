# Function to enable widgets
def enabled_widgets(*widgets):
    """
    # Function to enable widgets
    accept:
    widgets -> *args of widgets
    """
    for my_widget in widgets:
        my_widget["state"] = "normal"


# Function to disabled widgets
def disabled_widgets(*widgets):
    """
    # Function to disabled widgets
    accept:
    widgets -> *args of widgets
    """
    for my_widget in widgets:
        my_widget["state"] = "disabled"


# Function to clear widgets
def clear_widget(*widgets):
    """
    # Function to clear widgets
    accept:
    widgets -> *args of widgets
    """
    for my_widgets in widgets:
        type_of_widget = my_widgets.winfo_class()
        if type_of_widget in "Label":
            my_widgets["text"] = ""
        else:
            my_widgets.delete(0, 'end')


# Function to write message
def write_message(label_to_write, message):
    """
    # Function to write message
    accept:
    label_to_write -> widget
    message -> str
    """
    
    type_of_widget = label_to_write.winfo_class()
    if type_of_widget in "Label":
        label_to_write["text"] = ""
        label_to_write["text"] = message
    else:
        label_to_write.delete(0, "end")
        label_to_write.insert(0, message)
