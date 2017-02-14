import AllClass
from sqlalchemy import orm
from sqlalchemy import create_engine
from PyQt5.QtWidgets import QTableWidgetItem

engine = create_engine('sqlite:///CLI SQLite', echo=False)
Session = orm.sessionmaker(bind=engine)

glfirmid=0
glfirmid1=0

glhikeid=0
glhikeid1=0

glmembind=0

glmembid=0
#заполняет таблицы
def table_appender(widget, t):

    def set_columns(len, pos):
        if pos == len-1:
            widget.setItem(widget.rowCount()-1, pos, QTableWidgetItem(t[pos]))
        else:
            widget.setItem(widget.rowCount()-1, pos, QTableWidgetItem(t[pos]))
            set_columns(len, pos+1)

    widget.insertRow(widget.rowCount())
    set_columns(widget.columnCount(), 0)

#Firms
#-----------------------------------------------------#
def addrowtofirms(*args):
    session=Session()
    firm = AllClass.Firm(*args)
    session.add(firm)
    session.commit()

def showrowinfirms():
    session=Session()
    firms= session.query(AllClass.Firm).all()
    session.commit()
    row=[]
    rowset=[]
    for firm in firms:
        row.append(str(firm.firm_id))
        row.append(firm.firm_name)
        row.append(str(firm.score))
        rowset.append(row)
        row=[]
    return rowset

def changefirmdb(i, val, b):
    session=Session()
    if b==1:
        session.query(AllClass.Firm).filter_by(firm_id=int(i)).update({"firm_name": val})
    if b==2:
        session.query(AllClass.Firm).filter_by(firm_id=int(i)).update({"score": int(val)})
    session.commit()

def deletefirmdb(delid):
    session=Session()
    session.query(AllClass.Firm).filter_by(firm_id=delid).delete()
    session.query(AllClass.Fr_to_Rt).filter_by(firm=delid).delete()
    session.query(AllClass.Guide).filter_by(firm=delid).delete()
    session.commit()

#Routes
#-----------------------------------------------------#

    session=Session()
    route = AllClass.Route(*args)
    session.add(route)
    session.commit()

def addfirm_to_rote(prc):
    global glfirmid
    session=Session()
    route= session.query(AllClass.Route).order_by(AllClass.Route.route_id.desc()).first()
    frtrt = AllClass.Fr_to_Rt(prc, glfirmid, route.route_id)
    session.add(frtrt)
    session.commit()

def showrowinroutes(inf):
    session=Session()
    t=[]
    for i in range(len(inf)):
        t.append(inf[i][0])
    routes= session.query(AllClass.Route).filter(AllClass.Route.route_id.in_(t))
    session.commit()
    row=[]
    rowset=[]
    for route in routes:
        row.append(str(route.route_id))
        row.append(route.name)
        row.append(route.country)
        row.append(route.difficult)
        if route.oxygen == 1:
            row.append("Y")
        else:
            row.append("N")
        row.append(str(route.length_km))
        rowset.append(row)
        row=[]
    for i in range(len(inf)):
        rowset[i].append(inf[i][1])
    return rowset

def changeroutedb( i, val, b):
    session=Session()
    if b==1:
        session.query(AllClass.Route).filter_by(route_id=int(i)).update({"name": val})
    if b==2:
        session.query(AllClass.Route).filter_by(route_id=int(i)).update({"country": val})
    if b==3:
        session.query(AllClass.Route).filter_by(route_id=int(i)).update({"difficult": val})
    if b==4:
        if val == "Y" or val == "y":
            intval=1
        if val == "N" or val == "n":
            intval=0
        session.query(AllClass.Route).filter_by(route_id=int(i)).update({"oxygen": intval})
    if b==5:
        session.query(AllClass.Route).filter_by(route_id=int(i)).update({"length_km": val})
    session.commit()

def deleteroutedb(delid):
    session=Session()
    session.query(AllClass.Route).filter_by(route_id=delid).delete()
    session.query(AllClass.Fr_to_Rt).filter_by(route=delid).delete()
    session.commit()

#Fr_to_Rt
#-----------------------------------------------------#
def firm_to_route(firmid):
    session=Session()
    routes = session.query(AllClass.Fr_to_Rt).filter_by(firm=firmid)
    session.commit()
    global glfirmid
    glfirmid=firmid
    routeinfo = []
    routesinfo = []
    for route in routes:
        routeinfo.append(route.route)
        routeinfo.append(str(route.price))
        routesinfo.append(routeinfo)
        routeinfo = []
    if routesinfo:
        return showrowinroutes(routesinfo)

