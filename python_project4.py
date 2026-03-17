#qr code generator

import QRCode
data = "https://www.youtube.com/channel/UCWv7vMbMWH4-V0ZXdmDpPBA"
qr = QRCode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")
