box_height = int(input())
box_width = int(input())
box_length = int(input())
window_height = int(input())
window_width = int(input())

print('N') if box_height > window_height and box_length > window_height and box_width > window_height or box_height > window_width and box_length > window_width and box_width > window_width else print('S')