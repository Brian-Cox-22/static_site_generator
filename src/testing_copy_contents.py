import os
import shutil


def copy_contents(source_dir, destination_dir):
    '''
    Takes one directory at a time (source_dir)
    And moves each file to a destination_dir
    '''
    # source_dir = os.path.expanduser(source_dir)
    print(source_dir)
    # destination_dir = os.path.expanduser(destination_dir)
    print(destination_dir)

    # Check if the source exhists
    if not os.path.exists(source_dir):
        raise Exception("Invalid source")

    # remove the destination, to keep things clean
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)


    # If its a directory, call on each file in the directory
    if os.path.isdir(source_dir):
        for item in os.listdir(source_dir):
            child_source = os.path.join(source_dir, item)
            child_destination = os.path.join(destination_dir, item)
            copy_contents(child_source, child_destination)
    
    # If its a file, just move the file
    elif os.path.isfile(source_dir):
        print(source_dir)
        shutil.copy2(source_dir, destination_dir)



## Test 1

copy_contents("./static", "./public")