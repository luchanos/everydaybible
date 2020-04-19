from PIL import Image, ImageFont, ImageDraw


def jesus_quote_image(top, bottom='Иисус Христос'):
    image = Image.open('./images/quotepic.jpg')
    draw = ImageDraw.Draw(image)

    band_name_font = ImageFont.truetype(font='./OpenSans-ExtraBold.ttf', size=25)
    album_name_font = ImageFont.truetype(font='./OpenSans-ExtraBold.ttf', size=25)

    band_x, band_y = 50, 50
    album_x, album_y = 50, 400

    outline_color = "black"
    draw.text((band_x-1, band_y-1), top, font=band_name_font, fill=outline_color)
    draw.text((band_x+1, band_y-1), top, font=band_name_font, fill=outline_color)
    draw.text((band_x-1, band_y+1), top, font=band_name_font, fill=outline_color)
    draw.text((band_x+1, band_y+1), top, font=band_name_font, fill=outline_color)
    draw.text((album_x-1, album_y-1), bottom, font=album_name_font, fill=outline_color)
    draw.text((album_x+1, album_y-1), bottom, font=album_name_font, fill=outline_color)
    draw.text((album_x-1, album_y+1), bottom, font=album_name_font, fill=outline_color)
    draw.text((album_x+1, album_y+1), bottom, font=album_name_font, fill=outline_color)

    draw.text((band_x, band_y), top, (255, 255, 255), font=band_name_font)
    draw.text((album_x, album_y), bottom, (255, 255, 255), font=album_name_font)

    return image
