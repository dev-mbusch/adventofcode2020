import re

def lineparser (policy_and_password: str):
    """Takes in a string consisting of a policy followed by a password.
    Policies define min and max occurencies of a single character within a password, e.g. min-max x.
    Policies and passwords are seperated by a colon.
    An example input string looks like 2-7 x: abcxyz"""

    policy = re.split(r':', policy_and_password)[0]
    password = re.split(r':', policy_and_password)[1].strip()

    patterns = re.match("(\d+)-(\d+)\s(\w)", policy).groups()

    return (*patterns, password)

def password_validator(min, max, magic_char, password):
    """Takes in elements of a policy: min and mac occurency of a specific chareacter as well as a password to be validated against the policy."""
    magic_char_count = password.count(magic_char)
    is_valid = (magic_char_count >= int(min) and magic_char_count <= int(max))
    return is_valid

def second_password_validator(first_index, second_index, magic_char, password):
    is_valid = (password[int(first_index)-1] == magic_char and password[int(second_index)-1] != magic_char) or (password[int(first_index)-1] != magic_char and password[int(second_index)-1] == magic_char)
    return is_valid
    
#sample_input = "4-5 t: ttglwxxghtznp"
# parsed_input = lineparser(sample_input)
# #print(password_validator(1,12,"t","ttglwxxghtznp"))
#print(password_validator(*lineparser(sample_input)))


if __name__ == '__main__':
    file = open("input_files\day02_input_mp.txt")
    lines = file.read().split("\n")
    file.close()

    # define counter
    valid_password_count = 0
    second_valid_password_count = 0

    for line in lines:
        if password_validator(*lineparser(line)):
            valid_password_count += 1
        if second_password_validator(*lineparser(line)):
            second_valid_password_count +=1
    
    print(valid_password_count)
    print(second_valid_password_count)