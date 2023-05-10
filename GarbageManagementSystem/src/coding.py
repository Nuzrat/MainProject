from flask import *
from src.dbconnection import *
app = Flask(__name__)
import os
from werkzeug.utils import secure_filename

app.secret_key="nmjfdjkfjk"


@app.route('/')
def login():
    return render_template("loginindex.html")



@app.route('/logincode',methods=['post'])
def logincode():
    un=request.form['textfield']
    ps=request.form['textfield2']
    qry="Select *from login where username=%s and Password=%s"
    val=(un,ps)
    res=selectone(qry,val)
    if res is None:
        return'''<script>alert("invalid");window.location='/'</script>'''
    elif res['type']=='admin':
        return redirect('/AdminHome')
    else:
        return'''<script>alert("");window.location='/'</script>'''






@app.route('/AddPlace',methods=['get','post'])
def AddPlace():
    return render_template("AddPlace.html")

@app.route('/addplace_post',methods=['post'])
def addplace_post():
    place=request.form['textfield']
    latitude=request.form['textfield2']
    logitude=request.form['textfield3']


    q="INSERT INTO `places` VALUES (NULL,%s,%s,%s)"
    val=(place,latitude,logitude)
    res=iud(q,val)



    return '''<script>alert("Successfully Added");window.location='/ManagePlaces'</script>'''



@app.route('/deletePlace')
def deletePlace():
    id = request.args.get('id')
    qry="delete from places WHERE `Place_id`=%s"
    iud(qry,id)
    return '''<script>alert("Successfully Deleted");window.location='/ManagePlaces'</script>'''



@app.route('/editPlace',methods=['get','post'])
def editPlace():
    id = request.args.get('id')
    session['pid'] = id
    qry = "select * from places WHERE `Place_id`=%s"
    res = selectone(qry, id)
    print(res)
    return render_template("editPlace.html",val=res)

@app.route('/editPlace1',methods=['post'])
def editPlace1():
    place=request.form['textfield']
    latitude=request.form['textfield2']
    logitude=request.form['textfield3']


    q="UPDATE `places` SET `Place`=%s,`Latitude`=%s,`Logitude`=%s WHERE `Place_id`=%s"
    val=(place,latitude,logitude,session['pid'])
    res=iud(q,val)



    return '''<script>alert("Successfully Edited");window.location='/ManagePlaces'</script>'''















@app.route('/editplace_post',methods=['post'])
def editplace_post():
    place=request.form['textfield']
    latitude=request.form['textfield2']
    logitude=request.form['textfield3']


    q="INSERT INTO `places` VALUES (NULL,%s,%s,%s)"
    val=(place,latitude,logitude)
    res=iud(q,val)



    return '''<script>alert("Successfully Added");window.location='/ManagePlaces'</script>'''

@app.route('/AdminHome')
def AdminHome():
    return render_template("AdminHome.html")




@app.route('/AddProduct',methods=['get','post'])
def AddProduct():
    return render_template("AddProduct.html")


@app.route('/addproduct_post',methods=['post'])
def addproduct_post():
    product=request.form['textfield']
    type=request.form['textfield2']

    image=request.files['file']
    import time
    fn=time.strftime("%Y%m%d_%H%M%S")+".jpg"
    image.save("static/Product/"+fn)
    # fn=secure_filename(image.filename)
    # image.save(os.path.join('static/product',fn))


    q="INSERT INTO `product` VALUES (NULL,%s,%s,%s)"
    val=(product,type,fn)
    iud(q,val)
    return '''<script>alert("Successfully Added");window.location='/ManageProduct'</script>'''

@app.route('/deleteProduct',methods=['get','post'])
def deleteProduct():
    id = request.args.get('id')
    qry="delete from Product WHERE `Product_id`=%s"
    iud(qry,id)
    return '''<script>alert("Successfully deleted");window.location='/ManageProduct'</script>'''



@app.route('/editProduct',methods=['get','post'])
def editProduct():
    id = request.args.get('id')
    session['proid'] = id
    qry = "select * from Product WHERE `Product_id`=%s"
    res = selectone(qry, id)
    print(res)
    return render_template("editProduct.html",val=res)

