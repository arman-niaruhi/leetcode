def convert(s:str, numRows:int)->str:
    # if number of rows is just one or is greater than the length of the string we return the string itself
    if numRows == 1 or numRows >= len(s):
            return s
        
    converted_str = ""
    converted_str_list = ["" for _ in range(numRows)]
    going_down = False
    curr_row = 0
    
    for char in s:
        converted_str_list[curr_row] += char
        # Revert the direction
        if curr_row == 0 or curr_row == numRows-1:
            going_down = not going_down
        curr_row += 1 if going_down else -1
    
    converted_str = converted_str.join(converted_str_list)
    return converted_str
