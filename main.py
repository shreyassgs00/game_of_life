import math
import iteration
import set_field
import sys
import conditions

def main():
    height = int(input('Enter the height of the bounded field in units: '))
    if not conditions.validity(height):
        print("Height must be a positive number.")
        sys.exit()

    width = int(input('Enter the width of the unbounded field in units: '))
    if not conditions.validity(width):
        print("Width must be a positive number.")
        sys.exit()
    
    field = set_field.Field(height,width)
    field_array = field.form_field_array()
    field_array = set_field.place_random_ones(field_array)
    set_field.build_field(field_array)

    n = 1
    while n == 1:
        field_array = iteration.next_iteration(field_array)
        set_field.build_field(field_array)

if __name__ == '__main__':
    main()

        
