# HEAP SORT
import pygame


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


def heapify(arr, n, i, ascending):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if ascending:
        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest, ascending)

    elif not ascending:
        if l < n and arr[i] > arr[l]:
            largest = l

        if r < n and arr[largest] > arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest, ascending)


def heap_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)

    for i in range(n // 2, -1, -1):
        heapify(lst, n, i, ascending)
        draw_list(draw_info, {i - 1: draw_info.BLUE, i: draw_info.RED}, True)
        yield True

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        draw_list(draw_info, {i - 1: draw_info.BLUE, i: draw_info.RED}, True)
        yield True
        heapify(lst, i, 0, ascending)
        draw_list(draw_info, {i - 1: draw_info.BLUE, i: draw_info.RED}, True)
        yield True

    return lst
