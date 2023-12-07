# Read hash
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            index = content.find("My string is: ")
            if index != -1:
                hash_text = content[index + len("My string is: "):].strip()
                return hash_text
        return None
    except FileNotFoundError:
        return None

# Check match hash
def check_hash(hash_text, user_input):
    if hash_text is not None:
        return hash_text == user_input
    else:
        return False

# Check flag
def check_flag(flag_text, user_input):
    if flag_text is not None:
        return flag_text == user_input
    else:
        return False

# myfile.txt path
file_path = 'myfile.txt'
flag_text = 'h1dd3n_1n_pLa1n_51GHT_18375919'

# hash text
content = read_file(file_path)
#print(content)
#print(flag_text)
# Input flag and hash
flag = input("Enter flag: ")
hash = input("Enter hash: ")


# Confirm
if check_hash(content, hash) and check_flag(flag_text, flag):
    print("Congratulations")
else:
    print("Error")
