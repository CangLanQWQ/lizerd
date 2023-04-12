import os
import sys
import window
import web
import start
import stdio
import file
import pygame
import bar
import arithmetic
import Carray
import Ctype
sys.modules['window']=window
sys.modules['web']=web
sys.modules['start']=start
sys.modules['stdio']=stdio
sys.modules['file']=file
sys.modules['bar']=bar
sys.modules['arithmetic']=arithmetic
sys.modules['Ctype']=Ctype
sys.modules['Carray']=Carray
__path__=os.getcwd()
################################################################################
__path__=os.getcwd()
def expand(value,lens):
    value.__expand__(None,lens)
def __setattr__(self,name,value):
    raise typeError("invalid syntax!")
class when:
    def __struct__(v,__struct_list__):
        if v:
            for __shell__ in __struct_list__:
                try:
                    __temp__=__source__.eval(__shell__)
                    if __temp__ != None:
                        __source__.print(__temp__)
                except BaseException as c:
                    try:
                        if __shell__.split(' ')[0] in __source__.__import__('keyword').kwlist:
                            __source__.print('  <Lizerd> Error\n\t\tinvalid syntax')
                        else:
                            __source__.exec(__shell__)
                    except:
                        if __shell__=='':
                            pass
                        elif __shell__[0]=='@':
                            pass
                        elif __shell__[-1]=='{':
                            __struct_list__=[]
                            other=False
                            __struct_list__.append(__shell__)
                            for __shell__ in __struct_list__:
                                __struct_file__(__shell__,1,__line__)
                        else:
                            __source__.print('  <Lizerd> line '+__source__.str(__line__+1)+' Error'+'\n\t\t'+__source__.str(c))
                            break
class loop:
    def __struct__(v,__struct_list__):
        for __num__ in range(v):
            for __shell__ in __struct_list__:
                try:
                    __temp__=__source__.eval(__shell__)
                    if __temp__ != None:
                        __source__.print(__temp__)
                except BaseException as c:
                    try:
                        if __shell__.split(' ')[0] in __source__.__import__('keyword').kwlist:
                            __source__.print('  <Lizerd> Error\n\t\tinvalid syntax')
                        else:
                            __source__.exec(__shell__)
                    except:
                        if __shell__=='':
                            pass
                        elif __shell__[0]=='@':
                            pass
                        elif __shell__[-1]=='{':
                            __struct_list__=[]
                            other=False
                            __struct_list__.append(__shell__)
                            for __shell__ in __struct_list__:
                                __struct_file__(__shell__,1,__line__)
                        else:
                            __source__.print('  <Lizerd> line '+__source__.str(__line__+1)+' Error'+'\n\t\t'+__source__.str(c))
                            break
class cycle:
    def __struct__(v,__struct_list__):
        for __num__ in v:
            for __shell__ in __struct_list__:
                try:
                    __temp__=__source__.eval(__shell__)
                    if __temp__ != None:
                        __source__.print(__temp__)
                except BaseException as c:
                    try:
                        if __shell__.split(' ')[0] in __source__.__import__('keyword').kwlist:
                            __source__.print('  <Lizerd> Error\n\t\tinvalid syntax')
                        else:
                            __source__.exec(__shell__)
                    except:
                        if __shell__=='':
                            pass
                        elif __shell__[0]=='@':
                            pass
                        elif __shell__[-1]=='{':
                            __struct_list__=[]
                            other=False
                            __struct_list__.append(__shell__)
                            for __shell__ in __struct_list__:
                                __struct_file__(__shell__,1,__line__)
                        else:
                            __source__.print('  <Lizerd> line '+__source__.str(__line__+1)+' Error'+'\n\t\t'+__source__.str(c))
                            break
class repeat:
    def __struct__(v,__struct_list__):
        while v:
            for __shell__ in __struct_list__:
                try:
                    __temp__=__source__.eval(__shell__)
                    if __temp__ != None:
                        __source__.print(__temp__)
                except BaseException as c:
                    try:
                        if __shell__.split(' ')[0] in __source__.__import__('keyword').kwlist:
                            __source__.print('  <Lizerd> Error\n\t\tinvalid syntax')
                        else:
                            __source__.exec(__shell__)
                    except:
                        if __shell__=='':
                            pass
                        elif __shell__[0]=='@':
                            pass
                        elif __shell__[-1]=='{':
                            __struct_list__=[]
                            other=False
                            __struct_list__.append(__shell__)
                            for __shell__ in __struct_list__:
                                __struct_file__(__shell__,1,__line__)
                        else:
                            __source__.print('  <Lizerd> line '+__source__.str(__line__+1)+' Error'+'\n\t\t'+__source__.str(c))
                            break
