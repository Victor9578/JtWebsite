from MyQR.mylibs.data import byte_encoding
from PIL.Image import register_save
import openpyxl
from MyQR import myqr
from openpyxl.drawing.image import Image
from openpyxl import load_workbook
import copy,os
from os import mkdir, read, write

from openpyxl.workbook.workbook import Workbook

i = input('输入i:')
try:
    mkdir('{}'.format(i))
except:
    print('目录存在')
path_st = r'{}\{}.xlsx'.format(i,i)
path_png = r'{}\{}.png'.format(i,i)

word = 'http://jt.jaywxl.asia/'+str(i)+'.html'
myqr.run(word,save_name=path_png)

bk = load_workbook('jt/请假条.xlsx')
st = bk.worksheets[0]
img = Image(path_png)
img.width,img.height=(150,150)
img1 =copy.copy(img)
st.add_image(img,'D6')
st.add_image(img1,'D22')
bk.close()
bk.save(path_st)
print(type(path_st))
