import os
import pyclan as pc
import shutil

start_dir = "data"   # this is the root folder where all the cha files in question are
output_dir = ""     # this is optional, only for when copy_to_folder = True
copy_to_folder = False   # whether or not to copy the files which have CHI's to an output folder




list_of_files = []

def output_csv(files):
    with open("file_list.csv", "wb") as out:
        for file in files:
            out.write("{}\n".format(file))

def walk_tree(start_dir):
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith(".cha"):
                clan_file = pc.ClanFile(os.path.join(root, file))
                annots = clan_file.annotations()
                if any(x.speaker == "CHI" for x in annots):
                    if copy_to_folder:
                        shutil.copy(os.path.join(root, file),
                                    os.path.join(output_dir, file))
                list_of_files.append(file)

    output_csv(list_of_files)


walk_tree(start_dir)