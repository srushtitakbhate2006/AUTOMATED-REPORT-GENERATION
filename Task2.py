from fpdf import FPDF
import pandas as pd

# Read data from CSV
data = pd.read_csv("sample_data.csv")

# Calculate basic stats
average_score = data["Score"].mean()
max_score = data["Score"].max()
min_score = data["Score"].min()

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Simple Automated Report", ln=True, align='C')
pdf.ln(10)  # Add space

# Add summary
pdf.cell(200, 10, txt=f"Average Score: {average_score:.2f}", ln=True)
pdf.cell(200, 10, txt=f"Maximum Score: {max_score}", ln=True)
pdf.cell(200, 10, txt=f"Minimum Score: {min_score}", ln=True)

pdf.output("simple_report.pdf")

print("Report generated successfully: simple_report.pdf")
