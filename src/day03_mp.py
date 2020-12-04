

def count_trees(tree_map, horizontal_steps, vertical_steps):
    map_width = len(tree_map[0])
    tree_counter = 0
    horizontal_position = 0

    for i in range(0, len(tree_map), vertical_steps):
        
        if i != 0 and tree_map[i][horizontal_position] == "#":
            tree_counter += 1
        if horizontal_position < map_width - horizontal_steps:
            horizontal_position += horizontal_steps
        else:
            horizontal_position = ((horizontal_position + horizontal_steps) % map_width)
    
    return tree_counter

if __name__ == '__main__':
    file = open("input_files\day03_input_mp.txt")
    tree_map = file.read().split("\n")
    file.close()

    # Solution part 1
    print(count_trees(tree_map, 3, 1))
    

    # Solution part 2
    slope_1 = count_trees(tree_map, 1, 1)
    slope_2 = count_trees(tree_map, 3, 1)
    slope_3 = count_trees(tree_map, 5, 1)
    slope_4 = count_trees(tree_map, 7, 1)
    slope_5 = count_trees(tree_map, 1, 2)

    print(slope_1 * slope_2 * slope_3 * slope_4 * slope_5)