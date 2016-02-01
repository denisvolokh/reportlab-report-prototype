from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, Table
from reportlab.lib.colors import PCMYKColor, HexColor
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin, Rect
from reportlab.graphics import renderPDF

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

        headerCanvas = Drawing()
        headerRect = Rect(0, 0, width=self.width, height=50)
        headerRect.fillColor = HexColor("#607D8B")
        headerRect.strokeColor = HexColor("#607D8B")
        headerCanvas.add(headerRect)
        renderPDF.draw(headerCanvas, self.c, 0, self.height - 50)

        p = Paragraph("Kit Trading Fund Report", style=self.styles["Heading1"])
        p.wrapOn(self.c, self.width, self.height - 50)
        p.drawOn(self.c, *self.coord(75, 10, mm))

        p = Paragraph("Monthly Report: January 2016", style=self.styles["Heading4"])
        p.wrapOn(self.c, self.width, self.height - 50)
        p.drawOn(self.c, *self.coord(85, 16, mm))

    def create_header(self, text):
        pass

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