#--------------------------init---------------------------------#
import os
import sys
from main import *
import builtins as __source__
import ctypes
abs, all, any, ascii, bin, bool, breakpoint, bytearray, bytes, callable, chr, classmethod, compile, complex, copyright, credits, delattr, dict, dir, divmod, enumerate, eval, exec, exit, filter, float, format, frozenset, getattr, globals, hasattr, hash, help, hex, id, input, int, isinstance, issubclass, iter, len, license, list, locals, map, max, memoryview, min, next, object, oct, open, ord, pow, print, property, quit, range, repr, reversed, round, set, setattr, slice, sorted, staticmethod, str, sum, super, tuple, type, vars, zip=range(73)
quitmain=0
#import os,sys,re,socket,file,threading,types,start,time,requests,datetime,random,shutil,__subprocess__,base64,bz2,bdb,binhex,builtins,cgi,chunk,cmath,cmd,code,email,enum,errno,gc,gzip,hashlib,json,keyword,lib2to3,mailbox,math,tkinter,pdb,pathlib,uu,urllib,urllib3,venv,zipfile,zipapp,zlib,zipimport
__shell__=None
__deepest__=1
__deep__=0
__found__=0
__runline__=0
__deep_name__=[]
__when__=False
__curry__=0
from environs import Env
env = Env()
path=__import__("copy").deepcopy(env.list('Path'))
path.append(';'+os.getcwd()+'\\script;')
path.append(os.getcwd()+';')

path=''.join(path)
#--------------------------func---------------------------------#
def __type__():
    global __shell__
    __shell__=__shell__.replace('"','String("')
    __shell__=__shell__.replace('"','")')
    __shell__=__shell__.replace('<','Stack(')
    __shell__=__shell__.replace('>',')')
    __shell__=__shell__.replace('[','List(')
    __shell__=__shell__.replace(']',')')
    __shell__=__shell__.replace('$','Null()')
def __struct__(__shell__,__deep__):
    __struct_list__=[]
    __shell_deep__=' '
    if __shell_deep__!='':
        while __shell_deep__[0]!='}':
            __source__.print('  '*__deep__,end='')
            __shell_deep__=__source__.input('>')
            if __shell_deep__[-1]=='{':
                __struct_temp__=__struct__(__shell_deep__[:-1],__deep__+1)
                __struct_list__.append(__struct_temp__)
            else:
                __struct_list__.append(__shell_deep__)
    else:
        pass
    __shell__=__source__.list(__shell__)
    try:
        __shell__.insert(__shell__.index('('),'.__struct__')
        __shell__.insert(__shell__.index(')'),',__struct_list__[:-1]')
        __shell__=''.join(__shell__)
    except:
        __source__.print('  <Lizerd> Error\n\t\tinvalid syntax')
    try:
        if __deep__==1:
            __source__.eval(__shell__)
        elif __deep__!=1:
            __shell__=__shell__.split(',')
            __shell__[-1]=','+__source__.str(__struct_list__[:-1])+')'
            __shell__=''.join(__shell__)
            return __shell__
    except BaseException as b:
        try:
            if __shell__.split(' ')[0] in __source__.__import__('keyword').kwlist:
                __source__.print('  <Lizerd> Error\n\t\tinvalid syntax')
            else:
                __source__.exec(__shell__)
        except:
            if __shell__=='':
                pass
            elif __shell__==None:
                pass
            elif __shell__[0]=='@':
                pass
            try:
                if __shell__[-1]=='{':
                    __struct__(__shell__[:-1],__deep__+1)
            except:
                __source__.print('  <Lizerd> '+'Error'+'\n\t\t'+__source__.str(b))
            else:
                __source__.print('  <Lizerd> '+'Error'+'\n\t\t'+__source__.str(b))
