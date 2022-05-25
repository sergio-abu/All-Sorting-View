# MERGE SORT
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


def make_lst(draw_info):
    return draw_info.lst


def merge_sort(lst, draw_info, ascending=True):

    # ASCENDING
    if ascending:
        #  r is the point where the array is divided into two subarrays
        r = len(lst) // 2
        L = lst[:r]
        M = lst[r:]

        # Sort the two halves
        merge_sort(L, draw_info)
        merge_sort(M, draw_info)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                lst[k] = L[i]
                i += 1
                draw_list(draw_info, {k - 1: draw_info.BLUE, i: draw_info.RED}, True)
                yield True
            else:
                lst[k] = M[j]
                j += 1
                draw_list(draw_info, {k - 1: draw_info.BLUE, j: draw_info.RED}, True)
                yield True
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1
            draw_list(draw_info, {k - 1: draw_info.BLUE, i: draw_info.RED}, True)
            yield True

        while j < len(M):
            lst[k] = M[j]
            j += 1
            k += 1
            draw_list(draw_info, {k - 1: draw_info.BLUE, j: draw_info.RED}, True)
            yield True

    # DESCENDING
    elif not ascending:
        #  r is the point where the array is divided into two subarrays
        r = len(lst) // 2
        L = lst[:r]
        M = lst[r:]

        # Sort the two halves
        merge_sort(draw_info, False, L)
        merge_sort(draw_info, False, M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            lst[k] = M[j]
            j += 1
            k += 1
