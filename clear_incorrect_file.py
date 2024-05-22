import os

filenames = os.listdir("./easyocr_text_train_images")

for filename in filenames:
    print(filename)
    for char in filename[2:]:
        if (char in "123456789"):
            print("Removed " + filename)
            os.remove("easyocr_text_train_images/" + filename)
            break