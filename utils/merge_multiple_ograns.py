import os

if __name__ == '__main__':
    DATASET = 'abd_corr_view'

    liver_path = f'./dataset/{DATASET}/MasksLiver_yolo_segmentation/'
    spleen_path = f'./dataset/{DATASET}/MasksSpleen_yolo_segmentation/'
    kidneyR_path = f'./dataset/{DATASET}/MasksKidneyR_yolo_segmentation/'
    
    dest_path = f'./dataset/{DATASET}/masks_liver_spleen_kidneyR/'

    os.makedirs(dest_path, exist_ok=True)

    for mask in os.listdir(liver_path):
        with open(liver_path+mask, 'r') as file:
            liver = list(file.read().rstrip('\n'))
        with open(spleen_path+mask, 'r') as file:
            spleen = list(file.read().rstrip('\n'))
        with open(kidneyR_path+mask, 'r') as file:
            kidneyR = list(file.read().rstrip('\n'))
        
        spleen[0] = '1'
        kidneyR[0] = '2'
        
        organs = [''.join(liver), ''.join(spleen), ''.join(kidneyR)]

        with open(dest_path+mask, 'w') as file:
            file.write('\n'.join(organs))
        file.close()
