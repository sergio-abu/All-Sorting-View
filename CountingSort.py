# COUNTING SORT
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


def counting_sort(draw_info, ascending=True):
    lst = draw_info.lst
    size = len(lst)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        count[lst[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[lst[i]] - 1] = lst[i]
        count[lst[i]] -= 1
        i -= 1

    for i in range(0, size):
        lst[i] = output[i]
        draw_list(draw_info, {i - 1: draw_info.BLUE, i: draw_info.RED}, True)
        yield True

    return lst

