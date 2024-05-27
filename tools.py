import os
from pythainlp.spell import correct
import cv2
import pytesseract
import easyocr
from PIL import Image, ImageGrab
import matplotlib.pyplot as plt

def correct_file_name(folder_path):
    filenames = os.listdir(folder_path)
    for file in filenames:
        name_list = file.split("_")
        try:
            real_name = name_list[1]
            real_name = real_name.split(".")[0]
            print(real_name[0])
            if (real_name[0] == 'แ'):
                real_name = "แทน"
            if (real_name[0] == 'ข'):
                real_name = "ขาว"
            if (real_name[0] == 'ด'):
                real_name = "ดำ"
            if (real_name[0] == 'ค'):
                real_name = "ครีม"
            if (real_name[0] == 'ะ' and real_name[1] == 'ะ'):
                real_name = "กะปิ"
            if (real_name[0] == 'ก' and real_name[1] == 'า'):
                real_name = "กากี"
            corrected_file_name = correct(real_name)
            print(corrected_file_name)
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path, corrected_file_name + ".png"))
        except:
            print("Error")



COLOR_DICT = ["โอรส", "เบจ", "ดำ", "ฟ้า", "ครีม", "ครีมสลับขาว", "ทอง", "เขียว", "เทา", "กากี", "กะปิ", "ขี้ม้า", "กลม", "นาค", "นูด", "นู๊ต", "ส้ม", "ชมพู", "ม่วง", "แดง", "เงิน", "แทน", "ตาล", "ขาว", "ขาวสลับดำ", "เหลืิิอง"]

def read_image_text(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #display_image_from_array(gray_image)
    threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(threshold_image, lang='tha', config='--psm 6')
    return text

def display_image_from_array(image_array):
    displayed_image = Image.fromarray(image_array)
    displayed_image.show()

def easy_ocr(image_path, output_path="", render=False, output=False):
    reader = easyocr.Reader(['th'])
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)
    image = cv2.fastNlMeansDenoising(image, None, 30, 7, 21)
    transformed_image = cv2.equalizeHist(image)
    results = reader.readtext(transformed_image)
    for index, result in enumerate(results):
        # print(result[1])
        print("Color found:", result[1])
        if(render == True):
            render_bouding_box(result[0], image_path, output_path, index)
    if (output == True):
        return results
    
def easy_ocr_text(image_path):
    reader = easyocr.Reader(['th'])
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)
    image = cv2.fastNlMeansDenoising(image, None, 30, 7, 21)
    transformed_image = cv2.equalizeHist(image)
    results = reader.readtext(transformed_image)
    coordinate = []
    for index, result in enumerate(results):
        coordinate.append(result[0])
    return coordinate

def tesseract(image_path, output_path="", render=False, output=False):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(threshold_image, lang='tha')
    if (render == True):
        render_bouding_box(text, image_path, output_path)
    if (output == True):
        return text

def render_bouding_box(coordinates, input_path, output_path, index):
    image = cv2.imread(input_path)
    if (index > 0):
        image = cv2.imread(output_path)
    for i in range (len(coordinates)):
        start_point = (int(coordinates[i][0]), int(coordinates[i][1]))
        print(start_point)
        end_point = (int(coordinates[(i + 1) % len(coordinates)][0]), int(coordinates[(i + 1) % len(coordinates)][1]))
        color = (0, 0, 0)
        thickness = 2
        cv2.line(image, start_point, end_point, color, thickness)
    cv2.imwrite(output_path, image)

def estimate_text_location_and_size(top_left, top_right, bottom_left, bottom_right):
    horizontal_location = (top_right[0] - bottom_left[0]) /2 + bottom_left[0]
    vertical_location = (bottom_right[1] - top_left[1]) / 2 + top_left[1]
    width = top_right[0] - top_left[0]
    height = bottom_right[1] - top_right[1]
    return (horizontal_location, vertical_location, width, height)


def screenshot_specific_area(coordinate, image_path, output_path):
    image = Image.open(image_path)
    print(coordinate)
    left, right, bottom, top = coordinate[0][0], coordinate[2][0], coordinate[2][1], coordinate[0][1]
    if (bottom < top):
        return
    if (right < left):
        return
    crop_image = image.crop((left, top, right, bottom))
    crop_image.save(output_path)


def clear_incorrect_file(file_name):
    print(file_name)
    for char in file_name[2:]:
        if (char in "123456789"):
            print("Removed " + file_name)
            os.remove("easyocr_text_train_images/" +  file_name)
            break

def move_all_files_in_folder(original_folder, destination_folder):
    file_names = os.listdir(original_folder)
    for file_name in file_names:
        os.rename(os.path.join(original_folder, file_name), os.path.join(destination_folder, file_name))


if __name__ == "__main__":
    correct_file_name("easyocr_text_train_images")