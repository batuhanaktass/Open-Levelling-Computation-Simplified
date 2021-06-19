import sys
# --- Program Title and Lines Section ---
title = 'This program calculates the elevations in open leveling net'
proportion = len(title)
print('\n' + title + '\n' + ('-' * proportion))  # Print Title and Lines

# --- PID SECTION ---
known_pID = input(f'{"Enter the point ID of known point"} {": ":>20}')  # First PID
# Point ID and Value Lists
point_list = [known_pID]  # Point List
elevation_first = float(input(
    f'{"Enter the elevation of point"} {point_list[0]} {"(m)"} {": ":>19}'))  # Known Elevation of First Known Point
number_unknown = int(input(f'{"Enter the number of unknown points"} {": ":>19}'))  # Number of Unknown Points
for i in range(1, number_unknown + 1):
    unknown_point = input(f'{"Enter the point ID of unknown point"} {i} {": ":>16}')  # Responsive Unknown Point ID
    point_list.append(unknown_point)

# Same Point ID Exception
def Same_except(error_message):
    if error_message.lower() == 'y' or error_message.lower() == 'yes':
        print('Resuming...')
        pass
    else:
        sys.exit()
if len(point_value_list) != len(set(point_value_list)):
    print('\n'+'You Should Not Have Same Point ID' + '\n' + 'That Can Cause Conflict')
    error_message = input('Do You Want To Continue? (Not Recommended) (y/n): ')
    Same_except(error_message)
else:
    pass   