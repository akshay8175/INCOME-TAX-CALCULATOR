import reportlab
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.platypus import Paragraph
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from PyQt5.QtWidgets import *
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet

def save(self):
	options = QFileDialog.Options()
	path, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()","","pdf Docdument (*.pdf)", options=options)
    
	print(path)
	if path.endswith('.pdf'):
		return path

	elif path=="" :
		return 'newpdf.pdf'

	else:
		path=str(path)+('.pdf')
		return path


def pdfw(self, data):
	filename=str(save(self))
	styles=getSampleStyleSheet()
	style=styles["BodyText"]
	style.alignment=TA_CENTER

	pdf=Canvas(filename,pagesize=letter)
	header=Paragraph("<bold><font size=18><center>Income Tax Calculater</center></font></bold>",style)

	table=Table(data)

	style=TableStyle([('BACKGROUND',(0,0),(6,0),colors.green),
		('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
		('ALIGN',(0,0),(-1,-1),'CENTER'),
		('FONTSIZE',(0,0),(-1,0),13)
		])

	table.setStyle(style)

	rowNumb=len(data)
	
	for i in range(1,rowNumb):
		if i%2==0:
			bc=colors.burlywood
		else:
			bc=colors.beige

		ts=TableStyle([('BACKGROUND',(0,i),(-1,i),bc)])
		table.setStyle(ts)

	aW=540
	aH=720
	w,h=header.wrap(aW,aH)
	header.drawOn(pdf,72,aH)
	aH=aH-h
	w,h=table.wrap(aW,aH)
	table.drawOn(pdf,72,aH-h)
	pdf.save()


def pdfo(self, data):
	
	filename=str(save(self))
	styles=getSampleStyleSheet()
	style=styles["BodyText"]
	style.alignment=TA_CENTER

	pdf=Canvas(filename,pagesize=letter)
	header=Paragraph("<bold><font size=18>Income Tax Calculater</font></bold>",style)

	table=Table(data)

	aW=540
	aH=720
	w,h=header.wrap(aW,aH)
	header.drawOn(pdf,72,aH)
	aH=aH-h
	w,h=table.wrap(aW,aH)
	table.drawOn(pdf,72,aH-h)
	pdf.save()

