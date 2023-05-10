from flask import *
from src.dbconnection import *
from src.tsp import tsp_nearest_neighbor
app = Flask(__name__)

@app.route('/login',methods=['post'])
def login():
    username=request.form['username']
    password=request.form['password']
    qry="select * from  login where username=%s and password=%s"
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
        return jsonify({"task":"invalid"})
    else:
        type=res['type']
        id=res['login_id']
        return  jsonify({'task':'valid','id':id,'type':type})


@app.route('/userreg',methods=['post'])
def userreg():
    fname=request.form['fname']
    lname=request.form['lname']
    place=request.form['place']
    post=request.form['post']
    pin=request.form['pin']
    phone=request.form['phone']
    email=request.form['email']
    username=request.form['username']
    password=request.form['password']
    qry="insert into login values(Null,%s,%s,'user')"
    val=(username,password)
    id=iud(qry,val)
    qry1="insert into user values (Null,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(id,fname,lname,place,post,pin,phone,email)
    iud(qry1,val)
    return jsonify({"task":"success"})


@app.route('/sendnotification',methods=['post'])
def sendnotification():
    did=request.form['did']
    uid=request.form['uid']
    qry="insert into pickup_notification values(Null,%s,%s,curdate())"
    val=(did,uid)
    iud(qry,val)
    return jsonify({"task":"success"})



@app.route('/sendpickupnotification1',methods=['post'])
def sendnotification1():
    did=request.form['uid']
    lid=request.form['lid']
    qry="insert into pickup_notification values(Null,%s,%s,curdate())"
    val=(lid,did)
    iud(qry,val)
    return jsonify({"task":"success"})



@app.route('/usersendnotification',methods=['post'])
def usersendnotification():
    did = request.form['did']
    uid = request.form['lid']
    noti = request.form['notification']

    qry = "insert into notification values(Null,%s,%s,curdate(),'pending',%s)"
    val = (uid,did,noti)
    iud(qry, val)
    return jsonify({"task": "success"})


@app.route('/ViewReplay',methods=['post'])
def ViewReplay():
    did = request.form['lid']
    qry="SELECT * FROM `complaint` WHERE `uid`=%s"
    val=selectall2(qry,did)
    return jsonify(val)







@app.route('/sendcomplaint',methods=['post'])
def sendcomplaint():

    uid = request.form['lid']
    noti = request.form['complaint']

    qry = "INSERT INTO `complaint` VALUES(NULL,%s,%s,CURDATE(),'pending')"
    val = (uid,noti)
    iud(qry, val)
    return jsonify({"task": "success"})

@app.route('/update_status',methods=['post'])
def update_status():
    Notification_id = request.form['Notification_id']
    status = request.form['status']
    qry="UPDATE `notification` SET `status`=%s WHERE `Notification_id`=%s"
    val=(status,Notification_id)
    iud(qry, val)
    return jsonify({"task": "success"})


@app.route('/Viewassingnedplaces',methods=['post'])
def Viewassingnedplaces():
    lid=request.form['lid']
    qry="SELECT `assign`.`Place_id`,`assign`.`Date`,`places`.`Place`,`places`.`Latitude`,`places`.`Longitude`  FROM assign  JOIN `places`ON `places`.`Place_id`=`assign`.`Place_id`WHERE `assign`.Driver_id=%s"
    res=selectall2(qry,lid)
    return jsonify(res)

@app.route('/viewuser',methods=['post'])
def Viewuser():
    lid=request.form['lid']
    qry="SELECT * FROM `user`  JOIN `assign`ON `user`.`Place`= `assign`.`Place_id`  WHERE `assign`.`Driver_id` =%s"
    res=selectall2(qry,lid)
    return jsonify(res)


@app.route('/Viewplaces',methods=['post'])
def Viewplaces():
    qry="select * from places "
    res=selectall(qry)
    return jsonify(res)

@app.route('/Viewusernotification',methods=['post'])
def Viewusernotification():
    lid=request.form['lid']
    qry="SELECT * FROM notification JOIN `user`ON `user`.`Login_id`=`notification`.`User_id` WHERE `Driver_id`=%s"
    res=selectall2(qry,lid)
    return jsonify(res)


@app.route('/Viewpickup_notification',methods=['post'])
def Viewpickup_notification():
    lid = request.form['lid']
    qry = "SELECT * FROM `pickup_notification` JOIN `driver` ON `driver`.`login_id`=`pickup_notification`.`Driver_id` WHERE `pickup_notification`.`User_id`=%s"
    res = selectall2(qry, lid)
    return jsonify(res)


