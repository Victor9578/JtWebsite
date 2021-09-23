from flask import Flask,render_template,redirect
from flask.globals import request
from jt import qjt
from flask_split import split

app=Flask('jay',static_folder='static',template_folder='templates')

@app.route('/')
def hello_world():
    return render_template('qjt.html')

@app.route('/xinxi', methods=['post'])
def xinxi():
    print(request.form.getlist)
    i = request.form.get('i')
    i = str(i)
    mz = request.form.get('mz')
    dd = request.form.get('dd')
    yy = request.form.get('yy')
    qsm =request.form.get('qsm')
    qs,qm = str(qsm).split(':')
    print((qsm))
    zsm = request.form.get('zsm')
    zs,zm = str(zsm).split(':')
    tx = request.form.get('tx')
    qjt.jiatiao(i,mz,dd,yy,qs,qm,zs,zm,tx)
    return  redirect(('http://jt.jaywxl.asia/jt/{}/{}.xlsx').format(i,i))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9578)
