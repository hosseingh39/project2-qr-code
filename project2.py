
import qrcode

message = "تبریک شما برنده شدید 🎉🏆"

qr = qrcode.make(message)

qr.save("my_qrcode.png")

print("QR code ba movafaghiat sakhte shod")