#Guides
#-----------------------------------------------------#
def addrowtoguide(guid_name, guid_exp_y, age):
    global glfirmid1
    session = Session()
    if not glfirmid1==0:
        guide = AllClass.Guide(guid_name, guid_exp_y, age, glfirmid1)
        session.add(guide)
    session.commit()

def firm_to_guide(firmid):
    session=Session()
    guides = session.query(AllClass.Guide).filter_by(firm=firmid)
    session.commit()
    global glfirmid1
    glfirmid1=firmid
    guideinfo = []
    guidesinfo = []
    for guide in guides:
        guideinfo.append(str(guide.guid_id))
        guideinfo.append(guide.guid_name)
        guideinfo.append(str(guide.guid_exp_y))
        guideinfo.append(str(guide.age))
        guidesinfo.append(guideinfo)
        guideinfo = []
    if guidesinfo:
        return guidesinfo

def changeguidedb( i, val, b):
    session=Session()
    if b==1:
        session.query(AllClass.Guide).filter_by(guid_id=int(i)).update({"guid_name": val})
    if b==2:
        session.query(AllClass.Guide).filter_by(guid_id=int(i)).update({"guid_exp_y": int(val)})
    if b==3:
        session.query(AllClass.Guide).filter_by(guid_id=int(i)).update({"age": int(val)})
    session.commit()

def deleteguidedb(delid):
    session = Session()
    session.query(AllClass.Guide).filter_by(guid_id=delid).delete()
    session.commit()

#Hike
#-----------------------------------------------------#
def changecmbbox():
    list=[]
    session = Session()
    firms = session.query(AllClass.Firm).all()
    routes = session.query(AllClass.Route).all()
    frm=[]
    rt=[]
    for firm in firms:
        frm.append(firm.firm_name)
    for route in routes:
        rt.append(route.name)
    list.append(frm)
    list.append(rt)
    return list

def addrowtohike (frmnm, rtnm, date_start, date_end, transport):
    session = Session()
    frms=session.query(AllClass.Firm).filter_by(firm_name=frmnm)
    f=[]
    for frm in frms:
        f.append(frm.firm_id)
    rts=session.query(AllClass.Route).filter_by(name=rtnm)
    r=[]
    for rt in rts:
        r.append(rt.route_id)
    frtr1 = session.query(AllClass.Fr_to_Rt).filter(AllClass.Fr_to_Rt.firm.in_(f))
    frtr2 = session.query(AllClass.Fr_to_Rt).filter(AllClass.Fr_to_Rt.route.in_(r))
    id1=[]
    id2=[]
    for fr in frtr1:
        id1.append(fr.id)
    for fr in frtr2:
        id2.append(fr.id)
    id=0
    for a in id1:
        for b in id2:
            if a == b:
                id = a
    if not id==0:
        hike = AllClass.Hike(id, date_start, date_end, transport)
        session.add(hike)
        session.commit()
        sess = Session()
        lasthike = sess.query(AllClass.Hike).order_by(AllClass.Hike.hike_id.desc()).first()
        sess.commit()
        addguidestomembers(lasthike.hike_id)

def showrowinhikes():
    session=Session()
    hikes = session.query(AllClass.Hike).all()
    row=[]
    rowset=[]
    for hike in hikes:
        row.append(str(hike.hike_id))
        frrt=session.query(AllClass.Fr_to_Rt).filter_by(id=hike.id)
        for fr in frrt:
            f=session.query(AllClass.Firm).filter_by(firm_id=fr.firm)
            r=session.query(AllClass.Route).filter_by(route_id=fr.route)
            p=str(fr.price)
        for rts in r:
            row.append(rts.name)
            row.append(rts.country)
        for frm in f:
            row.append(frm.firm_name)
        row.append(p)
        row.append(str(hike.date_start))
        row.append(str(hike.date_end))
        for rts in r:
            row.append(rts.difficult)
        row.append(hike.transport)
        rowset.append(row)
        row=[]
    session.commit()
    return rowset

