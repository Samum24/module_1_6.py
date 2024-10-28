from ftplib import print_line

my_dict={'Michael':1974,'Alina':1997,'Viktor':1949}
print(my_dict)
print(my_dict['Viktor'])
print(my_dict.get('Ira'))
my_dict.update(({'Ira':1976,'Katy':1954}))
print(my_dict)
print(my_dict.get('Kiril'))
a = my_dict.pop('Katy')
print(a)
print(my_dict)

my_set={5,8,3,8,2,7,9,3,1,2}
print(my_set)
my_set.add('Kiwi')
my_set.add('Cery')
print(my_set)
my_set.discard('Cery')

print(my_set)





