@app.route('/editproduct_post',methods=['post'])
def editproduct_post():
    try:
        product=request.form['textfield']
        type=request.form['textfield2']
        image=request.files['file']
        import time
        fn=time.strftime("%Y%m%d_%H%M%S")+".jpg"
        image.save("static/Product/"+fn)
        # fn=secure_filename(image.filename)
        # image.save(os.path.join('static/product',fn))

        q="UPDATE `product` SET `Product`=%s,`Type`=%s,`Image`=%s WHERE `Product_id`=%s"
        val=(product,type,fn,session['proid'])
        iud(q,val)
        return '''<script>alert("Successfully edited");window.location='/ManageProduct'</script>'''
    except:
        product = request.form['textfield']
        type = request.form['textfield2']
        q = "UPDATE `product` SET `Product`=%s,`Type`=%s WHERE `Product_id`=%s"
        val = (product, type, session['proid'])
        iud(q, val)
        return '''<script>alert("Successfully edited");window.location='/ManageProduct'</script>'''





@app.route('/AddDriver',methods=['get','post'])
def AddDriver():
    return render_template("AddDriver.html")

@app.route('/adddriver_post',methods=['post'])
def adddriver_post():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    place=request.form['textfield3']
    post=request.form['textfield4']
    pin=request.form['textfield5']
    phone=request.form['textfield6']
    email=request.form['textfield7']
    username=request.form['textfield8']
    password=request.form['textfield9']


    q="INSERT INTO `login` VALUES (NULL,%s,%s,'driver')"
    val=(username,password)
    res=iud(q,val)

    qry="INSERT INTO `driver` VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    va=(str(res),fname,lname,place,post,pin,phone,email)
    iud(qry,va)
    return '''<script>alert("Successfully Added");window.location='/ManageDrivers'</script>'''

@app.route('/editDriver',methods=['get','post'])
def editDriver():
    id=request.args.get('id')
    session['did']=id
    qry="select * from driver WHERE `Driver_id`=%s"
    res=selectone(qry,id)
    print(res)
    return render_template("editDriver.html",val=res)

@app.route('/editdriver_post',methods=['post'])
def editdriver_post():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    place=request.form['textfield3']
    post=request.form['textfield4']
    pin=request.form['textfield5']
    phone=request.form['textfield6']
    email=request.form['textfield7']
    qry="UPDATE `driver` SET `F_name`=%s,`L_name`=%s,`Place`=%s,`Post`=%s,`Pin`=%s,`Phone`=%s,`Email_id`=%s WHERE `Driver_id`=%s"
    va=(fname,lname,place,post,pin,phone,email,session['did'])
    iud(qry,va)
    return '''<script>alert("Successfully Edited");window.location='/ManageDrivers'</script>'''



@app.route('/delete_Driver')
def delete_Driver():
    id=request.args.get('id')
    qry="DELETE FROM `driver` WHERE `login_id`=%s"
    iud(qry,id)
    qry1="DELETE FROM `login` WHERE `login_id`=%s"
    iud(qry1,id)
    return '''<script>alert("Successfully Deleted");window.location='/ManageDrivers'</script>'''



@app.route('/AddVideo',methods=['get','post'])
def AddVideo():
    return render_template("AddVideo.html")


@app.route('/AddVideo1',methods=['get','post'])
def AddVideo1():
    image=request.files['file']
    # import time
    # fn=time.strftime("%Y%m%d_%H%M%S")+".jpg"
    # image.save("static/Product/"+fn)
    fn=secure_filename(image.filename)
    image.save(os.path.join('static/product',fn))
    qry="INSERT INTO `videos` VALUES (NULL,%s)"
    val=(fn)
    iud(qry,val)
    return '''<script>alert("Successfully Added");window.location='/ManageVideos'</script>'''

@app.route('/Assign',methods=['post'])
def Assign():
    qry="select *from Places "
    res=selectall(qry)
    qry1="select *from driver"
    res1=selectall(qry1)
    return render_template("Assign.html",val=res,val1=res1)


@app.route('/Assign1',methods=['post'])
def Assign1():
    Place=request.form['select']
    driver=request.form['select2']
    qry="INSERT INTO `assign` VALUES(NULL,%s,%s,CURDATE(),'pending')"
    val=(driver,Place)
    iud(qry,val)
    return '''<script>alert("Successfully Assigned");window.location='/ManageAssign'</script>'''





@app.route('/Awareness_camp_info')
def Awareness_camp_info():
    qry="SELECT * FROM `camp`"
    res=selectall(qry)
    return render_template("Awareness_camp_info.html",val=res)

@app.route('/AwarenessCampAdd',methods=['post'])
def AwarenessCampAdd():
    return render_template("AwarenessCampAdd.html")

