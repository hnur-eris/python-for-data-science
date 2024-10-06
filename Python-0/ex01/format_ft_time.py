import time

date = time.time()
str_date = str(date)
number, float_part = str_date.split(".")
print(f"Second since January 1, 1970: {number[:1]},{number[1:4]},{number[4:7]},{number[7:10]}.{float_part} or {float(str_date):.1e} in scientific notation")

date2 = time.ctime()
new_data = date2.split(" ")
print(new_data[1], new_data[3], new_data[-1])