@app.route('/Viewproductbook',methods=['post'])
def Viewproductbook():
    qry = "select * from product "
    res = selectall(qry)
    print(res)
    return jsonify(res)

@app.route('/viewdriver',methods=['post'])
def viewdriver():
    lid=request.form['lid']

    qry = "SELECT * FROM driver  JOIN `assign`ON `driver`.`login_id`= `assign`.`Driver_id` JOIN `user`ON `user`.`Place`=`assign`.`Place_id` WHERE `user`.`Login_id`=%s "
    res = selectall2(qry,lid)
    print(res)
    return jsonify(res)


@app.route('/Viewawareness_camp_info',methods=['post'])
def Viewawareness_camp_info():

    qry = "select * from camp"
    res = selectall(qry)
    print(res)
    return jsonify(res)

@app.route('/Booking_info',methods=['post'])
def Booking_info():
    lid = request.form['lid']
    pid = request.form['pid']
    qty = request.form['qty']
    qry = "INSERT INTO `booking_info` VALUES(NULL,%s,%s,%s,'pending')"
    iud(qry,(pid,lid,qty))
    return jsonify({"task":"success"})



@app.route('/Viewvideos',methods=['post'])
def Viewvideos():
    qry = "select * from videos "
    res = selectall(qry)
    return jsonify(res)




@app.route('/plan_route', methods=['post'])
def plan_route():
        print(request.form)
        lid=request.form['lid']


        lat = request.form['lat']
        lon = request.form['lon']

        qry = "SELECT `places`.`Place`,`Latitude`,`Longitude` FROM `places` JOIN `assign` ON `assign`.`Place_id`=`places`.`Place_id` WHERE `assign`.`Driver_id`=%s AND `Date`=CURDATE()"

        # val=(place)
        res = selectall2(qry,lid)
        print(res)

        location = [(float(lat), float(lon))]
        for i in res:
            city = (float(i['Latitude']), float(i['Longitude']))

            location.append(city)
        startcity = (float(lat), float(lon))
        shortest_route, shortest_distance = tsp_nearest_neighbor(location, startcity)
        print(shortest_route)
        print(shortest_route)
        print(shortest_route)
        cityname = []

        for i in range(1, len(shortest_route)-1):
            r = selectone("SELECT * FROM `places` WHERE `Latitude`=%s  AND `Longitude` =%s", shortest_route[i])
            cityname.append(r)
        print(shortest_distance)
        print(shortest_route, "uuuuuuuuuuuuuuuuuuu")





        return jsonify(cityname)



@app.route('/plan_route1', methods=['post','get'])
def plan_route1():
        print(request.form)
        lid,lat,lon=request.args.get("id").split(",")




        qry = "SELECT `places`.`Place`,`Latitude`,`Longitude` FROM `places` JOIN `assign` ON `assign`.`Place_id`=`places`.`Place_id` WHERE `assign`.`Driver_id`=%s AND `Date`=CURDATE()"

        # val=(place)
        res = selectall2(qry,lid)
        print(res)

        location = [(float(lat), float(lon))]
        for i in res:
            city = (float(i['Latitude']), float(i['Longitude']))

            location.append(city)
        startcity = (float(lat), float(lon))
        shortest_route, shortest_distance = tsp_nearest_neighbor(location, startcity)
        print(shortest_route)
        print(shortest_route)
        print(shortest_route)
        cityname = [{"Place":"My Location", 'Latitude': lat, 'Longitude': lon}]

        for i in range(1, len(shortest_route)-1):
            r = selectone("SELECT * FROM `places` WHERE `Latitude`=%s  AND `Longitude` =%s", shortest_route[i])
            cityname.append(r)
        print(shortest_distance)
        print(shortest_route, "uuuuuuuuuuuuuuuuuuu")





        return render_template("map.html",val=cityname)




@app.route('/LOCATION',methods=['post'])
def LOCATION():
    lid=request.form['lid']
    tid=request.form['latitude']
    com=request.form['longitude']

    qry = "SELECT * FROM `location` WHERE `did`=%s"
    res = selectone(qry,lid)

    if res is None:

        qry="INSERT INTO  `location` VALUES(NULL,%s,%s,%s)"
        val=(lid,tid,com)
        iud(qry,val)
        return jsonify({'task': 'success'})
    else:
        qry = "UPDATE `location`SET `lati`=%s,`longi`=%s WHERE `id`=%s"
        val = (tid, com, lid)
        iud(qry, val)
        return jsonify({'task': 'success'})







app.run(host='0.0.0.0',port=5000)