def changehikedb( i, val, b):
    session=Session()
    hk = session.query(AllClass.Hike).filter_by(hike_id=int(i))
    for h in hk:
        r=h.id
    fr = session.query(AllClass.Fr_to_Rt).filter_by(id=r)
    for s in fr:
        rt=s.route
    if b==4:
        session.query(AllClass.Fr_to_Rt).filter_by(id=r).update({"price": val})
    if b==5:
        session.query(AllClass.Hike).filter_by(hike_id=int(i)).update({"date_start": val})
    if b==6:
        session.query(AllClass.Hike).filter_by(hike_id=int(i)).update({"date_end": val})
    if b==7:
        session.query(AllClass.Route).filter_by(route_id=rt).update({"difficult": val})
    if b==8:
        session.query(AllClass.Hike).filter_by(hike_id=int(i)).update({"transport": val})
    session.commit()

def deletehikedb(delid):
    session = Session()
    deletefooddb(delid)
    deletememberdb(delid)
    session.query(AllClass.Hike).filter_by(hike_id=delid).delete()
    session.commit()

#Food
#-----------------------------------------------------#
def addrowtofood(type, number):
    global glhikeid
    session = Session()
    if not glhikeid==0:
        food = AllClass.Food(glhikeid, type, number)
        session.add(food)
    session.commit()

def hike_to_food(hikeid):
    session=Session()
    foods = session.query(AllClass.Food).filter_by(hike_id=hikeid)
    session.commit()
    global glhikeid
    glhikeid=hikeid
    foodinfo = []
    foodsinfo = []
    for food in foods:
        foodinfo.append(str(food.food_id))
        foodinfo.append(food.type)
        foodinfo.append(str(food.number))
        foodsinfo.append(foodinfo)
        foodinfo = []
    return foodsinfo

def changefooddb( i, val, b):
    session=Session()
    if b==1:
        session.query(AllClass.Food).filter_by(food_id=int(i)).update({"type": val})
    if b==2:
        session.query(AllClass.Food).filter_by(food_id=int(i)).update({"number": int(val)})
    session.commit()

def deletefooddb(delid):
    session = Session()
    session.query(AllClass.Food).filter_by(food_id=delid).delete()
    session.commit()

#Members
#-----------------------------------------------------#

def addrowtomember(clientname,clientage,clientexp,insurnum,insurpr,insursit,ticketnum,ticketpr):
    global glhikeid1
    session = Session()
    if not glhikeid1==0:
        clients = AllClass.Client(clientname, clientexp, clientage)
        session.add(clients)
        medicine = AllClass.Medicine(int(insurnum), int(insurpr), insursit)
        session.add(medicine)
        hikes=session.query(AllClass.Hike).filter_by(hike_id=glhikeid1)
        for hk in hikes:
            tp=hk.transport
        transp = AllClass.Transport(int(ticketnum), tp, int(ticketpr))
        session.add(transp)
        client = session.query(AllClass.Client).order_by(AllClass.Client.client_id.desc()).first()
        members = AllClass.Members(glhikeid1, client.client_id, 0, int(insurnum), int(ticketnum))
        session.add(members)
    session.commit()

def addguidestomembers(glhikeid1):
    session = Session()
    hike = session.query(AllClass.Hike).filter_by(hike_id=glhikeid1).first()
    firm = session.query(AllClass.Fr_to_Rt).filter_by(id=hike.id).first()
    guides = session.query(AllClass.Guide).filter_by(firm=firm.firm)
    for guide in guides:
         members = AllClass.Members(glhikeid1, 0, guide.guid_id, 0, 0)
         session.add(members)
    session.commit()

def hike_to_member(hikeid):
    session=Session()
    members = session.query(AllClass.Members).filter_by(hike=hikeid)
    session.commit()
    global glhikeid1
    glhikeid1=hikeid
    memberinfo = []
    membersinfo = []
    for member in members:
        if not member.client == 0:
            session1 = Session()
            clients=session1.query(AllClass.Client).filter_by(client_id=member.client)
            session1.commit()
            for client in clients:
                memberinfo.append(str(member.member_id))
                memberinfo.append(client.name)
                memberinfo.append(str(client.experience_y))
                memberinfo.append(str(client.age))
                memberinfo.append("C")
                memberinfo.append(str(member.med))
                memberinfo.append(str(member.ticket))
        if not member.guid == 0:
            session2 =Session()
            guides = session2.query(AllClass.Guide).filter_by(guid_id=member.guid)
            session2.commit()
            for guide in guides:
                memberinfo.append(str(member.member_id))
                memberinfo.append(guide.guid_name)
                memberinfo.append(str(guide.guid_exp_y))
                memberinfo.append(str(guide.age))
                memberinfo.append("G")
                memberinfo.append(" ")
                memberinfo.append(" ")
        membersinfo.append(memberinfo)
        memberinfo = []
    return membersinfo

