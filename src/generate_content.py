import os
import shutil
from markdown_to_html import markdown_to_html_node, extract_title


def copy_contents(source_dir, destination_dir):
    '''
    Takes one directory at a time (source_dir)
    And moves each file to a destination_dir
    '''
    # source_dir = os.path.expanduser(source_dir)
    print(source_dir)
    # destination_dir = os.path.expanduser(destination_dir)
    print(destination_dir)

    # Check if the source exists
    if not os.path.exists(source_dir):
        raise Exception("Invalid source")

    # remove the destination, to keep things clean
    # if not os.path.exists(destination_dir):
    #     os.makedirs(destination_dir)


    # If its a directory, call on each file in the directory
    if os.path.isdir(source_dir):
        os.makedirs(destination_dir, exist_ok=True)
        for item in os.listdir(source_dir):
            child_source = os.path.join(source_dir, item)
            child_destination = os.path.join(destination_dir, item)
            copy_contents(child_source, child_destination)
    
    # If its a file, just move the file
    elif os.path.isfile(source_dir):
        # print(source_dir)
        shutil.copy2(source_dir, destination_dir)

def generate_page(from_path, template_path, dest_path):
    '''
    Assumes that from_path is a markdown file
    '''
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # read the from path in as from_cont
    if os.path.isfile(from_path):
        with open(from_path) as f: from_cont = f.read()
    else:
        raise Exception(f"{from_path} is not a file")

    # read the template in as temp_cont
    if os.path.isfile(template_path):
        with open(template_path) as f: temp_cont = f.read()
    else:
        raise Exception(f"{template_path} is not a file")
    

    # time to convert to an html string
    # assuming that the markdown file is the from_path, opened as from_cont
    node = markdown_to_html_node(from_cont)  
    html = node.to_html()

    title = extract_title(from_cont)   

    # replace the title
    temp_cont = temp_cont.replace("{{ Title }}", title)

    # and the content
    temp_cont = temp_cont.replace("{{ Content }}", html)

    dirs = dest_path.split("/")
    
    
    file_name = dirs[-1]
    dirs = dirs[:-1]
    dirs = "/".join(dirs)
    # print(dirs)
    # print(file_name)
    # check that directories exist, make any that don't exist
    os.makedirs(dirs, exist_ok=True)



    with open(dest_path, "w") as file:
        file.write(temp_cont)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    '''
    Recursivly generates a new .html file for every .md file using the same template.html
    dir_path_content should be a directory with .md files in it.
    '''


    if os.path.isfile(dir_path_content): # and dir_path_content.split(".", 1)[1] == "md":
        dest_path = dest_dir_path.replace(".md", ".html")
        generate_page(dir_path_content, template_path, dest_path)

    elif os.path.isdir(dir_path_content):
        files = os.listdir(dir_path_content)
        # print(files)
        for file in files:
            # print(os.path.join(dir_path_content, file))
            destination = os.path.join(dest_dir_path, file)
            generate_pages_recursive(os.path.join(dir_path_content, file), template_path, destination)

    else:
        raise Exception(f"{dir_path_content} was neither a .md file or a directory")
    

