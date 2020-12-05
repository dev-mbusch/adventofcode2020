import re

def clean_passport_batch(batch_file):
    '''This method cleans a batch of passports (in one string) and provides a cleaned list of passports with a single string in one line per passport.'''
    passports_dirty = batch_file.read().split('\n\n')
    passports = [passp.replace('\n',' ') for passp in passports_dirty]
    return passports

def check_passport(expected_fields, passport):
    '''This method checks whether a password contains all mandatory fields and returns a boolean: True for valid, False for invalid passports.'''
    matched_fields = re.findall(r"(?=("+'|'.join(expected_fields)+r"))",passport)
    is_valid = set(matched_fields).issuperset(set(expected_fields))
    return is_valid


if __name__ == '__main__':
    # reading input file
    file = open("input_files\day04_input_mp.txt")
    passports = clean_passport_batch(file)
    file.close()

    # creating list with mandatory passport fields
    expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    # counter initialization
    number_of_valid_passports = 0

    # looping through the list of passports, checking for validity. Counter increases for each valid passport.
    for passport in passports:
        if check_passport(expected_fields, passport) == True:
            number_of_valid_passports += 1

    print(number_of_valid_passports)