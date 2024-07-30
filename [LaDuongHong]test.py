import io

def open_file(file_path: str):
    io.open(file_path, 'r')
    pass

def write_to_file(file_operator: str, text: str, line: int):
    new_lines = []
    # need to read the data first
    with io.open(file_path, 'r') as open:
        new_lines = open.readlines()

    # Insert the text at the specified line number (1-based index)
    # for  the index easier modifying with the existing lines, you can start the index from 1 instead of 0-index starting
    new_lines.insert(line - 1, text + '\n') 

    # writing the data after
    with io.open(file_path, 'w') as file:
        file.writelines(new_lines)    
    pass

def print_file(file_operator: str):
    with io.open(file_path, 'r') as file:
        print(file)
    pass

# Example usage as mentioned on ChatGPT:
if __name__ == '__main__':
    file_path = input('your file you need: ')
    # Be awared, the ath should be inputted directly from a folder location. Ex: /home/user/Downloads/'you_name_file.path'
    
    # your inputs
    line = int(input('Enter line number to insert (1-based): '))
    text = input('Enter text to insert: ')
    
    # the main function
    write_to_file(file_path, text, line)
    
    # Print file has been updated
    print('\nUpdated file contents: ')
    print_file(file_path)