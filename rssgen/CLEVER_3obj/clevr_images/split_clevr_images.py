import os
import random
import shutil

# Configuration
input_dir = '/home/jovyan/workspace/rsbench-code/rssgen/out/clevr_images/train'  # change this to your actual folder path
output_base = '/home/jovyan/workspace/datasets/CLE4EVR_3obj'    # base folder for output
train_ratio, val_ratio, test_ratio = 0.5, 0.2, 0.3
random.seed(42)  # for reproducibility

# Create output directories
for split in ['train', 'val', 'test']:
    os.makedirs(os.path.join(output_base, split), exist_ok=True)

# Get all base filenames (without extension)
all_files = sorted(f for f in os.listdir(input_dir) if f.endswith('.json'))
all_ids = [os.path.splitext(f)[0] for f in all_files]

# Shuffle and split
random.shuffle(all_ids)
n_total = len(all_ids)
n_train = int(train_ratio * n_total)
n_val = int(val_ratio * n_total)

train_ids = all_ids[:n_train]
val_ids = all_ids[n_train:n_train + n_val]
test_ids = all_ids[n_train + n_val:]

# Function to copy paired files
def copy_pairs(file_ids, split):
    for fid in file_ids:
        for ext in ['.json', '.png']:
            src = os.path.join(input_dir, fid + ext)
            dst = os.path.join(output_base, split, fid + ext)
            shutil.copy2(src, dst)

# Copy files
copy_pairs(train_ids, 'train')
copy_pairs(val_ids, 'val')
copy_pairs(test_ids, 'test')

print(f'Done. Total: {n_total}, Train: {len(train_ids)}, Val: {len(val_ids)}, Test: {len(test_ids)}')
