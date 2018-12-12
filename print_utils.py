import numpy as np
# support func
def ptype(x):
    print('>> type:',type(x))
    
def pshape(x):
    if type(x).__module__ == np.__name__:
        print('>> shape:',x.shape)
        
def pmin(x, name=''):
    if name!='':
        print('\n',name)
    ptype(x)
    pshape(x)
    
def pall(x):
    pmin(x)
    print('>> data:',x)