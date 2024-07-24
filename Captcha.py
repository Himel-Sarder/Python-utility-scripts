from captcha.image import ImageCaptcha
import random
import string

# Generate random text for CAPTCHA
def generate_captcha_text(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Create CAPTCHA image
def generate_captcha_image(captcha_text):
    image = ImageCaptcha()
    captcha_image = image.generate_image(captcha_text)
    return captcha_image

# Save CAPTCHA image
def save_captcha_image(captcha_image, file_path):
    captcha_image.save(file_path)

# Main function
if __name__ == "__main__":
    captcha_text = generate_captcha_text()
    captcha_image = generate_captcha_image(captcha_text)
    save_captcha_image(captcha_image, "captcha.png")
    print(f"CAPTCHA text: {captcha_text}")
    print("CAPTCHA image saved as 'captcha.png'")
