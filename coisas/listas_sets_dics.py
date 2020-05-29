# coding: utf-8

s = set(x for x in range(1000))
l = [x for x in range(1000)]
from random import randint 
get_ipython().run_line_magic('time', '-n 1000 -r 10 randint(1,100) in s')
get_ipython().run_line_magic('time', '-n 1000 -r 10  randint(1,100) in s')
get_ipython().run_line_magic('time', '-n 1000 -r 10 []')
get_ipython().run_line_magic('timeit', '-n 1000 -r 10  randint(1,100) in s')
get_ipython().run_line_magic('timeit', '-n 1000 -r 10  randint(1,100) in l')
l = [x for x in range(1000000)]
s = set(x for x in range(1000000))
get_ipython().run_line_magic('timeit', '-n 1000 -r 10  randint(1,100) in s')
l = [x for x in range(1000000)]
get_ipython().run_line_magic('timeit', '-n 1000 -r 10  randint(1,100) in l')
def random_string(l):
    carac = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    string = ''
    for i in range(l):
        letra = randint(0,25)
        string += carac[letra]
    return string 
    
random_string(2)
random_string(2)
random_string(4)
random_string(4)
random_string(4)
l_str = [random_string(10) for x in range(1000)]
dic_str = [str(x) : random for x in range(1000)]
dic_str = [str(x):random_string(10) for x in range(1000)]
dic_str = [str(x) : random_string(10) for x in range(1000)]
dic_str = {str(x) : random_string(10) for x in range(1000)}
dic_st
r
dic_str
get_ipython().run_line_magic('timeit', '-n 1000 -r 10 randint(1,1000) in l_str')
dic_str = {x : random_string(10) for x in range(1000)}
get_ipython().run_line_magic('timeit', '-n 1000 -r 10 randint(1,1000) in dic_str')
ord('a')
chr(97)
