from textnode import TextNode, TextType
# from markdown_to_html import generate_page
from generate_content import copy_contents, generate_page, generate_pages_recursive
import os
import shutil
import sys

if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_contents(dir_path_static, dir_path_public)

    
    # generate content
    generate_pages_recursive("./content", "./template.html", "./public", basepath)






    

main()