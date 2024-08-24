ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

my_tuple = (ft_tuple[0], "Turkey!")
ft_tuple = my_tuple

ft_set.remove("tutu!")
ft_set.remove("Hello")
ft_set.add("Hello")
ft_set.add("Istanbul!")
#garip çalışıyo enteresan


ft_dict["Hello"] = "42Istanbul!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
