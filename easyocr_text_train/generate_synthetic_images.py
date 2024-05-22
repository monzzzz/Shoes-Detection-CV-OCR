import os
from PIL import Image, ImageFont, ImageDraw


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


def generate_images_with_pillow(file_path, output_folder_path, font_path, text_file_path):
    with open(file_path, "r") as read_file:
        lines = read_file.readlines()
        index = 0
        # shuffle the line
        for line in lines:
            image_width, image_height = 1000, 100
            image = Image.new('RGB', (image_width, image_height), color="white")
            draw = ImageDraw.Draw(image) 
            font = ImageFont.truetype(font_path, 30)
            draw.text((30, 30), line, font=font, fill=(0,0,0))
            if (line.rstrip('\n') == '.' or line.rstrip('\n') == '/' ):
                print(True)
                continue
            image.save(os.path.join(output_folder_path, line.rstrip('\n') + ".png"))
            write_path_on_text_file(text_file_path, os.path.join(output_folder_path, line.rstrip('\n') + ".png"), line.rstrip('\n'))
            index += 1
            if (index > 1000):
                break


def write_path_on_text_file(text_file_path, file_path, label):
    with open(text_file_path, 'a') as text_file:
        text_file.write(file_path + '\t' + label + '\n')



def main():
    input_path = "datasets/tha_dataset.txt"
    output_folder_path = "pillow_images_generated"
    pattaya_font_path = "fonts/Pattaya/Pattaya-Regular.ttf"
    ayutthaya_font_path = "fonts/Ayutthaya/Ayutthaya/Ayutthaya.ttf"
    text_file_path = "gt.txt"
    # generate_images_with_pillow(input_path, output_folder_path, pattaya_font_path)
    generate_images_with_pillow(input_path, output_folder_path, pattaya_font_path, text_file_path)


if __name__ == "__main__":
    main()





# generate with synthtiger



# list of fonts
# pattaya font
# ayutthaya font