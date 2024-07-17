def interchange_first_last(my_list):
    if len(my_list) < 2:
        return my_list
    
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
    return my_list

input_list = [12, 35, 9, 56, 24]
output_list = interchange_first_last(input_list)
print("Output:", output_list)