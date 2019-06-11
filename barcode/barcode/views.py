from django.http import HttpResponse
def barcode(request):
    #instantiate a drawing object
    from . import mybarcode
    d = mybarcode.MyBarcodeDrawing("My Name is Jain")
    binaryStuff = d.asString('gif')
    return HttpResponse(binaryStuff, 'image/gif')