def changememberdb( i, val, b):
    session=Session()
    clientid = session.query(AllClass.Members).filter_by(member_id=int(i)).first()
    if b==1:
        if not clientid.client == 0:
            session.query(AllClass.Client).filter_by(client_id=clientid.client).update({"name": val})
    if b==2:
        if not clientid.client == 0:
            session.query(AllClass.Client).filter_by(client_id=clientid.client).update({"experience_y": int(val)})
    if b==3:
        if not clientid.client == 0:
            session.query(AllClass.Client).filter_by(client_id=clientid.client).update({"age": int(val)})
    if b==5:
        mdnum = session.query(AllClass.Members).filter_by(member_id=int(i)).first()
        session.query(AllClass.Medicine).filter_by(med_number=mdnum.med).update({"med_number": int(val)})
    if b==6:
        tknum = session.query(AllClass.Members).filter_by(member_id=int(i)).first()
        session.query(AllClass.Transport).filter_by(ticket_id=tknum.ticket).update({"ticket_id": int(val)})
    session.commit()

def deletememberdb(delid):
    session = Session()
    session.query(AllClass.Equipment).filter_by(member=delid).delete()
    memb = session.query(AllClass.Members).filter_by(member_id=delid).first()
    if memb.guid==0:
        session.query(AllClass.Client).filter_by(client_id=memb.client).delete()
        session.query(AllClass.Transport).filter_by(ticket_id=memb.ticket).delete()
        session.query(AllClass.Medicine).filter_by(med_number=memb.med).delete()
        session.query(AllClass.Members).filter_by(member_id=delid).delete()
    session.commit()

def showinsurance(pos):
    session = Session()
    t=[]
    memb = session.query(AllClass.Members).filter_by(member_id=pos).first()
    if memb.guid==0:
        med = session.query(AllClass.Medicine).filter_by(med_number=memb.med).first()
        session.commit()
        t.append(str(med.med_number))
        t.append(str(med.price))
        t.append(med.situations)
    return t

def showticket(pos):
    session = Session()
    t=[]
    memb = session.query(AllClass.Members).filter_by(member_id=pos).first()
    if memb.guid==0:
        tick = session.query(AllClass.Transport).filter_by(ticket_id=memb.ticket).first()
        session.commit()
        t.append(str(tick.ticket_id))
        t.append(tick.type)
        t.append(str(tick.price))
    return t

#Equipment
#-----------------------------------------------------#
def addrowtoequipment(type, weight, properties, code):
    global glmembid
    session = Session()
    if not glmembid==0:
        equip = AllClass.Equipment(type, weight, properties, int(code), glmembid)
        session.add(equip)
    session.commit()

def memb_to_equip(membid):
    session=Session()
    equipments = session.query(AllClass.Equipment).filter_by(member=membid)
    session.commit()
    global glmembid
    glmembid=membid
    equipinfo = []
    equipsinfo = []
    for equipment in equipments:
        equipinfo.append(str(equipment.id))
        equipinfo.append(str(equipment.code))
        equipinfo.append(equipment.type)
        equipinfo.append(str(equipment.wight))
        equipinfo.append(equipment.param)
        equipsinfo.append(equipinfo)
        equipinfo = []
    return equipsinfo

def changeequipmentdb( i, val, b):
    session=Session()
    if b==1:
        session.query(AllClass.Equipment).filter_by(id=int(i)).update({"code": int(val)})
    if b==2:
        session.query(AllClass.Equipment).filter_by(id=int(i)).update({"type": val})
    if b==3:
        session.query(AllClass.Equipment).filter_by(id=int(i)).update({"wight": int(val)})
    if b==4:
        session.query(AllClass.Equipment).filter_by(id=int(i)).update({"param": val})
    session.commit()

def deleteequipmentdb(delid):
    session = Session()
    session.query(AllClass.Equipment).filter_by(id=delid).delete()
    session.commit()