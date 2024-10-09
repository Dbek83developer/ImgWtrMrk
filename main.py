from PIL import Image as img
from PIL import ImageDraw
from PIL import ImageFont
from tkinter import *
from tkinter import ttk

# with img.open("photo.JPG") as img:
#     img.show()


def watermark_text(input_image_path,
                   output_image_path,
                   text, pos):
    photo = img.open(input_image_path)
    # make the image editable
    drawing = ImageDraw.Draw(photo)
    black = (3, 8, 12)
    font = ImageFont.truetype("arial.ttf", 150)
    drawing.text(pos, text, fill=black, font=font)
    photo.show()
    photo.save(output_image_path)


def watermark_photo(input_image_path,
                    output_image_path,
                    watermark_image_path,
                    position):
    base_image = img.open(input_image_path)
    watermark = img.open(watermark_image_path)
    # add watermark to your image
    base_image.paste(watermark, position)
    base_image.show()
    base_image.save(output_image_path)


def watermark_with_transparency(input_image_path,
                                output_image_path,
                                watermark_image_path,
                                position):
    base_image = img.open(input_image_path)
    watermark = img.open(watermark_image_path)
    width, height = base_image.size
    transparent = img.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.show()
    transparent.save(output_image_path)


def watermark_with_transparency2(input_image_path, output_image_path, watermark_image_path, position):
    # Open the original image
    base_image = img.open(input_image_path).convert("RGBA")

    # Open the watermark image
    watermark = img.open(watermark_image_path).convert("RGBA")

    # Create a new image for the result
    transparent = img.new('RGBA', base_image.size, (0, 0, 0, 0))

    # Paste the base image on the transparent background
    transparent.paste(base_image, (0, 0))

    # Ensure the watermark has an alpha channel for transparency
    if watermark.mode != 'RGBA':
        watermark = watermark.convert('RGBA')

    # Extract the alpha channel as the mask
    mask = watermark.split()[3]

    # Paste the watermark image on the transparent background
    transparent.paste(watermark, position, mask=mask)

    # Save the result
    transparent = transparent.convert('RGB')  # Convert back to 'RGB' to save in JPG format
    transparent.save(output_image_path, 'JPEG')


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
#watermark_text('photo.JPG', 'photo_watermarked.jpg', text='dbek.developer', pos=(0, 0))
watermark_with_transparency2('photo.JPG', 'photo_watermarked_tr.jpg', 'dbek-logo.png', position=(0, 0))
root.mainloop()
