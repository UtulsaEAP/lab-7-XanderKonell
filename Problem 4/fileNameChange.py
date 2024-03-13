#Name: Xander Konell
#Hour: 3

def fileNameChange():
    #type your code here
    input_file_name = str(input(""))
    try:
        with open(input_file_name, 'r') as file:
            for line in file:
                photo_file_name = line.strip()
                modified_file_name = photo_file_name.replace("_photo.jpg", "_info.txt")
                print(modified_file_name)
    except FileNotFoundError:
        print("File not found!")
        
if __name__ == '__main__':
        fileNameChange()