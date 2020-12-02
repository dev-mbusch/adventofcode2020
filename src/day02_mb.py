"""
https://adventofcode.com/2020/day/2
"""

from collections import namedtuple

# Reading the Input
with open(r'../input_files/day02_input_mb.txt', 'r') as fh:
    lines = [line.strip('\n') for line in fh.readlines()]

# Yeah, I've used namedtuples for the first time in a real use case :) --> https://docs.python.org/3/library/collections.html#collections.namedtuple
Password_Policy_1 = namedtuple('Password_Policy_1', ['min', 'max', 'char', 'passphrase'])

# Create
passwords_1 = []
for line in lines:
    temp = line.replace('-', ' ').replace(': ', ' ').split()
    passwords_1.append(Password_Policy_1(int(temp[0]), int(temp[1]), temp[2], temp[3]))

# Test Cases Part One
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Should return 2 because two passwords (first line/last line) comply to the password policy.

def check_pwd_policy_compliance_1(passwords):
    "Takes a list of PasswordPolicies and checks if the passwords comply to the policy."
    valid_passwords = 0
    for password in passwords:
        if password.passphrase.count(password.char) in range(password.min, password.max+1):
            valid_passwords += 1
    return valid_passwords

print(f'Part One - Number of valid passwords: {check_pwd_policy_compliance_1(passwords_1)}')


# TODO: WRONG!
# Tests Cases Part Two
# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

# Yeah, I've used namedtuples for the first time in a real use case :) --> https://docs.python.org/3/library/collections.html#collections.namedtuple
Password_Policy_2 = namedtuple('Password_Policy_2', ['fst_idx', 'snd_idx', 'char', 'passphrase'])

# Create
passwords_2 = []
for line in lines:
    temp = line.replace('-', ' ').replace(': ', ' ').split()
    passwords_2.append(Password_Policy_2(int(temp[0]), int(temp[1]), temp[2], temp[3]))


def check_equality(char, position, input_string):
    if char == input_string[position]:
        return True
    elif position > len(input_string):
        return False
    else:
        return False


def check_pwd_policy_compliance_2(passwords):
    "Takes a list of PasswordPolicies and checks if the passwords comply to the policy."
    valid_passwords = 0
    count1 = 0
    count2 = 0

    for password in passwords:
        # print(f'{password.snd_idx < len(password.passphrase) -1 = }')
        if check_equality(password.char, password.fst_idx - 1 , password.passphrase) ^ check_equality(password.char, password.snd_idx - 1 , password.passphrase):
            valid_passwords += 1
    return valid_passwords

print(f'Part Two - Number of valid passwords: {check_pwd_policy_compliance_2(passwords_2)}')
