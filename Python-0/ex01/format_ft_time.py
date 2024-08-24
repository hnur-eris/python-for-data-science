import time
#zamanın başlagıcı = January 1, 1970, 00:00:00
#ctime = okunulabilir bi şekilde zamanı gösteriyo
#sleep(2) 2 saniye programı uyutuo

date = time.time()
str_date = str(date)
number, float_part = str_date.split(".")
print(f"Second since January 1, 1970: {number[:1]},{number[1:4]},{number[4:7]},{number[7:10]}.{float_part}")
# print(date)

date2 = time.ctime()
new_data = date2.split(":")[0]
print(new_data[:-3])
