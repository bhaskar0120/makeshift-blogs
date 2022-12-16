from sys import argv
from json import dump, load
from re import sub
from datetime import datetime

# a function to get the current date in the format DD MMM. YYYY
def get_date():
    return datetime.now().strftime("%d %b. %Y")

def main():
    if len(argv) != 2:
        print("Usage: python publisher.py <FILE.md>")
        return
    
    # Questionaire
    print("Enter the following details for the blog:")

    title = input("Title: ")

    author = input("Author (Bhaskar Bhardwaj): ")
    if author == "":
        author = "Bhaskar Bhardwaj"

    author_img = input("Author Image (https://github.com/bhaskar0120.png): ")
    if author_img == "":
        author_img = "https://github.com/bhaskar0120.png"
    
    description = input("Description: ")
    date = get_date()

    background_image = input("Background Image (https://picsum.photos/1000/300): ")
    if background_image == "":
        background_image = "https://picsum.photos/1000/300"


    print("")
    print("Is the following information correct?")
    print("Title: ", title)
    print("Author: ", author)
    print("Author Image: ", author_img)
    print("Date: ", date)
    print("Description: ", description)
    print("Background Image: ", background_image)
    print("")
    print("Enter 'Y' to continue or any other key to exit")
    if input() != 'Y':
        return
    
    # create id for new blog
    id = sub(' ', '-', title.lower())
    # remove special characters
    id = sub('[^a-z0-9-]', '', id)
    
    # create metadata for new blog
    meta = {
        "title": title,
        "id": id,
        "author": author,
        "content" : description,
        "date": date
    }
    
    with open(argv[1]) as f:
        blog = f.read()

    with open('all.json') as f:
        all_files = load(f)
    
    # add the new blog to the list
    all_files['blogs'].append(meta)
    

    # write all_files to the file all.json
    with open('all.json', 'w') as f:
        dump(all_files, f, indent=4)
    
    # create metadata for md file
    meta_md = {
        "author": author,
        "authorImg": author_img,
        "backgroundImg": background_image,
        "date": date,
        "blog": blog
    }

    # write meta_md in blogs/<id>.json
    with open('./blogs/{}.json'.format(id), 'w') as f:
        dump(meta_md, f, indent=4)

    
if __name__ == "__main__":
    main()