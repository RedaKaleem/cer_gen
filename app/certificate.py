from PIL import Image, ImageDraw, ImageFont

def generate_certificate(name, event, template_path, output_path):
    template = Image.open(template_path)
    draw = ImageDraw.Draw(template)

    # Load a custom font
    font = ImageFont.truetype("arial.ttf", size=50)

    # Add text to the template
    draw.text((400, 300), f"Name: {name}", fill="black", font=font)
    draw.text((400, 400), f"Event: {event}", fill="black", font=font)

    # Save the generated certificate
    template.save(output_path)