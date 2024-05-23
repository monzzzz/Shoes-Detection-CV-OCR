import os
from PIL import Image, ImageFont, ImageDraw
import random
import argparse

# get the second column from the txt file
def get_text_from_tha_file():
    input_path = 'dataset/tha_community_2021.txt'
    output_path = 'datasets/tha_dataset.txt'
    with open(input_path, 'r') as file:
        lines = file.readlines()
        lists = []
        for line in lines:
            list = line.split('\t')
            lists.append(list)
        with open(output_path, 'w') as output_file:
            for list in lists:
                output_file.write(list[1] + '\n')
# generate with pillow image

def generate_images_with_pillow(file_path, output_folder_path, font_path, text_file_path, amount):
    with open(file_path, "r") as read_file:
        lines = read_file.readlines()
        index = 0
        random.shuffle(lines)
        # shuffle the line
        clean_text_file(text_file_path)
        for line in lines:
            image_width, image_height = 1000, 100
            image = Image.new('RGB', (image_width, image_height), color="white")
            draw = ImageDraw.Draw(image) 
            font = ImageFont.truetype(font_path, 30)
            draw.text((30, 30), line, font=font, fill=(0,0,0))
            if (line.rstrip('\n') == '.' or line.rstrip('\n') == '/' ):
                print(True)
                continue
            try:
                image.save(os.path.join(output_folder_path, line.rstrip('\n') + ".png"))
                write_path_on_text_file(text_file_path, os.path.join("test/", line.rstrip('\n') + ".png"), line.rstrip('\n'))
                index += 1
                if (index >= amount):
                    break
            except:
                print("error")


def write_path_on_text_file(text_file_path, file_path, label):
    with open(text_file_path, 'a') as text_file:
        text_file.write(file_path + '\t' + label + '\n')

def clean_text_file(text_file_path):
    with open(text_file_path, 'w') as text_file:
        text_file.write('')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--func", type=str, default="train", help="train or val")   
    args = parser.parse_args()
    input_path = "datasets/tha_dataset.txt"
    output_folder_path = "formatted_data/train/test"
    text_file_path = "formatted_data/train/gt.txt"
    pattaya_font_path = "fonts/Pattaya/Pattaya-Regular.ttf"
    # ayutthaya_font_path = "fonts/Ayutthaya/Ayutthaya/Ayutthaya.ttf"
    data_amount = 1000
    if (args.func == "train"):
        output_folder_path = "formatted_data/train/test"
        text_file_path = "formatted_data/train/gt.txt"
        data_amount = 800
    if (args.func == "val"):
        output_folder_path = "formatted_data/val/test"
        text_file_path = "formatted_data/val/gt.txt"
        data_amount = 200
    # generate_images_with_pillow(input_path, output_folder_path, pattaya_font_path)
    generate_images_with_pillow(input_path, output_folder_path , pattaya_font_path, text_file_path, data_amount)


if __name__ == "__main__":
    main()

# python create_lmdb_dataset.py --inputPath formatted_data/train/ --gtFile train/gt.txt --outputPath lmdb/train_lmdb/
# python create_lmdb_dataset.py --inputPath formatted_data/val/ --gtFile val/gt.txt --outputPath lmdb/val_lmdb/

# train command
""" CUDA_VISIBLE_DEVICES=0 python train.py \
--train_data train_lmdb --valid_data val_lmdb \
--select_data MJ-ST --batch_ratio 0.5-0.5 \
--Transformation None --FeatureExtraction VGG --SequenceModeling BiLSTM --Prediction CTC
"""
#
#
#

# generate with synthtiger



# list of fonts
# pattaya font
# ayutthaya font