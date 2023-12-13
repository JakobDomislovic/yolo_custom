import os

if __name__ == '__main__':
    
    DATASET = 'both_suitcases'

    labels_path = f'./dataset/{DATASET}/labels/'
    
    dest_path = f'./dataset/{DATASET}/labels_renamed/'

    os.makedirs(dest_path, exist_ok=True)

    for mask in os.listdir(labels_path):
        with open(labels_path+mask, 'r') as file:
            lines = file.readlines() # list(file.read().rstrip('\n'))

        if len(lines) == 2:
            first_line = list(lines[0])
            second_line = list(lines[1])
            second_line[0] = '1'
            merged = [''.join(first_line), ''.join(second_line)]
        else:
            merged = lines

        with open(dest_path+mask, 'w') as file:
            file.write('\n'.join(merged))
        file.close()