def __struct_file__(__shell__,__deep__,__line__,__found__):
    global __deepest__,__curry__
    __struct_list__=[]
    __deepest__+=1
    try:
        while __runline__!=__found__[-1]:
            __struct_list__.append(__source__.next(__line__))
    except:
        __source__.print('  <Lizerd> Error in struct\n\t\tinvalid syntax(want \'{\' or \'}\')')
    return
    __shell__=__source__.list(__shell__)
    try:
        __shell__.insert(__shell__.index('('),'.__struct__')
        __shell__.insert(__shell__.index(')'),',__struct_list__[:-1]')
        __shell__=''.join(__shell__)
    except:
        __source__.print('  <Lizerd> Error in struct\n\t\tinvalid syntax(want \'(\' or \')\')')
    try:
        if __deep__==1:
            __source__.eval(__shell__)
        else:
            __shell__=__shell__.split(',')
            __shell__[-1]=','+__source__.str(__struct_list__[:-2])+')'
            __shell__=''.join(__shell__)
            return __shell__
    except BaseException as b:
        try:
            if __shell__.split(' ')[0] in __source__.__import__('keyword').kwlist:
                __source__.print('  <Lizerd> Error in struct\n\t\tinvalid syntax')
            else:
                __source__.exec(__shell__)
        except:
            try:
                if __shell__=='':
                    pass
                elif __shell__==None:
                    pass
                elif __shell__[0]=='@':
                    pass
                elif __shell__[-1]=='{':
                    __struct_file__(__shell__[:-1],__deep__+1,__line__,__found__[:-1])
                else:
                    __source__.print('  <Lizerd> '+'Error in struct'+'\n\t\t'+__source__.str(b))
            except:
                __source__.print('  <Lizerd> '+'Error in struct'+'\n\t\t'+__source__.str(b))
    __curry__+=1
def __main_file__(__line__,__args__):
    global __deep__,__shell__,__deep_name__,__source__,__found__,__source__,__curry__
    while True:
        #-f C:\\Users\\tcy\\Desktop\\lizerdTestStruct.li
        try:
            __shell__=__source__.next(__line__)
            import builtins as __source__
            try:
                __temp__=__source__.eval(__shell__)
            except BaseException as c:
                try:
                    if __shell__.split(' ')[0] in __source__.__import__('keyword').kwlist:
                        __source__.print('  <Lizerd> Error in running\n\t\tinvalid syntax')
                    else:
                        __source__.exec(__shell__)
                except:
                    if __shell__=='':
                        pass
                    elif __shell__[0]=='@':
                        pass
                    try:
                        if __shell__.strip()[-1]=='{':
                            __struct_file__(__shell__[:-1],1,__line__,__found__)
                        elif __curry__ in __found__:
                            pass
                    except:
                        __source__.print('  <Lizerd>  Error in  running''\n\t\t'+__source__.str(c))
                    if __curry__ in __found__:
                        pass
            __curry__+=1
        except StopIteration:
            break
    __source__.print('---------END---------')
def __main__(inp='>'):
    global __deep__,__shell__
    import builtins as __source__
    while True:
        try:
            __shell__=__source__.input(inp)
            __type__()
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
                elif __shell__==None:
                    pass
                elif __shell__[0]=='@':
                    continue
                elif __shell__[-1]=='{':
                    __struct__(__shell__[:-1],1)
                else:
                    __source__.print('  <Lizerd> '+'Error'+'\n\t\t'+__source__.str(c))
                    continue
#-----------------------------------main---------------------------#
import argparse
__parser__ = argparse.ArgumentParser()
__parser__.add_argument("--code", "-c", type=__source__.str, help="to run a line of code", default="")
__parser__.add_argument("--file", "-f", type=__source__.str, help="to run a file by lizerd", default="")
__parser__.add_argument("--args", "-a", type=__source__.dict, help="to run a file by lizerd with some args", default={})
__parser__.add_argument("--package", "-p", type=__source__.str, help="to run a LizerdPackage by lizerd", default="")
__parser__.add_argument("--set_working_directory",'-s' , type=__source__.str, help="to run a LizerdPackage by lizerd", default="")
__parser__.add_argument("--set_working_directory_current_directory", type=__source__.bool, help="to run a lizerd thar directory", default=False)
__args__ = __parser__.parse_args()
if __args__.code!='':
    __main_file__([__args__.code,'code end'])
    del argparse
