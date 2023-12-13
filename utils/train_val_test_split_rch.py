import os
import shutil
import random
from tqdm import tqdm  # For progress bar
from sklearn.model_selection import train_test_split


def split_and_copy_data(source_dir, destination_dir, train_ratio, test_ratio, validation_ratio):
    split_subsets = ['train', 'test', 'val']

    # Create destination folders if they don't exist
    for split in split_subsets:
      os.makedirs(os.path.join(destination_dir, 'images', split), exist_ok=True)
      os.makedirs(os.path.join(destination_dir, 'labels', split), exist_ok=True)
    
    # Get a list of image files in the source directory
    image_files = sorted(os.listdir(os.path.join(source_dir, 'Images')))
    
    patients = range(0, len(image_files)//600)

    train, test = train_test_split(patients, test_size=test_ratio, random_state=1)

    train, val = train_test_split(train, test_size=validation_ratio/(train_ratio + validation_ratio), random_state=1)

    # Copy images and masks to train, test, and validation folders
    for split, files in [('train', train), ('test', test), ('val', val)]:
        for patient in tqdm(files, desc=f'Copying {split} files'):
            for file in image_files[patient*600:(patient+1)*600]:
                image_source_path = os.path.join(source_dir, 'Images', file)
                mask_source_path = os.path.join(source_dir, 'MasksLiver_yolo_segmentation/', file[:-4]+'.txt')

                image_destination_path = os.path.join(destination_dir, 'images', split, file)
                mask_destination_path = os.path.join(destination_dir, 'labels', split, file[:-4]+'.txt')

                shutil.copy(image_source_path, image_destination_path)
                shutil.copy(mask_source_path, mask_destination_path)

    print("Split and copy completed.")

if __name__ == '__main__':
    source_directory = "./dataset/abd_corr_view/"
    destination_directory = "./dataset/abd_liver/" 
    train_ratio = 0.7  # 70% for training
    test_ratio = 0.15   # 20% for testing
    validation_ratio = 0.15  # 10% for validation
    
    split_and_copy_data(source_directory, destination_directory, train_ratio, test_ratio, validation_ratio)
