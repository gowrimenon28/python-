import qrcode

features=qrcode.QRCode(version=1,box_size=40,border=3)

features.add_data("https://www.youtube.com/watch?v=-GmJLI122ZM")
features.make(fit=True)
generate_image=features.make_image(fill_color="black",back_color="blue")
generate_image.save("image.png")
