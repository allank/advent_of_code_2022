def process_input(input):
    lines = input.splitlines()
    return lines


def dir_size(lines):
    dirs = {}
    current = ""
    tree = []
    for line in lines:
        parts = line.split(" ")
        if line.startswith("$ cd .."):
            tree.pop()
        elif line.startswith("$ cd"):
            current_dir = parts[2]
            tree.append(current_dir)
            current = tuple(tree)
            if dirs.get(current, None):
                pass
            else:
                dirs[current] = {}
                dirs[current]["sub"] = []
                dirs[current]["files"] = 0
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            dirs[current]["sub"].append(parts[1])
        else:
            start = line.split(" ")
            if all([n.isdigit() for n in start[0]]):
                dirs[current]["files"] = dirs[current]["files"] + int(start[0])
    return dirs


def walk_tree(dirs, tree):
    # path = list(tree)
    total = dirs[tree]["files"]
    for d in dirs[tree]["sub"]:
        local_tree = list(tree)
        local_tree.append(d)
        tree_total = walk_tree(dirs, tuple(local_tree))
        total = total + tree_total
    return total


def part1(input):
    lines = process_input(input)
    dirs = dir_size(lines)
    valid = []
    for k in dirs.keys():
        size = walk_tree(dirs, k)
        if size <= 100000:
            valid.append(size)
    return sum(valid)


def part2(input):
    lines = process_input(input)
    dirs = dir_size(lines)
    sizes = []
    for k in dirs.keys():
        size = walk_tree(dirs, k)
        sizes.append(size)
    total = walk_tree(dirs, ("/",))
    available = 70000000 - total
    required = 30000000 - available
    return sorted([size for size in sizes if size >= required])[0]


if __name__ == "__main__":
    # get day number
    day = __file__.split(".")[0].split("_")[-1]
    # get raw input
    with open(f"data/input_{day}.txt", "r") as f:
        input = f.read()
    # TODO: if function returns 0 then this will not print ....
    if result_one := part1(input):
        print(f"Part 1: {result_one}")
    if result_two := part2(input):
        print(f"Part 2: {result_two}")
