import fitz
import tempfile
import base64
import os
from flask import Flask, request
from flask.views import MethodView
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


class PdfAPI(MethodView):
    def get(self):
        return "OK"

    def post(self):
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
            f.write(request.data)

        response = {
            "images": []
        }
        doc = fitz.open(f.name)
        for i in range(len(doc)):
            for img in doc.getPageImageList(i):
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)
                picture = pix.tobytes()
                b64_picture = base64.b64encode(picture)
                response['images'].append(b64_picture.decode())
        os.remove(f.name)
        return response


app.add_url_rule('/api/pdf/', view_func=PdfAPI.as_view('pdf'))

if __name__ == '__main__':
    app.run()
