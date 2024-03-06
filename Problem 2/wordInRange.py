#Name: Xander Konell
#Hour: 3
def wordInRange():
    #Type your code here
    file_name = input().strip()
    lower_bound = input().strip()
    upper_bound = input().strip()
    
    with open(file_name, 'r') as file:
        words = file.readlines()
    
    words.sort()
    
    for word in words:
        word = word.strip()
        if lower_bound <= word <= upper_bound:
            print(f'{word} - in range')
        else:
            print(f'{word} - not in range')
            
    return
if __name__ == '__main__':
    wordInRange()