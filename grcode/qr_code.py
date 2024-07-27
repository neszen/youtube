import qrcode

url = "https://www.youtube.com/@Neszen/shorts"

image = qrcode.make(url)

image.save('qr.png')

