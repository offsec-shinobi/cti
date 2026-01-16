import mmh3
import codecs

# Assuming the favicon file is named 'favicon.ico' in the same directory
# You might need to adjust the file path if your file is located elsewhere
try:
    with open('vite.svg', 'rb') as f:
        favicon_content = f.read()
    favicon_base64 = codecs.encode(favicon_content, "base64")
    favicon_hash = mmh3.hash(favicon_base64)
    print(favicon_hash)
except FileNotFoundError:
    print("Error: favicon.ico not found. Please make sure the file is in the correct directory.")
except Exception as e:
    print(f"An error occurred: {e}")
