import cv2
img = None  
msg = ""  
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}
def encrypt_message(message, password_input):
    global img, msg
    img = cv2.imread("bougainvillea.jpg")  
    if img is None:
        print("Error: Could not load image.")
        return
    max_message_length = img.shape[0] * img.shape[1] * 3
    if len(message) > max_message_length:
        print(f"Error: Message is too long. Maximum allowed length is {max_message_length} characters.")
        return
    msg = message
    with open("password.txt", "w") as f:
        f.write(password_input)
    
    with open("message.txt", "w") as f:
        f.write(msg)
    n, m, z = 0, 0, 0
    for char in msg:
        img[n, m, z] = d[char]  
        n += 1
        m += 1
        z = (z + 1) % 3  
    cv2.imwrite("encryptedImage.png", img)
    print("Encryption complete. Encrypted image saved as 'encryptedImage.png'.")
    print("Message have been saved for decryption.")
if __name__ == "__main__":
    message = input("Enter secret message: ")
    password_input = input("Enter a passcode: ")
    encrypt_message(message, password_input)
