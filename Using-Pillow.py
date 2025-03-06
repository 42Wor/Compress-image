from PIL import Image

def compress_image_pillow(input_path, output_path, quality=85, optimize=True, format=None):
    """Compresses an image using Pillow.

    Args:
        input_path: Path to the input image file.
        output_path: Path to save the compressed image.
        quality: Compression quality (0-100, where 100 is the best quality and worst compression, and 0 is the worst quality and best compression).  A good starting point is 85.
        optimize:  If True, Pillow will attempt to further reduce the file size by examining the image. This can be slower, but may improve compression.
        format:  The output format (e.g., "JPEG", "PNG", "WEBP").  If None, Pillow will attempt to infer the format from the output_path extension.  If that fails, or you want to change the format, you need to specify it.
    """
    try:
        img = Image.open(input_path)

        # Handle different image modes (RGBA, etc.)
        if img.mode in ("RGBA", "P"):  # Handle transparency. "P" is for paletted images.
            img = img.convert("RGB") # Convert to RGB for JPEG, or preserve for PNG

        img.save(output_path, quality=quality, optimize=optimize, format=format)
        return True

    except FileNotFoundError:
        print(f"Error: File not found at {input_path}")
        return False
    except OSError as e:
        print(f"Error: Could not open or save image: {e}")  # More specific OSError
        return False
    except Exception as e:  # Catch other potential exceptions
        print(f"An unexpected error occurred: {e}")
        return False



# Example Usage:
input_image = "Assets/years.png"  # Replace with your image file
output_image = "output/{input_image}"


compress_image_pillow(input_image, output_image, quality=75, optimize=True)  # Compress to JPEG, good balance
compress_image_pillow(input_image, output_image, quality=80, format="WEBP") # Compress to WebP (often better compression than JPEG)
compress_image_pillow(input_image, output_image, quality=90)   # Compress PNG (lossless, quality parameter controls zlib compression level)
# For PNG, use the compress_level parameter (0-9),  where 9 is maximum compression.  Quality is ignored for lossless formats like PNG
#  img.save(output_path, compress_level=9) # For maximum PNG compression