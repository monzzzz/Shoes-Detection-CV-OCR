import os
import tools

label_cropped_images_path = "./text_train_images"

def main():
    filenames = os.listdir(label_cropped_images_path)
    index = 0
    for filename in filenames:
        # results = tools.easy_ocr(os.path.join(label_cropped_images_path, filename), output=True)
        results = tools.tesseract(os.path.join(label_cropped_images_path, filename), output=True)
        if (results == [] or results == None):
            continue
        print(results)
        index += 1
        if (index == 50):
            break
        # os.rename(os.path.join(label_cropped_images_path, filename), os.path.join(label_cropped_images_path, str(index) + "_" + results + ".jpg" ))
if __name__ == "__main__":
    main()