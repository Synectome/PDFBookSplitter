def tuple_sum(a, b):
    c = []
    for i in range(len(a)):
        x = a[i] + b[i]
        c.append(x)
    return tuple(c)


def pixel_column_average(img_obj):
    dimensions = img_obj.size
    minmax = img_obj.getextrema() # minimum and maximum pixel values
    pixel_arr = img_obj.load()
    flat_pixels = list(img_obj.getdata())

    col_averages = []
    for colnum in range(pixel_arr[2]):
        colsum = (0, 0, 0)
        for rownum in range(pixel_arr[1]):
            current_pixel = pixel_arr[rownum, colnum]
            colsum = map(sum, colsum, current_pixel) # sum each three elements in the tuples
        colavg = colsum/dimensions[1]
        col_averages.append(colavg)
    return col_averages
