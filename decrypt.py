import cv2
message = ""
n, m, z = 0, 0, 0
c = {i: chr(i) for i in range(255)}

def get_password():
    try:
        with open("password.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        print("Error: Password file not found. Encryption might not have been performed.")
        return None

def get_encrypted_message():
    try:
        with open("message.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        print("Error: Message file not found. Encryption might not have been performed.")
        return None
img = cv2.imread("encryptedImage.png")
if img is None:
    print("Error: Could not load encrypted image.")
    exit()
pas = input("Enter passcode for Decryption: ")
stored_password = get_password()
if stored_password is None:
    exit()
encrypted_message = get_encrypted_message()
if encrypted_message is None:
    exit()
if stored_password == pas:
    for i in range(len(encrypted_message)):  
        if n >= img.shape[0] or m >= img.shape[1]:
            print("Error: Pixel coordinates out of bounds.")
            break
        
        pixel_value = img[n, m, z]
        message += c[pixel_value]  
        n += 1
        m += 1
        z = (z + 1) % 3
    
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT authorized")