class error:
    def __init__(self,code):
        self.code=code
    class typeError(TypeError): pass
    def __setattr__(self,name,value):
        raise typeError("invalid syntax!")
    def __lt__(self,errorc):
        self.errorc=errorc
    def __gt__(self,allc):
        self.allc=allc
    def __lshift__(self,error):
        try:
            code()
        except error:
            errorc()
        finally:
            allc()
def quit():
    exit()

class Boolean:
    def __setattr__(self,name,value):
        self.value=bool(value)
        self.__dict__[name]=value
class Null:
    def __bool__():
        return 0
    def __int__():
        return 0;
    def __str__():
        return '$'
class List:
    def __init__(self,*list):
        self._list=[]
        for i in list:
            self._list.append(i)
        self.cur=0
        self.len=len(self._list)
        self.size=len(self._list)-1
    def append(self,*list):
        for i in list:
            self.list.append(i)
    def __setitem__(self,index,value):
        self._list[index]=value
    def __delitem__(self,index):
        del self._list[index]
    def __getitem__(self,index):
        self._list[index]=value
    def __len__(self):
        return len(self._list)
    def __lshift__(self,n):
        self.cur-=n
    def __rshift__(self,n):
        self.cur+=n
    def __invert__(self):
        return self._list[self.cur]
    def __repr__(self):
        return repr(self._list)
    def __le__(self, value):
        self._list.append(value)
    def __gt__(self, other):
        self._list.pop()
    def __xor__(self,index):
        return self._list[index]
class Number(int):
    pass
class String:
    def __setattr__(self,name,value):
        self.value=value
        self.__dict__[name]=value
class Stack:
    def OutofMemory(BaseException): pass
    def __init__(self,lens):
        self.value=[]
        self.len=lens
        self.end=0
    def append(self,value):
        if self.len < end:
            raise OutofMemory("out of memory")
        else:
            self.value.append(value)
            self.end+=1
    def get(self):
        if self.len < 0:
            raise OutofMemory("out of memory")
        else:
            return self.value[-1]
    def delete(self):
        if self.len < end:
            raise OutofMemory("out of memory")
        else:
            del self.value[-1]
            self.end-=1
    def pop(self):
        if self.len < end:
            raise OutofMemory("out of memory")
        else:
            return self.value[-1]
            del self.value[-1]
            self.end-=1
class Type:
    def __init__(self,name,bases):
        self.name=name
        self.bases=bases
        self.type=type(name,bases,{})
    class typeError(TypeError): pass
    def __setattr__(self,name,value):
        raise typeError("invalid syntax!")
    def __str__(self):
        return str(self.type)
    def __repr__(self):
        return str(self.type)
    def __lshift__(self,function):
        for k,v in function:
            exec('self.type.'+str(k)+'='+str(v))
class Function:
    def __init__(self,name,*lst,**kwargs):
        self.lst=lst
        self.kwargs=kwargs
        self.name=name
        self.fct=[]
    class typeError(TypeError): pass
    def __setattr__(self,name,value):
        raise typeError("invalid syntax!")
    def __repr__(self):
        return '< function '+str(self.name)+' >'
    def __call__(self,*lst,**kwargs):
        import copy
        diccopy.copy(kwargs)
        lst={}
        for k,v in kwargs:
            self.kwargs[k]=kwargs[k]
        for k,v in self.kwargs:
            exec(k+"="+v)
        for i in range(len(lst)-1):
            lst[self.lst[i]]=lst[i]
        for k,v in list:
            exec(k+'='+v)
        for i in self.fct:
            try:
                eval(i)
            except:
                try:
                    exec(i)
                except:
                    if i[0]=="@":
                        pass

        

class TraversalList:
    def __init__(self,val):
        self.val=val
        self.iter=iter(val)
    class typeError(TypeError): pass
    def __setattr__(self,name,value):
        raise typeError("invalid syntax!")
    def __setattr__(self,name,value):
        raise TypeError("mustn't write")
    def __repr__(self):
        return "::"+str(val)[1:-2]+"::"
    def __str__(self):
        return "::"+str(val)[1:-2]+"::"
def iteration(val):
    return next(val)
def length(val):
    return val.__len__()
def include(val=None,help=False):
    import sys,os
    if not val:
        if help:
            print("Why this is disorder?\n\tBecause there are few people here.Can you join us?We're Tilesiw.")
        return None
    try:
        with open(os.getcwd()+'\\lib\\'+val+".lm",'r') as mod:
            for i in mod.readlines():
                try:
                    eval(i)
                except:
                    try:
                        exec(i)
                    except:
                        if i[0]=="@":
                            pass
                try:
                    return dict(eval('__clude__'))
                except:
                    pass
    except:
         with open(os.getcwd()+'\\lib\\'+val+'\\main.lm','r') as mod:
            for i in mod.readlines():
                try:
                    eval(i)
                except:
                    try:
                        exec(i)
                    except:
                        if i[0]=="@":
                            pass
                try:
                    return dict(eval('__clude__'))
                except:
                    pass
                
del os
