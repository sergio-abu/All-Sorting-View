import pygame
import random
import math
import SelectionSort
import InsertionSort

pygame.init()


class DrawInfo:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    BLUE = 65, 105, 225
    RED = 255, 0, 0
    BG_COLOR = WHITE

    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    SMALL_FONT = pygame.font.SysFont('comicsans', 25)
    FONT = pygame.font.SysFont('comicsans', 30)
    BIG_FONT = pygame.font.SysFont('comicsans', 40)

    SIDES = 100
    TOP = 200

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("All Sorting Algorithms Visualized")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDES) / len(lst))
        self.block_height = math.floor((self.height - self.TOP) / (self.max_val - self.min_val))
        self.start_x = self.SIDES // 2


def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BG_COLOR)

    best_time = 0
    worst_time = 0
    avg_time = 0
    space_com = 0
    stability = 0

    # BEST TIME CHECK
    if algo_name in ('Counting Sort', 'Radix Sort', 'Bucket Sort'):
        best_time = 'n+k'
    elif algo_name in ('Merge Sort', 'Quicksort', 'Heap Sort', 'Shell Sort'):
        best_time = 'nlog n'
    elif algo_name in ('Insertion Sort', 'Bubble Sort'):
        best_time = 'n'
    elif algo_name == 'Selection Sort':
        best_time = 'n²'

    # WORST TIME CHECK
    if algo_name in ('Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Bucket Sort', 'Quicksort', 'Shell Sort'):
        worst_time = 'n²'
    elif algo_name in ('Counting Sort', 'Radix Sort'):
        worst_time = 'n+k'
    elif algo_name in ('Merge Sort', 'Heap Sort'):
        worst_time = 'nlog n'

    # AVERAGE TIME CHECK
    if algo_name in ('Bubble Sort', 'Selection Sort', 'Insertion Sort'):
        avg_time = 'n²'
    elif algo_name in ('Counting Sort', 'Radix Sort'):
        avg_time = 'n+k'
    elif algo_name in ('Merge Sort', 'Quicksort', 'Heap Sort', 'Shell Sort'):
        avg_time = 'nlog n'
    elif algo_name == 'Bucket Sort':
        avg_time = 'n'


    # SPACE COMPLEXITY CHECK
    if algo_name in ('Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Heap Sort', 'Shell Sort'):
        space_com = '1'
    elif algo_name in ('Counting Sort', 'Radix Sort'):
        space_com = 'max'
    elif algo_name == 'Merge Sort':
        space_com = 'n'
    elif algo_name == 'Quicksort':
        space_com = 'log n'
    elif algo_name == 'Bucket Sort':
        space_com = 'n+k'

    # STABILITY CHECK
    if algo_name in ('Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Counting Sort', 'Radix Sort', 'Bucket Sort'):
        stability = 'Yes'
    else:
        stability = 'No'

    # TITLE
    title = draw_info.BIG_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1,
                                      draw_info.BLUE)
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))

    # COMMANDS
    controls = draw_info.FONT.render("[R] Reset | [SPACE] Start Sorting | [A] Ascending | [D] Descending", 1,
                                     draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 45))

    # ALGORITHMS
    info = draw_info.SMALL_FONT.render("[1] Bubble Sort | [2] Selection Sort | [3] Insertion Sort | [4] Merge Sort |"
                                       " [5] Quicksort", 1, draw_info.BLACK)
    draw_info.window.blit(info, (draw_info.width / 2 - info.get_width() / 2, 75))

    info = draw_info.SMALL_FONT.render("[6] Counting Sort | [7] Radix Sort | [8] Bucket Sort |"
                                       " [9] Heap Sort | [0] Shell Sort", 1, draw_info.BLACK)
    draw_info.window.blit(info, (draw_info.width / 2 - info.get_width() / 2, 95))

    # STATS
    info = draw_info.SMALL_FONT.render(f"Best Time Complexity: {best_time} | Worst Time Complexity: {worst_time} |"
                                       f" Average Time Complexity: {avg_time}", 1, draw_info.RED)
    draw_info.window.blit(info, (draw_info.width / 2 - info.get_width() / 2, 125))

    info = draw_info.SMALL_FONT.render(f"Space Complexity: {space_com} |"
                                       f" Same Value Stability: {stability}", 1, draw_info.RED)
    draw_info.window.blit(info, (draw_info.width / 2 - info.get_width() / 2, 145))

    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info, color_positions=None, clear_bg=False):
    if color_positions is None:
        color_positions = {}
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDES // 2, draw_info.TOP,
                      draw_info.width - draw_info.SIDES, draw_info.height - draw_info.TOP)
        pygame.draw.rect(draw_info.window, draw_info.BG_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.GRADIENTS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()


def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.BLUE, j + 1: draw_info.RED}, True)
                yield True

    return lst


def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInfo(800, 600, lst)
    sorting = False
    ascending = True

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(60)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_1 and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algo_name = "Bubble Sort"
            elif event.key == pygame.K_2 and not sorting:
                sorting_algorithm = SelectionSort.selection_sort
                sorting_algo_name = "Selection Sort"
            elif event.key == pygame.K_3 and not sorting:
                sorting_algorithm = InsertionSort.insertion_sort
                sorting_algo_name = "Insertion Sort"
            elif event.key == pygame.K_4 and not sorting:
                sorting_algorithm = InsertionSort.insertion_sort
                sorting_algo_name = "Merge Sort"
            elif event.key == pygame.K_5 and not sorting:
                sorting_algorithm = InsertionSort.insertion_sort
                sorting_algo_name = "Quicksort"
            elif event.key == pygame.K_6 and not sorting:
                sorting_algorithm = InsertionSort.insertion_sort
                sorting_algo_name = "Counting Sort"
            elif event.key == pygame.K_7 and not sorting:
                sorting_algorithm = InsertionSort.insertion_sort
                sorting_algo_name = "Radix Sort"
            elif event.key == pygame.K_8 and not sorting:
                sorting_algorithm = InsertionSort.insertion_sort
                sorting_algo_name = "Bucket Sort"
            elif event.key == pygame.K_9 and not sorting:
                sorting_algorithm = InsertionSort.insertion_sort
                sorting_algo_name = "Heap Sort"
            elif event.key == pygame.K_0 and not sorting:
                sorting_algorithm = InsertionSort.insertion_sort
                sorting_algo_name = "Shell Sort"

    pygame.quit()


if __name__ == "__main__":
    main()
