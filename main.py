from __future__ import print_function
import pyximport
pyximport.install()
from pure import test
from extention import fastest_dec 
from extention import extend
from extention import fastest

if __name__ == '__main__':
    fastest_dec.outer_4(99999999)
    fastest.outer_3(99999999)
    extend.outer_2(99999999)
    test.outer_1(99999999)
    
