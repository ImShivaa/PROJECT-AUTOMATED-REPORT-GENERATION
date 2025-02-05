from fpdf import FPDF
import pandas as pd

name = input("Enter your name: ")
print(f"Welcome, {name}! Generating your report...")

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Score": [85, 92, 78]
}

df = pd.DataFrame(data)

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "Student Performance Report", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", "B", 12)
for col in df.columns:
    pdf.cell(60, 10, col, border=1, align="C")
pdf.ln()

pdf.set_font("Arial", "", 12)
for index, row in df.iterrows():
    for value in row:
        pdf.cell(60, 10, str(value), border=1, align="C")
    pdf.ln()

pdf.output("Student_Report.pdf")

print(f"PDF Report Generated: Student_Report.pdf")
print(f"Thank you for using, {name}!")
