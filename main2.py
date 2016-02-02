from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, Table, TableStyle
from reportlab.lib.colors import PCMYKColor, HexColor
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin, Rect
from reportlab.graphics import renderPDF
from reportlab.lib.styles import ParagraphStyle

from reportlab.lib.colors import (
    black,
    purple,
    white,
    yellow
)

########################################################################
class LetterMaker(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, pdf_file, org, seconds):
        self.c = canvas.Canvas(pdf_file, pagesize=letter)
        self.width, self.height = self.c._pagesize
        self.styles = getSampleStyleSheet()
 
 
    #----------------------------------------------------------------------
    def createDocument(self):

        self.create_header()

        self.create_summary_header()

        self.create_summary_table()

        self.create_risk_header()

        self.create_risk_table()

        self.create_performance_chart_header()


    def create_risk_table(self):
        _width = self.width / 2 - 10
        _height = 100

        data = [
            ["Risk Exposure", "Lowest", "Highest", "Average"],
            ["Delta", "-2.5%", "9.0%", "5.03%"],
            ["Gamm", "-2.5%", "9.0%", "5.03%"],
            ["Theta (Monthly)", "-2.5%", "9.0%", "5.03%"],
            ["Vega", "-2.5%", "9.0%", "5.03%"],
            ["Rho", "-2.5%", "9.0%", "5.03%"]
        ]
        table = Table(data, colWidths = .9 * inch)
        table.setStyle([("ALIGN", (1,0), (-1,-1), "RIGHT")])
        table.setStyle([("LINEABOVE", (0,1), (-1,1), .25, black)])
        # table.setStyle([("BOX", (0,0), (-1,-1), 0.25, black)])
        table.wrapOn(self.c, _width + 20, _height)
        table.drawOn(self.c, *self.coord(115, 65, mm))

    def create_summary_table(self):
        _width = self.width / 2 - 10
        _height = 100

        data = [
            ["December", "-1.05%"],
            ["Since inception", "+77.43%"],
            ["Annualized Return", "+10.65%"],
            ["Net Asset Value", "117.05%"],
            ["NAV per Share", "US$ 17.743"],
            ["Fund AUM", "US$ 17`743m"],
        ]
        table = Table(data, colWidths = 1.75 * inch)
        table.setStyle([("ALIGN", (1,0), (-1,-1), "RIGHT")])
        # table.setStyle([("BOX", (0,0), (-1,-1), 0.25, black)])
        table.wrapOn(self.c, _width, _height)
        table.drawOn(self.c, *self.coord(5, 65, mm))


    def create_summary_header(self):
        _width = self.width / 2 - 10
        _height = 20
        headerCanvas = Drawing()
        headerRect = Rect(0, 0, width = _width, height = _height)
        headerRect.fillColor = HexColor("#607D8B")
        headerRect.strokeColor = HexColor("#607D8B")
        headerCanvas.add(headerRect)
        renderPDF.draw(headerCanvas, self.c, 0, self.height - 75)

        _summary_styles = ParagraphStyle(
            "SUMMARY",
            parent=self.styles["Heading5"],
            textColor=white,
            fontName='Helvetica'
        )
        p = Paragraph("SUMMARY", style = _summary_styles)
        p.wrapOn(self.c, _width, _height)
        p.drawOn(self.c, *self.coord(4, 25, mm))

    def create_risk_header(self):
        _width = self.width / 2 - 10
        _height = 20
        headerCanvas = Drawing()
        headerRect = Rect(0, 0, width = _width, height = _height)
        headerRect.fillColor = HexColor("#607D8B")
        headerRect.strokeColor = HexColor("#607D8B")
        headerCanvas.add(headerRect)
        renderPDF.draw(headerCanvas, self.c, x = _width + 20, y = self.height - 75)

        _summary_styles = ParagraphStyle(
            "RISKS",
            parent=self.styles["Heading5"],
            textColor=white,
            fontName='Helvetica'
        )
        p = Paragraph("RISKS", style = _summary_styles)
        p.wrapOn(self.c, _width, _height)
        p.drawOn(self.c, *self.coord(115, 25, mm))

    def create_performance_chart_header(self):
        _width = self.width
        _height = 20
        headerCanvas = Drawing()
        headerRect = Rect(0, 0, width = _width, height = _height)
        headerRect.fillColor = HexColor("#607D8B")
        headerRect.strokeColor = HexColor("#607D8B")
        headerCanvas.add(headerRect)
        renderPDF.draw(headerCanvas, self.c, 0, self.height - 217)

        _summary_styles = ParagraphStyle(
            "PERFORMANCE CHART",
            parent=self.styles["Heading5"],
            textColor=white,
            fontName='Helvetica'
        )
        p = Paragraph("PERFORMANCE", style = _summary_styles)
        p.wrapOn(self.c, _width, _height)
        p.drawOn(self.c, *self.coord(4, 75, mm))

    def create_header(self):
        headerCanvas = Drawing()
        headerRect = Rect(0, 0, width=self.width, height=50)
        headerRect.fillColor = HexColor("#607D8B")
        headerRect.strokeColor = HexColor("#607D8B")
        headerCanvas.add(headerRect)
        renderPDF.draw(headerCanvas, self.c, 0, self.height - 50)

        _header_styles = ParagraphStyle(
            "Header",
            parent=self.styles["Heading1"],
            textColor=white,
            fontName='Helvetica'
        )
        p = Paragraph("Kit Trading Fund Report", style = _header_styles)

        p.wrapOn(self.c, self.width, self.height - 50)
        p.drawOn(self.c, *self.coord(75, 10, mm))

        _sub_header_styles = ParagraphStyle(
            "SubHeader",
            parent=self.styles["Heading4"],
            textColor=white,
            fontName='Helvetica'
        )
        p = Paragraph("Monthly Report: January 2016", style = _sub_header_styles)
        p.wrapOn(self.c, self.width, self.height - 50)
        p.drawOn(self.c, *self.coord(85, 16, mm))

    #----------------------------------------------------------------------
    def coord(self, x, y, unit=1):
        """
        # http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
        Helper class to help position flowables in Canvas objects
        """
        x, y = x * unit, self.height -  y * unit
        return x, y    
 
    #----------------------------------------------------------------------
    def createParagraph(self, ptext, x, y, style=None):
        """"""
        if not style:
            style = self.styles["Normal"]
        p = Paragraph(ptext, style=style)
        p.wrapOn(self.c, self.width, self.height)
        p.drawOn(self.c, *self.coord(x, y, mm))
 
    #----------------------------------------------------------------------
    def savePDF(self):
        """"""
        self.c.save()   
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    doc = LetterMaker("report2.pdf", "The MVP", 10)
    doc.createDocument()
    doc.savePDF()