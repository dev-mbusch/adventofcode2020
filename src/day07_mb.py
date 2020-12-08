"""
https://adventofcode.com/2020/day/7
"""

from collections import namedtuple
from pprint import pprint as pp

with open(r'./input_files/day07_input_mb.txt', 'r') as fh:
    raw_input = fh.read()


# Step 1 seperate lines to get the rules
raw_rules = raw_input.splitlines()

# Step 2 seperate outer layer from inner layer
split_outer_layer = [rule.split(' contain ') for rule in raw_rules if 'no other bags' not in rule]

# Step 3 build a dictionary with outer bags as keys and their content as a list of Bags
outer_bags = [' '.join(item[0].split(' ')[0:2]) for item in split_outer_layer]

Bags = namedtuple('Bags', ['amount', 'color'])
inner_bags = [item[1].split(', ') for item in split_outer_layer]
inner_bags = [ [item.split(' ') for item in sublist] for sublist in inner_bags ]
inner_bags = [ [ Bags(item[0], ' '.join(item[1:3]) ) for item in sublist] for sublist in inner_bags ]

dict_bags = {key: value for key, value in zip(outer_bags, inner_bags)}

candidates = set('shiny gold')

# keys = list(dict_bags.keys())


for candidate in candidates.copy():
    for key in dict_bags.copy():
        for bag in dict_bags[key]:
            if candidate in bag.color:
                candidates.add(key)



# def search_bags(search_dict, candidates=set()):
#     while len(search_dict):
#         if not candidates:
#             for key in search_dict:
#                 for bag in search_dict[key]:
#                     if 'shiny gold' in bag.color:
#                         candidates.add(key)
#                         search_dict.pop('shiny gold')
#                         search_bags(candidates, search_dict)

#         else:
#             for candidate in candidates:
#                 for key in search_dict:
#                     for bag in search_dict[key]:
#                         if candidate in bag.color:
#                             candidates.add(key)
#                             search_dict.pop(candidate)
#                             search_bags(candidates, search_dict)

#     return candidates

