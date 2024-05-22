import os
import tools

input_path = "shoes_color.v4i.yolov8/train/images"
output_path = "text_train_images"

def main():
    filenames = os.listdir(input_path)
    for filename in filenames:
        coordinates = tools.easy_ocr_text(os.path.join(input_path, filename))
        for coordinate in coordinates:
            for i in range(len(coordinate)):
                coordinate[i] = (int(coordinate[i][0]), int(coordinate[i][1]))
            coordinate = tuple(coordinate)
            tools.screenshot_specific_area(coordinate, os.path.join(input_path, filename), os.path.join(output_path, filename))


if __name__ ==  "__main__":
    main()