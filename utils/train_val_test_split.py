import os
import shutil
import random
from tqdm import tqdm  # For progress bar


def split_and_copy_data(source_dir, destination_dir, train_ratio, test_ratio, validation_ratio):
    split_subsets = ['train', 'test', 'val']

    # Create destination folders if they don't exist
    for split in split_subsets:
      os.makedirs(os.path.join(destination_dir, 'images', split), exist_ok=True)
      os.makedirs(os.path.join(destination_dir, 'labels', split), exist_ok=True)
    
    # Get a list of image files in the source directory
    image_files = os.listdir(os.path.join(source_dir, 'images'))
    random.shuffle(image_files)

    total_files = len(image_files)
    train_count = int(total_files * train_ratio)
    test_count = int(total_files * test_ratio)
    validation_count = total_files - train_count - test_count

    train_files = image_files[:train_count]
    test_files = image_files[train_count:train_count + test_count]
    validation_files = image_files[train_count + test_count:]

    # Copy images and masks to train, test, and validation folders
    for split, files in [('train', train_files), ('test', test_files), ('val', validation_files)]:
        for file in tqdm(files, desc=f'Copying {split} files'):
            image_source_path = os.path.join(source_dir, 'images/', file)
            mask_source_path = os.path.join(source_dir, 'labels_1_cls/', file[:-4]+'.txt')

            image_destination_path = os.path.join(destination_dir, 'images', split, file)
            mask_destination_path = os.path.join(destination_dir, 'labels', split, file[:-4]+'.txt')

            shutil.copy(image_source_path, image_destination_path)
            shutil.copy(mask_source_path, mask_destination_path)

    print("Split and copy completed.")

if __name__ == '__main__':
    source_directory = "./dataset/both_suitcases/"
    destination_directory = "./dataset/both_suitcases_1_cls/" 
    train_ratio = 0.8  # 70% for training
    test_ratio = 0.15   # 20% for testing
    validation_ratio = 0.05  # 10% for validation
    
    split_and_copy_data(source_directory, destination_directory, train_ratio, test_ratio, validation_ratio)
