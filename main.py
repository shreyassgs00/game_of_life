import math
import iteration
import set_field

def main():
    height = int(input('Enter the height of the bounded field in units: '))
    width = int(input('Enter the width of the unbounded field in units: '))
    field = set_field.Field(height,width)
    field_array = field.form_field_array()
    field_array = set_field.place_random_ones(field_array)
    set_field.build_field(field_array)

if __name__ == '__main__':
    main()

        
