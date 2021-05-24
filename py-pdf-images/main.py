import fitz

from flask import Flask, request
from flask.views import MethodView

app = Flask(__name__)


class PdfAPI(MethodView):

    def get(self):
        return "Hello World"

    def post(self):

        doc = fitz.open("file.pdf")
        for i in range(len(doc)):
            for img in doc.getPageImageList(i):
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)
                if pix.n < 5:       # this is GRAY or RGB
                    pix.writePNG("p%s-%s.png" % (i, xref))
                else:               # CMYK: convert to RGB first
                    pix1 = fitz.Pixmap(fitz.csRGB, pix)
                    pix1.writePNG("p%s-%s.png" % (i, xref))
                    pix1 = None
                pix = None

        return True


app.add_url_rule('/api/pdf', view_func=PdfAPI.as_view('pdf'))

if __name__ == '__main__':
    app.run()
