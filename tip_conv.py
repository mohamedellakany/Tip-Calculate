from tkinter import Tk, Button, Label, Radiobutton, Entry, StringVar, DoubleVar, IntVar


class TipCalc():
    def __init__(self):
        window = Tk()
        window.title("Tip Calculator")
        window.geometry("450x350")
        window.configure(background="light blue")
        window.resizable(width=False, height=False)

        self.meal_cost = StringVar()
        self.tip_precent = IntVar()
        self.tip = StringVar()
        self.total_cost = StringVar()

        #Labels and Entries
        lbl_1 = Label(window, text='Tip Percentage', bg='green',
                      fg='white', width=14).grid(column=0, row=0, padx=15, pady=15)
        lbl_2 = Label(window, text='Bill Amount', bg='red', fg='white', width=14).grid(
            column=1, row=0, padx=35, pady=15)
        ent_1 = Entry(window, textvariable=self.meal_cost,
                      width=14).grid(row=0, column=2)

        # Tip amount label and entry
        tip_amount_lbl = Label(
            window, text="Tip Amonut", bg='red', fg='white', width=14).grid(row=2, column=1)
        tip_amount_ent = Entry(window, textvariable=self.tip,
                               width=14).grid(row=2, column=2)

        # Bill Total label and entry
        bill_total_lbl = Label(
            window, text="Total Bill", bg='red', fg='white', width=14).grid(row=5, column=1)
        tbill_total_ent = Entry(
            window, textvariable=self.total_cost, width=14).grid(row=5, column=2)

        # Radio Buttons
        rb_5_percent = Radiobutton(
            window, text="5%", variable=self.tip_precent, value=5, width=4).grid(row=1, column=0)
        rb_10_percent = Radiobutton(
            window, text="10%", variable=self.tip_precent, value=5, width=4).grid(row=2, column=0)
        rb_15_percent = Radiobutton(
            window, text="15%", variable=self.tip_precent, value=5, width=4).grid(row=3, column=0)
        rb_20_percent = Radiobutton(
            window, text="20%", variable=self.tip_precent, value=5, width=4).grid(row=4, column=0)
        rb_25_percent = Radiobutton(
            window, text="25%", variable=self.tip_precent, value=5, width=4).grid(row=5, column=0)
        rb_30_percent = Radiobutton(
            window, text="30%", variable=self.tip_precent, value=5, width=4).grid(row=6, column=0)

        # Button to Calculate and Clear

        calc_btn = Button(window, bg='blue', fg="white", text="Calculate",
                          width=14, command=self.claculate).grid(row=7, column=1)
        clear_btn = Button(window,  bg='black', fg="white", text="Clear",
                           width=14, command=self.clear).grid(row=7, column=2)

        window.mainloop()

        # Function To Calculate

    def claculate(self):
        before_tip = float(self.meal_cost.get())
        percentage = self.tip_precent.get() / 100
        tip_amount_entry = before_tip * percentage
        self.tip.set(tip_amount_entry)

        final_bill = before_tip + tip_amount_entry
        self.total_cost.set(final_bill)

    def clear(self):
        self.total_cost.set("")
        self.meal_cost.set("")
        self.tip.set("")


TipCalc()
