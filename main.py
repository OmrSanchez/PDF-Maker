from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")


for index, row in df.iterrows():
	for i in range(row["Pages"]):
		pdf.add_page()

		# Set the header
		pdf.set_font("Times", size=24, style="B")
		pdf.set_text_color(100, 100, 100)
		pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
		pdf.line(x1=10, y1=21, x2=200, y2=21)

		# Set the footer
		pdf.ln(265)

		pdf.set_font("Times", size=8, style="I")
		pdf.set_text_color(180, 180, 180)
		pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)
pdf.output("output.pdf")