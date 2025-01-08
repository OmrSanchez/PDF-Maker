from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")


for index, row in df.iterrows():
		#Generate Master pages
		pdf.add_page()

		# Set the header
		pdf.set_font("Times", size=24, style="B")
		pdf.set_text_color(100, 100, 100)
		pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
		pdf.line(x1=10, y1=21, x2=200, y2=21)

		# Create PDF lines
		y_one, y_two = 21, 21
		for y in range(28):
			y_one += 10
			y_two += 10
			pdf.line(x1=10, y1=y_one, x2=200, y2=y_two)
		# Set the footer
		pdf.ln(266)

		pdf.set_font("Times", size=8, style="I")
		pdf.set_text_color(180, 180, 180)
		pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)

		# Child page code
		for i in range(row["Pages"] - 1):
			pdf.add_page()

			# Create PDF lines
			y_one, y_two = 11, 11
			pdf.line(x1=10, y1=y_one, x2=200, y2=y_two)
			for y in range(28):
				y_one += 10
				y_two += 10
				pdf.line(x1=10, y1=y_one, x2=200, y2=y_two)

			# Set the footer
			pdf.ln(278)

			pdf.set_font("Times", size=8, style="I")
			pdf.set_text_color(180, 180, 180)
			pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)


pdf.output("output.pdf")