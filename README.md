# python-for-data-science

for ex06
    Syntax: filter(function, sequence)

    Parameters:

        function: function that tests if each element of a sequence is true or not.
        sequence: sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.

    Returns: an iterator that is already filtered.

 The time complexity of the lambda function is constant, O(1)

bir fonksiyonu generator yapmak için yield kelimesi kullanılır
generator fonksiyonlar return değeri iterator object olur

Generator fonksiyonlar her kullanıldığında yield saolsun bir öncekine nazaran next değişkene geçer (iterable özellik)

yield kullanıldığında o değişkenler memory de yer kaplamaz Havada durur gibi düşünülebilir sadece ihtiyaç anında kullanılabilir
Ama bellekte tutulmadığı için değişken değeri için her seferinde en baştan alınır

iterator: iterasyon yapılacak liste, dizi veya başka bir iterable tür döndürür (list tuple felan)