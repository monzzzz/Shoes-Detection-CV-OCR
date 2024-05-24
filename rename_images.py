import os
import tools
import easy_ocr

label_cropped_images_path = "./text_train_images"

def main():
    filenames = os.listdir(label_cropped_images_path)
    index = 0
    for filename in filenames:
        # results = tools.easy_ocr(os.path.join(label_cropped_images_path, filename), output=True)
        results = tools.easy_ocr(os.path.join(label_cropped_images_path, filename), output=True)
        if (results == [] or results == None):
            continue
        results = results[0][1]
        index += 1
        if (index == 50):
            break
        os.rename(os.path.join(label_cropped_images_path, filename), os.path.join(label_cropped_images_path, str(index) + "_" + results + ".png" ))
if __name__ == "__main__":
    main()