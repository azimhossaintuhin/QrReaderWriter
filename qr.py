# All the pckage
import qrcode
import cv2
import os
import random
from pyfiglet import figlet_format
from tkinter import filedialog

# Getting Input For User Need
res = figlet_format("Qr Writer Reader", font='5lineoblique')
print(res)
print("*********************************** \n** For creating QrCode Type 'qc' ** \n** For reading QrCode type 'qr'  **\n*********************************** ")

user_input = input("What Do You Want: ")
# Enter The Text That You Want To Incode To qrcode

# qrcode file creator function


def create_qr(data, fileName):
    numbr = "0123456789"
    img = qrcode.make(data)
    if os.path.exists(f'{fileName}.png'):
        random_number = "".join(random.sample(numbr,2))
        img.save(f'{fileName}-{random_number}.png')
        print(f'"{fileName}-{random_number}".png is saved in your "{os.getcwd()}"')
    else:
        img.save(f"{fileName}.png")
        print(f'"{fileName}.png" is saved in your "{os.getcwd()}"')


# reading the qrcod
def read_qr_code(filename):
    try:
        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        value, point, straight_qrcode = detect.detectAndDecode(img)
        return value
    except Exception as e:
        return (e)


if user_input == 'qc':
    data = input("Enter the Text you want to incdoe: ")
    fileName = input("Enter name of your qrcode file: ")
    create_qr(data, fileName)
elif user_input == 'qr':
    filename = filedialog.askopenfilename()
    print(read_qr_code(filename))
