import tkinter,datetime, math
    
def is_prime(number):
    if (number == 1 or number == 2 or number == 3):
        return True
    for i in range(2, round(math.sqrt(number)) + 1):
        if (number % i == 0):
            return False
    return True
    

def change_direction(direction_vector):
    if (direction_vector[0] == -1 and direction_vector[1] == 0):
        direction_vector[0] = 0
        direction_vector[1] = 1
        return 1
    if (direction_vector[0] == 1 and direction_vector[1] == 0):
        direction_vector[0] = 0
        direction_vector[1] = -1
        return 1
    if (direction_vector[0] == 0 and direction_vector[1] == 1):
        direction_vector[0] = 1
        direction_vector[1] = 0
        return 1
    if (direction_vector[0] == 0 and direction_vector[1] == -1):
        direction_vector[0] = -1
        direction_vector[1] = 0
        return 1
        

root = tkinter.Tk()
canv = tkinter.Canvas(root, width = 901, height = 901, background = 'black')


start_point_x, start_point_y = 450, 400
direction_vector = []
direction_vector.append(-1)
direction_vector.append(0)

limit = 35000
x, y = start_point_x, start_point_y
coil_finished = 0
coil_side = 1
current_side_position = 0
current_spiral_position = 0
scale = 4

start_time = datetime.datetime.now()
print("Started {0} {1} {2}".format(start_time.hour, start_time.minute, start_time.second))
for i in range(1, limit):
    if (is_prime(i) == False):
        canv.create_oval(x,y,x,y, fill = 'midnight blue', outline = 'midnight blue')
    if (is_prime(i) == True):
        canv.create_oval(x,y,x,y, fill = 'snow', outline = 'snow')
    if (i == 1): # Если находимся в центре экрана
        x += scale*direction_vector[0]
        y += scale*direction_vector[1]
        coil_side = 3
    else: 
        if (coil_finished == 1): # Если только что завершили виток
            current_side_position = 0
            current_spiral_position = 0
            coil_side += 2
            coil_finished = 0
        else:
            if (current_spiral_position == 0): # Если только что начали новый виток
                x += scale*direction_vector[0]
                y += scale*direction_vector[1]
                current_spiral_position += 1
                current_side_position += 1
                change_direction(direction_vector)
            else:
                if (current_side_position == coil_side - 1): # Если стоим на углу витка
                    if (current_spiral_position == 2*coil_side + 2*(coil_side - 2)): # Если этот угол - конечный
                        coil_finished = 1
                        continue
                    else: # Если этот угол - не конечный
                        change_direction(direction_vector)
                        x += scale*direction_vector[0]
                        y += scale*direction_vector[1]
                        current_side_position = 1
                        current_spiral_position += 1
                else: # Если стоим не на углу витка
                    x += scale*direction_vector[0]
                    y += scale*direction_vector[1]
                    current_side_position += 1
                    current_spiral_position += 1
        
end_time = datetime.datetime.now()
print("Ended {0} {1} {2}".format(end_time.hour, end_time.minute, end_time.second))

canv.pack()
root.mainloop()

# No optimization, O(n^2), 2k numbers spiral: 11 min 40 sec ??
# Optimization 1, ~O(sqrt n), 2k numbers spiral: ahahaha 1 sec
        