elif __args__.file!='':
    with __source__.open(__args__.file) as __code__:
        __lines__=__code__.readlines()
        __runline__=__source__.len(__lines__)-1
        __found__=[i for i, x in __source__.enumerate(__lines__) if x.strip() == '}']
    with __source__.open(__args__.file) as __code__:
        __main_file__(__code__,__args__.args)
    del argparse
elif __args__.set_working_directory_current_directory!=False:
    import subprocess
    ret,val=subprocess.getstatusoutput("cd")
    if ret==1:
        __source__.print('  <Lizerd> Error\n\t\tcouldn\'t get working current directory',file=sys.stderr)
        del argparse,ret,val
    else:
        os.chdir(val)
        del argparse,ret,val
    __main__(__shell__)
elif __args__.set_working_directory!='':
    import subprocess
    ret,val=subprocess.getstatusoutput("cd")
    if ret==1:
        __source__.print('  <Lizerd> Error\n\t\tcouldn\'t get working current directory',file=sys.stderr)
        del argparse,ret,val
    else:
        os.chdir(val)
        del argparse,ret,val
    __main__(__shell__)
elif __args__.package!='':
    del argparse
    import zipfile as zf
    import sys
    if not os.path.isdir('LizerdPackageCache'):
        os.mkdir('LizerdPackageCache')
    with zf.ZipFile(__args__.package) as file:
        file.extractall('LizerdPackageCache')
    del file
    import copy
    getcwd=copy.deepcopy(os.getcwd())
    os.chdir(getcwd+'\\LizerdPackageCache\\scr')
    import yaml,hashlib
    with __source__.open(getcwd+'\\LizerdPackageCache\\init.yaml','rb') as yf:
        #-p F:\\Lizard\\Lizard_a00\\lizerdTestStruct.lp
        __init__=yaml.load(yf.read(),yaml.loader.FullLoader)
    del yf
    if 'SHA256' in __init__:
        __edit_time__=__source__.str(os.path.getmtime(__args__.package)).encode()
        with __source__.open(getcwd+'\\LizerdPackageCache\\command\\main\\'+__init__['name']+'.li','r') as sf:
            __lines__=sf.readlines()
        with __source__.open(getcwd+'\\LizerdPackageCache\\command\\main\\'+__init__['name']+'.li','r') as sf:
            __runline__=__source__.len(__lines__)-1
            __found__=[i for i, x in __source__.enumerate(__lines__) if x.strip() == '}']
            __fileSHA__=__source__.str(hashlib.sha256(__source__.open(getcwd+'\\LizerdPackageCache\\command\\main\\'+__init__['name']+'.li').read().encode()+__edit_time__).digest())
            __source__.print('',__fileSHA__,'\n',__source__.eval(__init__['SHA256']))
            if __fileSHA__==__source__.eval(__init__['SHA256']):
                with __source__.open(getcwd+'\\LizerdPackageCache\\command\\main\\'+__init__['name']+'.li','r') as __file__:
                    __main_file__(__file__,__args__.args)
            else:
                __untrusting__=__source__.input('Because of different SHA256 value,it is UNTRUSTING.it may be edited.Do you want to run it?( y | anonther )')
                if __untrusting__=='y':
                    with __source__.open(getcwd+'\\LizerdPackageCache\\command\\main\\'+__init__['name']+'.li','r') as __file__:
                        __shell__=__file__
                        __main_file__(__args__.args)
                else:
                    __source__.print('---------NOTRUN---------')
    else:
        __main_file__(__source__.open(getcwd+'\\LizerdPackageCache\\command\\main\\'+__init__['name'].encode()+'.li','r'),__args__.args)
    import os
    import shutil
    os.chdir(getcwd)
    shutil.rmtree('LizerdPackageCache')
else:
    __version__='22y10m17d'
    import builtins as __source__
    __source__.print("Lizerd  version:"+__version__+"  Copyright:Lizerd Team  2021 - 2025  official:lizerd.top")
    __main__()
################################################################################
