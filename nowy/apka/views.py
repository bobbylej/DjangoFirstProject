# _*_ coding: utf-8 _*_
from django.http import HttpResponse

def main_page(request):
    output = '''
      <html>
        <head><title>%s</title></head>
        <body>
          <h3>%s</h3>
          <p>%s</p>
        </body>
      </html>
    ''' % ('Strona startowa','Witamy :)','Wszystko działa')
    return HttpResponse(output)