@app.route('/AwarenessCampAdd1',methods=['post'])
def AwarenessCampAdd1():
    name = request.form['textfield']
    CampDetails=request.form['textfield2']
    Date = request.form['textfield3']

    q = "INSERT INTO `camp`VALUES (NULL,%s,%s,%s)"
    val = (name,CampDetails,Date)
    iud(q, val)
    return '''<script>alert("Successfully Added");window.location='/Awareness_camp_info'</script>'''

@app.route('/deleteAwareness_camp_info',methods=['get','post'])
def deleteAwareness_camp_info():
    id = request.args.get('id')
    qry="delete from camp WHERE `Camp_id`=%s"
    iud(qry,id)
    return '''<script>alert("Successfully Added");window.location='/Awareness_camp_info'</script>'''


@app.route('/delete_video',methods=['get','post'])
def delete_video():
    id = request.args.get('id')
    qry="DELETE FROM `videos`WHERE `Video_id`=%s"
    iud(qry,id)
    return '''<script>alert("Successfully Deleted");window.location='/ManageVideos'</script>'''




@app.route('/editAwareness_camp_info')
def editAwareness_camp_info():
    id = request.args.get('id')
    session['campid'] = id
    qry = "select * from camp WHERE `Camp_id`=%s"
    res = selectone(qry, id)
    print(res)
    return render_template("editAwareness_camp_info.html",val=res)

@app.route('/editAwareness_camp_info2',methods=['post'])
def editAwareness_camp_info2():
    name = request.form['textfield']
    CampDetails=request.form['textfield2']

    q = "UPDATE `camp` SET `Camp`=%s,`Camp_details`=%s WHERE `Camp_id`=%s"
    val = (name,CampDetails,session['campid'])
    iud(q, val)
    return '''<script>alert("Successfully Added");window.location='/Awareness_camp_info'</script>'''







@app.route('/editAwarenessCampAdd',methods=['post'])
def editAwarenessCampAdd():
    return render_template("editAwarenessCampAdd.html")

@app.route('/editAwarenessCampAdd1',methods=['post'])
def editAwarenessCampAdd1():
    name = request.form['textfield']
    CampDetails=request.form['textfield2']
    Date = request.form['textfield3']

    q = "INSERT INTO `camp`VALUES (NULL,%s,%s,%s)"
    val = (name,CampDetails,Date)
    iud(q, val)
    return '''<script>alert("Successfully Added");window.location='/Awareness_camp_info'</script>'''


@app.route('/ManageDrivers')
def ManageDrivers():

    D="select *from driver"
    res=selectall(D)
    return render_template("ManageDrivers.html",data=res)



@app.route('/ManagePlaces')
def ManagePlaces():

    D="select *from places"
    res=selectall(D)
    return render_template("ManagePlaces.html",val=res)


@app.route('/ManageProduct')
def ManageProduct():
    D = "select *from product"
    res = selectall(D)
    return render_template("ManageProduct.html",val=res)

@app.route('/ManageVideos')
def ManageVideos():
    D = "select *from Videos"
    res = selectall(D)
    return render_template("ManageVideos.html",val=res)

@app.route('/ViewBoogingInfo')
def ViewBoogingInfo():
    qry="SELECT `booking_info`.*,`product`.`Product`,`user`.`F_name`,`L_name` FROM `booking_info` JOIN `product`ON `booking_info`.`Product_id`=`product`.`Product_id` JOIN `user`ON `user`.`Login_id`=`booking_info`.`User_id`"
    res=selectall(qry)
    return render_template("ViewBoogingInfo.html",val=res)

@app.route('/ViewUsers')
def ViewUsers():
    D = "select *from user"
    res=selectall(D)
    return render_template("ViewUsers.html",val=res)


@app.route('/ManageAssign')
def ManageAssign():

    D="SELECT `driver`.`F_name`,`L_name`,`places`.`Place`,`assign`.* FROM `driver` JOIN `assign` ON `assign`.`Driver_id`=`driver`.`login_id` JOIN `places` ON `places`.`Place_id`=`assign`.`Place_id`"
    res=selectall(D)
    return render_template("ManageAssign.html",data=res)

@app.route('/delete_Assign')
def delete_Assign():
    id = request.args.get('id')
    qry="delete from assign WHERE `Assign_id`=%s"
    iud(qry,id)
    return '''<script>alert("Successfully Deleted");window.location='/ManageAssign'</script>'''





app.run(debug=True)



