import os
import shutil
import random


def data_reindexing():
    # Path to the folder containing the YOLO annotation files
    annotations_path = r"D:\programming\laboratory tools detector\dataset\micropipette tip\train\labels"

    # Output folder for updated annotation files (optional)
    updated_path = r"D:\programming\laboratory tools detector\dataset\micropipette tip\train\annotated_labels"
    os.makedirs(updated_path, exist_ok=True)

    # Loop through all annotation files
    for filename in os.listdir(annotations_path):
        if filename.endswith(".txt"):
            input_file = os.path.join(annotations_path, filename)
            output_file = os.path.join(updated_path, filename)

            with open(input_file, "r") as file:
                lines = file.readlines()

            updated_lines = []
            for line in lines:
                parts = line.strip().split()
                if parts:  # Ensure line is not empty
                    parts[0] = "10"  # Update the class index to 9
                    updated_lines.append(" ".join(parts))

            with open(output_file, "w") as file:
                file.write("\n".join(updated_lines))
    print("Class index updated successfully!")





label_dir = r"D:\programming\laboratory tools detector\dataset\flask\test\labels"
output_dir = r"D:\programming\laboratory tools detector\dataset\flask\test\annotated labels"
# Mapping of old class IDs to new labels
label_map = {0: 11, 1: 12, 2: 13, 3: 14, 4: 15, 5: 16}
#
#
# os.makedirs(output_dir, exist_ok=True)

# Function to relabel a single file and save to output directory
def relabel_file(file_path, output_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        parts = line.strip().split()
        old_class_id = int(parts[0])
        new_class_id = label_map.get(old_class_id, old_class_id)  # Default to old ID if not mapped
        new_line = f"{new_class_id} {' '.join(parts[1:])}\n"
        new_lines.append(new_line)

    with open(output_path, "w") as f:
        f.writelines(new_lines)

# Process all label files in the directory
# for filename in os.listdir(label_dir):
#     if filename.endswith(".txt"):
#         file_path = os.path.join(label_dir, filename)
#         output_path = os.path.join(output_dir, filename)
#         relabel_file(file_path, output_path)
#
# print(f"Relabeling complete! Relabeled files saved to: {output_dir}")


def split_micropipette_data(train_images_dir, train_labels_dir,
                       valid_images_dir, valid_labels_dir,
                       test_images_dir, test_labels_dir,
                       micropipette_class_id = 10,
                       valid_split = 0.1, test_split = 0.1):
    os.makedirs(valid_images_dir, exist_ok=True)
    os.makedirs(valid_labels_dir, exist_ok=True)
    os.makedirs(test_images_dir, exist_ok=True)
    os.makedirs(test_labels_dir, exist_ok=True)


    def find_micropipette_files():
        matching_files = []
        for label_file in os.listdir(train_labels_dir):
            if label_file.endswith(".txt"):
                label_path = os.path.join(train_labels_dir, label_file)
                with open(label_path, "r") as f:
                    lines = f.readlines()
                    if any(line.startswith(str(micropipette_class_id)) for line in lines):
                        matching_files.append(label_file)
        return matching_files

    # Move files to the new directories
    def move_files(files, dest_images_dir, dest_labels_dir):
        for label_file in files:
            # Corresponding image file
            image_file = label_file.replace(".txt", ".jpg")  # Adjust if using different extensions
            label_src = os.path.join(train_labels_dir, label_file)
            image_src = os.path.join(train_images_dir, image_file)

            # Destination paths
            label_dest = os.path.join(dest_labels_dir, label_file)
            image_dest = os.path.join(dest_images_dir, image_file)

            # Move files
            if os.path.exists(label_src) and os.path.exists(image_src):
                shutil.move(label_src, label_dest)
                shutil.move(image_src, image_dest)

    # Find all files containing the micropipette tip class
    micropipette_files = find_micropipette_files()

    # Shuffle the files randomly
    random.shuffle(micropipette_files)

    # Split the files into validation and test sets
    num_valid = int(len(micropipette_files) * valid_split)
    num_test = int(len(micropipette_files) * test_split)

    valid_files = micropipette_files[:num_valid]
    test_files = micropipette_files[num_valid:num_valid + num_test]

    # Move files
    print(f"Moving {len(valid_files)} files to validation set...")
    move_files(valid_files, valid_images_dir, valid_labels_dir)

    print(f"Moving {len(test_files)} files to test set...")
    move_files(test_files, test_images_dir, test_labels_dir)

    print("Dataset split complete!")



    """the data for micropipette tip only contains train data so i want to give some of its train data to the test and valid folder!"""



split_micropipette_data(
    train_images_dir=r"D:\programming\laboratory tools detector\dataset\micropipette tip\train\images",
    train_labels_dir=r"D:\programming\laboratory tools detector\dataset\micropipette tip\train\annotated_labels",
    valid_images_dir=r"D:\programming\laboratory tools detector\dataset\micropipette tip\train\new_splitted_dataset\valid\image",
    valid_labels_dir=r"D:\programming\laboratory tools detector\dataset\micropipette tip\train\new_splitted_dataset\valid\label",
    test_images_dir=r"D:\programming\laboratory tools detector\dataset\micropipette tip\train\new_splitted_dataset\test\image",
    test_labels_dir=r"D:\programming\laboratory tools detector\dataset\micropipette tip\train\new_splitted_dataset\test\label",
    micropipette_class_id=10,  # Adjust as per your class ID
    valid_split=0.1,          # 10% of data to validation
    test_split=0.1            # 10% of data to test
)