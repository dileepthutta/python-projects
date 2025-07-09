from tkinter import *
from tkinter import messagebox
from fpdf import FPDF
import pyqrcode
import os

class PDFCV(FPDF):
    def header(self):
        # Optional: Add header text or styling if needed
        pass

    def footer(self):
        # Optional: Add footer text or styling
        pass

    def generate_cv(self, name, email, phone_number, address, skills, work_experience, education, about_me, website):
        self.add_page()
        self.set_font('Arial', 'B', 26)
        self.cell(0, 10, name, ln=True, align='C')

        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Contact Information", ln=True)

        self.set_font("Arial", "", 10)
        self.cell(0, 5, f"Name: {name}", ln=True)
        self.cell(0, 5, f"Email: {email}", ln=True)
        self.cell(0, 5, f"Phone: {phone_number}", ln=True)
        self.cell(0, 5, f"Address: {address}", ln=True)
        self.cell(0, 5, f"Website: {website}", ln=True)

        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Skills", ln=True)
        self.set_font("Arial", "", 10)
        for skill in skills:
            self.cell(0, 5, f"- {skill}", ln=True)

        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Work Experience", ln=True)
        self.set_font("Arial", "", 10)
        for exp in work_experience:
            self.cell(0, 5, f"{exp['title']}: {exp['description']}", ln=True)

        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Education", ln=True)
        self.set_font("Arial", "", 10)
        for edu in education:
            self.cell(0, 5, f"{edu['degree']}: {edu['university']}", ln=True)

        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "About Me", ln=True)
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 5, about_me)

        # Add QR code to the bottom-right
        self.ln(10)
        self.image("mywebsite.png", x=160, y=self.get_y(), w=30)

        self.output("cv.pdf")

# GUI Setup
window = Tk()
window.title("CV Generator")
window.geometry("500x700")

# Utility functions
def create_labeled_entry(label_text, row):
    label = Label(window, text=label_text)
    label.grid(row=row, column=0, sticky=W, padx=10, pady=5)
    entry = Entry(window, width=50)
    entry.grid(row=row, column=1, padx=10)
    return entry

def create_labeled_text(label_text, row, height=5):
    label = Label(window, text=label_text)
    label.grid(row=row, column=0, sticky=NW, padx=10, pady=5)
    text = Text(window, width=50, height=height)
    text.grid(row=row, column=1, padx=10)
    return text

# Entry fields
entry_name = create_labeled_entry("Name:", 0)
entry_email = create_labeled_entry("Email:", 1)
entry_phone = create_labeled_entry("Phone:", 2)
entry_address = create_labeled_entry("Address:", 3)
entry_website = create_labeled_entry("Website:", 4)

entry_skills = create_labeled_text("Skills (One per line):", 5)
entry_experience = create_labeled_text("Work Experience (Title: Description):", 6)
entry_education = create_labeled_text("Education (Degree: University):", 7)
entry_about_me = create_labeled_text("About Me:", 8)

# Main function to generate PDF
def generate_cv_pdf():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    phone_number = entry_phone.get().strip()
    address = entry_address.get().strip()
    website = entry_website.get().strip()
    skills = [s.strip() for s in entry_skills.get("1.0", END).strip().split('\n') if s.strip()]

    work_experience = []
    for line in entry_experience.get("1.0", END).strip().split('\n'):
        if ':' in line:
            title, description = line.split(':', 1)
            work_experience.append({'title': title.strip(), 'description': description.strip()})
        else:
            messagebox.showerror("Input Error", f"Invalid work experience format: '{line}'")
            return

    education = []
    for line in entry_education.get("1.0", END).strip().split('\n'):
        if ':' in line:
            degree, university = line.split(':', 1)
            education.append({'degree': degree.strip(), 'university': university.strip()})
        else:
            messagebox.showerror("Input Error", f"Invalid education format: '{line}'")
            return

    about_me = entry_about_me.get("1.0", END).strip()

    # Validate required fields
    if not all([name, email, phone_number, address, website, skills, work_experience, education, about_me]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Generate QR code
    try:
        qrcode = pyqrcode.create(website)
        qrcode.png("mywebsite.png", scale=6)
    except Exception as e:
        messagebox.showerror("QR Code Error", f"Failed to generate QR code: {e}")
        return

    # Generate PDF
    try:
        cv = PDFCV()
        cv.generate_cv(name, email, phone_number, address, skills, work_experience, education, about_me, website)
        messagebox.showinfo("Success", "PDF CV generated successfully.")
        os.startfile("cv.pdf")  # Auto-open the PDF (Windows only)
    except Exception as e:
        messagebox.showerror("PDF Error", f"Failed to generate PDF: {e}")

# Button to generate CV
button_generate = Button(window, text="Generate CV", command=generate_cv_pdf)
button_generate.grid(row=9, column=0, columnspan=2, pady=20)

window.mainloop()