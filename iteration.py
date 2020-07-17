def next_iteration(field_array):
    next_state = field_array
    for i in range (0,len(field_array)):
        for j in range (0,len(field_array[i])):
            if is_alive_next(field_array,i,j):
                next_state[i][j] = 1
            else:
                next_state[i][j] = 0
    return next_state

def is_alive_next(field_array,index1,index2): #Function to check whether a particular element in the field will be alive in the next generation.
    alive_neighbours = 0
    dead_neighbours = 0
    element_value = field_array[index1][index2]
    if index1 == 0 and index2 == 0:
        neighbours = [field_array[index1][index2+1],field_array[index1+1][index2],field_array[index1+1][index2+1]]
        for i in range (0,len(neighbours)):
            if neighbours[i] == 1:
                alive_neighbours = alive_neighbours+1
            else:
                dead_neighbours = dead_neighbours+1

    elif index1 == 0 and index2 == len(field_array[0])-1:
        neighbours = [field_array[index1][index2-1],field_array[index1+1][index2],field_array[index1+1][index2-1]]
        for i in range (0,len(neighbours)):
            if neighbours[i] == 1:
                alive_neighbours = alive_neighbours+1
            else:
                dead_neighbours = dead_neighbours+1

    elif index1 == 0  and index2 > 0 and index2 < len(field_array[0])-1:
        neighbours = [field_array[index1][index2-1],field_array[index1][index2+1],field_array[index1+1][index2],field_array[index1+1][index2-1],field_array[index1+1][index2+1]]
        for i in range (0,len(neighbours)):
            if neighbours[i] == 1:
                alive_neighbours = alive_neighbours+1
            else:
                dead_neighbours = dead_neighbours+1

    elif index1 == len(field_array)-1 and index2 == 0:
        neighbours = [field_array[index1][index2+1],field_array[index1-1][index2],field_array[index1-1][index2+1]]
        for i in range (0,len(neighbours)):
            if neighbours[i] == 1:
                alive_neighbours = alive_neighbours+1
            else:
                dead_neighbours = dead_neighbours+1

    elif index1 == len(field_array)-1 and index2 == len(field_array[0])-1:
        neighbours = [field_array[index1][index2-1],field_array[index1-1][index2],field_array[index1-1][index2-1]]
        for i in range (0,len(neighbours)):
            if neighbours[i] == 1:
                alive_neighbours = alive_neighbours+1
            else:
                dead_neighbours = dead_neighbours+1

    elif index1 == len(field_array)-1  and index2 > 0 and index2 < len(field_array[0])-1:
        neighbours = [field_array[index1][index2-1],field_array[index1][index2+1],field_array[index1-1][index2],field_array[index1-1][index2-1],field_array[index1-1][index2+1]]
        for i in range (0,len(neighbours)):
            if neighbours[i] == 1:
                alive_neighbours = alive_neighbours+1
            else:
                dead_neighbours = dead_neighbours+1

    elif index1 > 0 and index1 < len(field_array)-1 and index2 == 0:
        neighbours = [field_array[index1][index2+1],field_array[index1+1][index2],field_array[index1+1][index2+1],field_array[index1-1][index2],field_array[index1-1][index2+1]]
        for i in range (0,len(neighbours)):
            if neighbours[i] == 1:
                alive_neighbours = alive_neighbours+1
            else:
                dead_neighbours = dead_neighbours+1

    elif index1 > 0 and index1 < len(field_array)-1 and index2 == len(field_array[0])-1:
        neighbours = [field_array[index1][index2-1],field_array[index1+1][index2],field_array[index1+1][index2-1],field_array[index1-1][index2],field_array[index1-1][index2-1]]
        for i in range (0,len(neighbours)):
            if neighbours[i] == 1:
                alive_neighbours = alive_neighbours+1
            else:
                dead_neighbours = dead_neighbours+1
    
    else:
        neighbours = [field_array[index1][index2+1],field_array[index1][index2-1],field_array[index1+1][index2],field_array[index1+1][index2+1],field_array[index1+1][index2-1],field_array[index1-1][index2],field_array[index1-1][index2+1],field_array[index1-1][index2-1]]
        for i in range (0,len(neighbours)):
            if neighbours[i] == 1:
                alive_neighbours = alive_neighbours+1
            else:
                dead_neighbours = dead_neighbours+1
    
    if element_value == 1:
        if alive_neighbours < 2:
            return False
        elif alive_neighbours > 3:
            return False
        else:
            return True
    else:
        if alive_neighbours == 3:
            return True
        else:
            return False