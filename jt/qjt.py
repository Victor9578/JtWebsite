from mimetypes import encodings_map
from re import I, UNICODE
from MyQR.mylibs.ECC import encode
import openpyxl,datetime,os
from openpyxl.workbook.workbook import Workbook
from openpyxl.drawing.image import Image
from os import mkdir, read
from bs4  import BeautifulSoup
from MyQR import  myqr
import copy,sys

def jiatiao(i,mz,dd,yy,qs,qm,zs,zm,tx):
    sq = (datetime.datetime.now()-datetime.timedelta(hours=2)).strftime('%Y/%m/%d %H:%M')
    sqh = (datetime.datetime.now()-datetime.timedelta(hours=2)).strftime('%Y-%m-%d %H:%M')
    qj1 = datetime.datetime.now().strftime('%Y-%m-%d')+' '+qs+':'+qm+':'+'00'
    qj1h = datetime.datetime.now().strftime('%Y-%m-%d')+' '+qs+':'+qm
    qj2 = datetime.datetime.now().strftime('%Y-%m-%d')+' '+zs+':'+zm+':'+'00'
    qj2h = datetime.datetime.now().strftime('%Y-%m-%d')+' '+zs+':'+zm
    qj = qj1+'-'+qj2
    sp = (datetime.datetime.now()-datetime.timedelta(hours=2)+datetime.timedelta(minutes=5)).strftime('%Y/%m/%d %H:%M')
    sph = (datetime.datetime.now()-datetime.timedelta(hours=2)+datetime.timedelta(minutes=5)).strftime('%Y-%m-%d %H:%M')
    try:
        mkdir('{}'.format(i))
    except:
        print('目录存在')
    path_html = r'{}/{}.html'.format(i,i)
    path_st = r'{}/{}.xlsx'.format(i,i)
    path_jpg = r'{}/{}.jpg'.format(i,i)

    with open('/data/website/jt/请假条.html','r',encoding="utf-8") as qjt:
        qjthd = qjt.read()
    sop = BeautifulSoup(qjthd,'lxml')

    data = [qj1h,qj2h,sqh,dd]
    n = 0
    for t in [1,2,4,6]:
        tag=sop.find_all('div',class_='listr')[t]
        tag.string = str(data[n])
        n = n+1

    tagsp = sop.find_all('div')[-3]
    tagsp.string = str(sph)
    tsgmz = sop.find('div',class_='header-rt')
    tsgmz.string = str(mz)
    tsgyy = sop.find('section',class_='list-center')
    tsgyy.string = str(yy)
    tsgimg = sop.find('img')
    if tx=='':
            quit
    else:
            tsgimg['src']=tx
    with open(path_html, "w",encoding='utf-8') as file:
        file.write(sop.prettify())

    # transport=paramiko.Transport('159.75.80.89',22)
    # transport.connect(username='root',password='Wxl10191019')
    # sftp=paramiko.SFTPClient.from_transport(transport)
    # #上传，下载文件  包含文件名
    # sftp.put(path_html,'/data/jay/{}.html'.format(i))
    # transport.close()

    word = 'http://jt.jaywxl.asia/jt/'+path_html
    myqr.run(word,save_name=path_jpg)

    bk = openpyxl.load_workbook('/data/website/jt/请假条.xlsx')
    st = bk['Sheet1']
    st['B4']=sq
    st['B20'] = sq
    st['B5'] = qj
    st['B21'] =qj
    st['B10'] = sp
    st['B26'] = sp
    st['B2'] = mz
    st['B18'] = mz
    st['A6'] = yy
    st['A22'] = yy
    st['D2'] = i
    st['D18'] = i
    img = Image(path_jpg)
    img.width,img.height=(150,150)
    img1 =copy.copy(img)
    st.add_image(img,'D6')
    st.add_image(img1,'D22')
    bk.template = False
    bk.save(path_st)

    os.remove(path_jpg)


# if __name__ =='__main__':
#     # i = (input('请输入学号:'))
#     # mz = (input('输入请假姓名：'))
#     # yy = (input('请输入请假原因：'))
#     # qs,qm = (input('请输入起始时间 {加冒号}:').split(':'))
#     # zs,zm = (input('请输入终止时间 {加冒号}:').split(':'))
#     # dd = input('请输入请假地点：')
#     # tx = input('请输入头像链接:')
# dzjiatiao()
# shangchuan()
# qrcode()
# jiatiao()



