# SELECTION SORT
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


def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for step in range(len(lst)):
        min_index = step

        for i in range(step+1, len(lst)):
            ascending_sort = (lst[i] < lst[min_index]) and ascending
            descending_sort = (lst[i] > lst[min_index]) and not ascending
            if ascending_sort or descending_sort:
                min_index = i

        draw_list(draw_info, {step - 1: draw_info.BLUE, min_index: draw_info.RED}, True)
        (lst[step], lst[min_index]) = (lst[min_index], lst[step])
        yield True

    return lst



