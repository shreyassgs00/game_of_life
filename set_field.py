import random
import iteration

class Field:
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def calc_area(self):
        return (self.height * self.width)

    def form_field_array(self):
        field_array = [[0 for i in range(self.width)] for j in range (self.height)]
        return field_array

def build_field(field_array): 
    for i in range (0,len(field_array)):
        for j in range(0,len(field_array[i])):
            print(field_array[i][j],end='')
        print()

def place_random_ones(field_array):
    random_places = []
    for i in range (0,len(field_array)):
        number = random.randint(0,len(field_array[i])-1)
        if (number == 0):
            continue
        else:
            for j in range (0,number):
                random_place = random.randint(0,len(field_array[i])-1)
                random_places.append([i,random_place])
    
    for i in range(0,len(random_places)):
        index1 = random_places[i][0]
        index2 = random_places[i][1]
        field_array[index1][index2] = 1
    return field_array
