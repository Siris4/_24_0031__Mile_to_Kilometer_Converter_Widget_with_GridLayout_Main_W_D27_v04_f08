from tkinter import *

# Column is the Top that goes left and right.
# Row is the Left side that goes up and down.

# Functions:

def miles_to_kilometers():
    miles = float(miles_input.get())
    kilometer = miles * 1.609   #floating point number * another floating point number (because some people may type out decimal places)  #can also use round() to round to whole numbers (if you want..)
    km_result_label.config(text=str(kilometer))   #.config() and text= is used to refresh the calculated result and to update the (col=1, row=1) box. #to place the converted number as a LABEL tho, it has to be a STRING!!!
                    #Basically, we need to take the user_input (miles_input), which is a string, convert to a Float, to do multiplication of math with decimals involved, then BACK to a string again, so that it can be imbedded into the Label format that is required from a label.
                    # you can use: text=str(kilometer) OR (text=f"{kilometer}")

# Window, size, and padding:
window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300, height=200)
#If you want to pad the entire window as a whole, use the below code:
window.config(padx=50, pady=50)

###################################

# Create an Entry widget
miles_input = Entry(width=6)
miles_input.grid(column=1, row=0)   #the fix was to reduce the row from 1 to 0.
# Set default text or placeholder within the double quotes (code line below):
miles_input.insert(0, "0")


###################################

# Labels
label = Label(text="This is old text")
label.config(text="Miles")
label.grid(column=2, row=0)   #the fix was to reduce the row from 1 to 0.

###################################

label = Label(text="This is old text")
label.config(text="is equal to")
label.grid(column=0, row=1)   #the fix was to reduce the col from 1 to 0, and row from 2 to 1.

###################################

km_result_label = Label(text="This is old text")
km_result_label.config(text="0")
km_result_label.grid(column=1, row=1)   #the fix was to reduce the col from 2 to 1, and row from 2 to 1.

###################################

label = Label(text="This is old text")
label.config(text="Km")
label.grid(column=2, row=1)   #the fix was to reduce the col from 3 to 2, and row from 2 to 1.

###################################

# Calculate Button:

button = Button(text="Calculate", command=miles_to_kilometers)  #ONCE the button is actually pressed, then you run the calculation from the miles and it rewrites over the km quantity converted amount and places it OVER the 0 that was written at the col=1, row=1 that was at the original spot for the km_result_label
button.grid(column=1, row=2)   #the fix was to reduce the col from 2 to 1, and row from 3 to 2.

###################################

# calc_button = Button(text="I'm a Button. Click Me!", command=user_typed_and_clicked_button)
# calc_button.grid(column=1, row=1)


# completes window loop to remain open:
window.mainloop()