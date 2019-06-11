from django.http import HttpResponse

def return_qr(request):
    text = 'Hello Sir'
    student_qr = generate_qr_code(text)
    response = HttpResponse(content_type="image/jpeg")
    student_qr.save(response, "JPEG")
    return response

def generate_qr_code(data):
	import qrcode
	import qrcode.image.svg
	from PIL import Image

	student_qr = qrcode.make(data)
	student_qr = student_qr.resize([250, 250])
	return student_qr
