import tools
import os
from pathlib import Path

directory_folder_path = "./shoes_color.v4i.yolov8/train/images"
rendered_folder_path = "./labeled_images"


file_name_in_folder = os.listdir(directory_folder_path)

def main():
    index = 0
    for filename in file_name_in_folder:
        file_path = Path(filename)
        print("image: " + str(index + 1) + " " + filename)
        if (index == 10):
            break
        tools.easy_ocr(os.path.join(directory_folder_path, filename), output_path=os.path.join(rendered_folder_path, file_path.stem + "_rendered.png"), render=True)
        print("\n")
        index+=1


if __name__ == "__main__":
    main()