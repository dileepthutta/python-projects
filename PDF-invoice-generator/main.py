from fpdf import *
from tkinter import *

window = Tk()
window.title('PDF-Invoice-Generator')
window.config(background="Black")

medicines = {
    "Medicine A" : 10,
    "Medicine B" : 20,
    "Medicine C" : 30,
    "Medicine D" : 40
}
invoice_items = []
total_amount = 0.0


# Function to add medicine.
def add_medicine():
    try:
        selected_medicine = medicine_listbox.get(ACTIVE)
        quantity = int(quantity_entry.get())
        if selected_medicine and quantity > 0:
            price = medicines[selected_medicine]
            item_total = price * quantity
            invoice_items.append((selected_medicine, quantity, item_total))
            total_amount_entry.delete(0, END)
            total_amount_entry.insert(END, str(calculate_total()))
            update_invoice_text()
    except ValueError:
        total_amount_entry.delete(0, END)
        total_amount_entry.insert(END, "Invalid quantity")

# To calculate Total Amount.
def calculate_total():
    total = 0.0
    for item in invoice_items:
        total += item[2]
    return total


# Function to update the invoice text
def update_invoice_text():
    invoice_text.delete(1.0, END)
    for item in invoice_items:
        invoice_text.insert(
            END,
            f"Medicine: {item[0]}, Quantity: {item[1]}, Total: {item[2]}\n"
        )


# Function to generate and save the invoice as PDF
def generate_invoice():
    customer_name = customer_entry.get().strip()

    if not customer_name:
        invoice_text.insert(END, "Enter customer name.\n")
        return

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Helvetica", size=12)
    pdf.cell(0, 10, text="Invoice", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.cell(0, 10, text="Customer: " + customer_name,
             new_x="LMARGIN", new_y="NEXT", align='L')
    pdf.cell(0, 10, text="", new_x="LMARGIN", new_y="NEXT")

    for item in invoice_items:
        medicine_name, quantity, item_total = item
        pdf.cell(
            0, 10,
            text=f"Medicine: {medicine_name}, Quantity: {quantity}, Total: {item_total}",
            new_x="LMARGIN",
            new_y="NEXT",
            align="L"
        )

    # Add total amount once
    pdf.cell(0, 10,
             text="Total Amount: " + str(calculate_total()),
             new_x="LMARGIN",
             new_y="NEXT",
             align="L")

    # Save the PDF
    pdf.output("invoice.pdf")

    invoice_text.insert(END, "Invoice generated and saved as 'invoice.pdf'\n")








#GUI Layout
medicine_label = Label(text="Medicine",fg="white",bg="black")
medicine_label.grid(row=0,column=0)

#Adding medicines into the list box.
medicine_listbox = Listbox(selectmode=SINGLE,fg="white",bg="black",highlightthickness=0)
for medicine in medicines:
    medicine_listbox.insert(END,medicine)
medicine_listbox.grid(row=0,column=1)

quantity_label = Label(text='Quantity',fg="white",bg="black")
quantity_label.grid(row=1,column=0)

quantity_entry = Entry()
quantity_entry.grid(row=1,column=1)

add_button = Button(text="Add Medicine",command=add_medicine,fg="white",bg="black")
add_button.grid(row=2,column=1)

total_amount_label = Label(text="Total Amount",fg="white",bg="black")
total_amount_label.grid(row=3,column=0)

total_amount_entry = Entry()
total_amount_entry.grid(row=3,column=1)

customer_label = Label(text="Customer Name:",fg="white",bg="black")
customer_label.grid(row=4,column=0)

customer_entry = Entry()
customer_entry.grid(row=4,column=1)

generate_button = Button(text="Generate Invoice",command=generate_invoice,fg="white",bg="black")
generate_button.grid(row=6,column=1)

invoice_text = Text(height=10,width=50,fg="white",bg="black")
invoice_text.grid(row=5,column=1)


window.mainloop()

