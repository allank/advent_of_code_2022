def process_input(input):
    lines = input.splitlines()
    lines = [[int(l) for l in line] for line in lines]
    return lines


def is_visible(sight_line, height):
    return all([True if tree < height else False for tree in sight_line])


def check_visible(tree_grid, h, w):
    current_height = tree_grid[h][w]
    # up from current_position
    sight_line = [tree_grid[i][w] for i in range(0, h)]
    u = is_visible(sight_line, current_height)
    # down from current position
    sight_line = [tree_grid[i][w] for i in range(h + 1, len(tree_grid))]
    d = is_visible(sight_line, current_height)
    # left from current position
    sight_line = [tree_grid[h][i] for i in range(0, w)]
    l = is_visible(sight_line, current_height)
    # right from current position
    sight_line = [tree_grid[h][i] for i in range(w + 1, len(tree_grid[0]))]
    r = is_visible(sight_line, current_height)
    return any([u, d, l, r])


def build_grid(tree_grid):
    # this would be easier with numpy...
    width = len(tree_grid[0])
    height = len(tree_grid)
    visible_trees = []
    for h in range(height):
        visible_trees.append([0 for _ in range(width)])

    # mark all edge visible
    for h in range(height):
        visible_trees[h][0] = 1
        visible_trees[h][-1] = 1
    for w in range(width):
        visible_trees[0][w] = 1
        visible_trees[-1][w] = 1

    # walk inside trees
    for h in range(1, height - 1):
        for w in range(1, width - 1):
            visible_trees[h][w] = int(check_visible(tree_grid, h, w))
    return visible_trees


def count_trees(sight_line, current_height):
    trees = 0
    for i in range(0, len(sight_line)):
        trees = trees + 1
        if current_height <= sight_line[i]:
            break
    return trees


def score_tree(tree_grid, h, w):
    # print(h, w)
    current_height = tree_grid[h][w]
    # up from current_position
    sight_line = [tree_grid[i][w] for i in range(0, h)]
    u = count_trees(sight_line[::-1], current_height)
    # down from current position
    sight_line = [tree_grid[i][w] for i in range(h + 1, len(tree_grid))]
    d = count_trees(sight_line, current_height)
    # left from current position
    sight_line = [tree_grid[h][i] for i in range(0, w)]
    l = count_trees(sight_line[::-1], current_height)
    # right from current position
    sight_line = [tree_grid[h][i] for i in range(w + 1, len(tree_grid[0]))]
    r = count_trees(sight_line, current_height)
    return u * d * l * r


def build_score_grid(tree_grid):
    # walk trees
    scenic_scores = []
    for h, row in enumerate(tree_grid):
        for w, _ in enumerate(row):
            scenic_scores.append(score_tree(tree_grid, h, w))
    return scenic_scores


def part1(input):
    grid = process_input(input)
    visible_trees = build_grid(grid)
    total = 0
    for h in visible_trees:
        total = total + sum(h)
    return total


def part2(input):
    grid = process_input(input)
    tree_scores = build_score_grid(grid)
    return max(tree_scores)


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
