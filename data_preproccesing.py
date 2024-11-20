import os


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



data_reindexing()