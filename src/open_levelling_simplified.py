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
if len(point_list) != len(set(point_list)):
    print('\n'+'You Should Not Have Same Point ID' + '\n' + 'That Can Cause Conflict')
    error_message = input('Do You Want To Continue? (Not Recommended) (y/n): ')
    Same_except(error_message)
else:
    pass   

#  --- BACK AND FORE SIGHT READING SECTION --- 
bs_read_known = float(input(f'{"Enter the BS reading of point"} {point_list[0]} {"(m)"} {": ":>18}'))  # Back Side Measure of First Point
# Back Side ID and Value List
bs_list = [bs_read_known]
# Fore Side ID and Value List
fs_list = []

# BACK AND FORE SIGHT VALUE INPUT
for i in range(number_unknown):
    if i != (len(point_list) - 2):
        fs_read = float(input(f'{"Enter the FS reading of point"} {point_list[i + 1]} {"(m)"} {": ":>18}'))
        fs_list.append(fs_read)
        bs_read = float(input(f'{"Enter the BS reading of point"} {point_list[i + 1]} {"(m)"} {": ":>18}'))
        bs_list.append(bs_read)
    else:
        fs_read = float(input(f'{"Enter the FS reading of point"} {point_list[i + 1]} {"(m)"} {": ":>18}'))
        fs_list.append(fs_read)

# --- HEIGHT AND ELEVATION DIFFERENCE SECTION --- 
# Height Difference ID and Value List
h_diff_list = []
# Elevation ID and Value List
elev_list = [elevation_first]

# --- Calculation Section --- 
# Height Difference Calculation
for val in range(len(point_list) - 1):
    val = bs_list[val] - fs_list[val]
    h_diff_list.append(val)
# Elevation Calculation
for calc in range(len(h_diff_list)):
    calc = elev_list[calc] + h_diff_list[calc]
    elev_list.append(calc)

# --- Output Section --- 
# First Table
height_calc_title = f'{"Point ID":<12} {"Point ID":<12} {"Delta H"}'
print('\n' + height_calc_title + '\n' + ('-' * len(height_calc_title)))
for i in range(len(point_list) - 1):
    delta_calculation = f'{point_list[i]:<12} {point_list[i + 1]:<12} {format(h_diff_list[i], ".3f")}'
    print(delta_calculation)
print(('-' * len(height_calc_title)))
# Second Table
elev_calc_title = f'{"Point ID":<12} {"Elevation"}'
print(elev_calc_title + '\n' + ('-' * len(elev_calc_title)))
for i in range(len(point_list) - 1):
    elevation_calculation = f'{point_list[i + 1]:<12} {format(elev_list[i + 1], ".3f")}'
    print(elevation_calculation)
print(('-' * len(elev_calc_title)))
