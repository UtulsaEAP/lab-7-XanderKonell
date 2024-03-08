#Name: Xander Konell
#Hour: 3
def fileNameChange():
    #type your code here 
    file_name = input("Enter file name: ")
    with open(file_name, 'r') as file:
        photo_file_names = file.readlines()
    for photo_file_name in photo_file_names:
        modified_file_name = photo_file_name.strip().replace("_photo.jpg", "__info.txt")
        print(modified_file_name)
    return

if __name__ == '__main__':
    fileNameChange()