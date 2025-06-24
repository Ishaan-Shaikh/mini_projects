import os
import matplotlib.pyplot as plt

def folder_size_generator():
    folder_path = '/home/ishaan/Documents/'
    folder_sizes = {}
    
    for root, dirs, files in os.walk(folder_path):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(dir_path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)
            folder_sizes[dir] = total_size

    # Generate pie chart
    labels = folder_sizes.keys()
    sizes = folder_sizes.values()
    plt.figure(figsize=(10, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Folder Sizes in D Drive')
    plt.show()

folder_size_generator()
