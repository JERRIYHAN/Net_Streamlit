from PIL import Image, ImageFilter, ImageOps, ImageDraw, ImageFont

# Load the image again
image = Image.open(r"/Users/jiaaijiajiazhangshi/Downloads/IMG_3783.JPG")

# Convert to grayscale
image_bw = image.convert("L")

# Apply edge detection filter
image_edges = image_bw.filter(ImageFilter.FIND_EDGES)

# Invert colors for a more striking black and white effect
image_inverted = ImageOps.invert(image_edges)

# Apply a threshold to create a high-contrast image
threshold = 128
image_contrast = image_inverted.point(lambda p: p > threshold and 255)

# Add text in a similar style to the provided image
draw = ImageDraw.Draw(image_contrast)
font = ImageFont.load_default()  # Use default font for simplicity

# Adding the text
text = "dream on\nlittle dreamer"
text_position = (image_contrast.width // 2, image_contrast.height // 10)
draw.text(text_position, text, fill=0, font=font, anchor="mm")

# Save and show the image
image_contrast.show()
