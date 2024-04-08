import os
import sys
import shutil


def check_group_dir(dir_path, group_dir_name):
    # Create a directory in the specified path if it doesn't already exist.
    group_dir_path = os.path.join(dir_path, group_dir_name)
    if not os.path.exists(group_dir_path):
        os.makedirs(group_dir_path)
    return group_dir_path

def group_by_a(dir_path):
    # Group files based on their first alphabetical letter
    for filename in os.listdir(dir_path):
        if filename[0] != '.':
            if os.path.isfile(os.path.join(dir_path, filename)):
                group_dir_name = f"{filename[0].upper()} Files"
                group_dir_path = check_group_dir(dir_path, group_dir_name)
                file_path = os.path.join(dir_path,filename)
                # Move the file to it's group directory
                shutil.move(file_path, group_dir_path)
                print(f"Moved: {filename} => {group_dir_name}/")

def group_by_x(dir_path):
    # Group files based on their extension.
    for filename in os.listdir(dir_path):
        if filename[0] != '.':
            if os.path.isfile(os.path.join(dir_path, filename)):
                extension = filename.split('.')[-1].upper()
                if extension:
                    group_dir_name = f"{extension} Files"
                    group_dir_path = check_group_dir(dir_path, group_dir_name)
                    file_path = os.path.join(dir_path,filename)
                    # Move the file to it's group directory
                    shutil.move(file_path, group_dir_path)
                    print(f"Moved: {filename} => {group_dir_name}/")

def help(filename):
    msg = f'''
    Usage: {filename} [OPTION] [PATH (absolute)]

    Group files in PATH directory or the current directory if no PATH by OPTION

    Options:
        -a          Group files based on their first alphabetical letter.
        -h, --help  Display this help 
        -x          Group files based on their extension.

            
    '''
    print(msg)


def clean_dir():

    #default arguments
    dir_path = os.getcwd()
    option = '-x'

    for index, arg in enumerate(sys.argv):
        if index == 1:
            if arg in ['-a','-x','-h','--help']:
                option = arg
            elif arg[0] == '/':
                if os.path.isdir(arg):
                    dir_path = arg
                    break
                else:
                    print(">> Invalid directory path. Please ensure the path is correct and try again.")
                    return
            else:
                print(f"Invalid argument.\nTry '{sys.argv[0]} --help' for more information.")
                return
        elif index == 2:
            if arg[0] == '/':
                if os.path.isdir(arg):
                    dir_path = arg
                    break
                else:
                    print("Invalid directory path. Please ensure the path is correct and try again.")
                    return
            else:
                print(f"Invalid argument.\nTry '{sys.argv[0]} --help' for more information.")
                return

    if option in ['-h','--help']:
        help(sys.argv[0])
    elif option == '-a':
        group_by_a(dir_path)
    elif option == '-x':
        group_by_x(dir_path)


if __name__ == "__main__":
    clean_dir()