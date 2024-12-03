from PIL import Image
import os
import shutil


def convert_to_grayscale(image_path, save_path):
    """Конвертирует изображение в черно-белое и сохраняет его."""
    img = Image.open(image_path)
    grayscale_img = img.convert("L")
    grayscale_img.save(save_path)


def resize_image(image_path, save_path, new_size):
    """Изменяет размер изображения и сохраняет его."""
    img = Image.open(image_path)
    resized_img = img.resize(new_size)
    resized_img.save(save_path)


def move_image(image_path, target_directory):
    """Перемещает изображение в другую папку."""
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    image_name = os.path.basename(image_path)
    new_path = os.path.join(target_directory, image_name)
    shutil.move(image_path, new_path)
    return new_path
