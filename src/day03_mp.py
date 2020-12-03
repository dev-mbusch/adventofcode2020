

if __name__ == '__main__':
    file = open("input_files\day03_input_mp.txt")
    lines = file.read().split("\n")
    file.close()

    tree_counter = 0
    horizontal_position = 0
    
    
    # print(lines[0][2] == "#")
    for line in lines:
        if line[horizontal_position] == "#":
            tree_counter += 1
        if horizontal_position < len(line) - 3:
            horizontal_position += 3
        else:
            horizontal_position = ((horizontal_position + 3) % 31)


    print(tree_counter)
    
    # print(tree_counter)