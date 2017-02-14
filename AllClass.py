from sqlalchemy import Column, Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

#Session = orm.sessionmaker(bind=engine)
#session=Session()
#clients = session.query(Client).all()
#for client in clients:
#    print(client)
#session.commit()

class Client(Base):
    __tablename__ = 'Clients'

    client_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    experience_y = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)

    def __init__(self, name, experience_y, age):
        self.name = name
        self.experience_y = experience_y
        self.age = age

    def __repr__(self):
        return "<User('%s','%s', '%s', '%s')>" % (self.client_id, self.name, self.experience_y, self.age)

class Route(Base):
    __tablename__ = 'Route'

    route_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    difficult = Column(String, nullable=False)
    oxygen = Column(Integer, nullable=False)
    length_km = Column(Integer,nullable=False)

    def __init__(self, name, country, difficult,oxygen,length_km):
        self.name = name
        self.country = country
        self.difficult = difficult
        self.oxygen = oxygen
        self.length_km=length_km

class Firm(Base):
    __tablename__ = 'Firms'

    firm_id = Column(Integer, primary_key=True)
    firm_name = Column(String, nullable=False)
    score = Column(Integer, nullable=False)

    def __init__(self, firm_name, score):
        self.firm_name = firm_name
        self.score = score

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.firm_id, self.firm_name, self.score)

class Fr_to_Rt(Base):
    __tablename__ = 'Fr_to_Rt'

    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    firm = Column(ForeignKey('Firms.firm_id'), nullable= False)
    route = Column(ForeignKey('Route.route_id'),nullable=False)

    def __init__(self, price, firm, route):
        self.price=price
        self.firm = firm
        self.route = route

class Guide(Base):
    __tablename__ = 'Guides'

    guid_id = Column(Integer, primary_key=True)
    guid_name = Column(String, nullable=False)
    guid_exp_y = Column(Integer, nullable=False)
    age=Column(Integer, nullable=False)
    firm = Column(ForeignKey('Firms.firm_id'), nullable=False)

    def __init__(self, guid_name, guid_exp_y, age, firm):
        self.guid_name = guid_name
        self.guid_exp_y = guid_exp_y
        self.age = age
        self.firm = firm

class Hike(Base):

    __tablename__ = 'Hike'

    hike_id = Column(Integer, primary_key=True)
    id = Column(ForeignKey('Fr_to_Rt.id'), nullable=False)
    date_start= Column(String, nullable=False)
    date_end = Column(String, nullable=False)
    transport = Column(String, nullable= True)

    def __init__(self, id, date_start, date_end, transport):
        self.id = id
        self.date_start = date_start
        self.date_end = date_end
        self.transport = transport

class Food(Base):
    __tablename__ = 'Food'

    food_id = Column(Integer, primary_key=True)
    hike_id = Column(ForeignKey('Hike.hike_id'), nullable=False)
    type= Column(String, nullable=False)
    number = Column(Integer, nullable=False)

    def __init__(self, hike_id, type, number):
        self.hike_id = hike_id
        self.type = type
        self.number = number

class Medicine(Base):
    __tablename__ = 'Medicine'

    med_number = Column(Integer, primary_key=True, unique= True)
    price= Column(Integer, nullable=False)
    situations = Column(String, nullable=True)

    def __init__(self, med_number, price, situations):
        self.med_number = med_number
        self.price = price
        self.situations = situations

class Transport(Base):
    __tablename__="Transport"

    ticket_id = Column(Integer, primary_key=True, unique= True)
    price= Column(Integer, nullable=False)
    type = Column(ForeignKey('Hike.transport'), nullable=True)

    def __init__(self,ticket_id, price, type):
        self.ticket_id=ticket_id
        self.price = price
        self.type = type

class Members(Base):
    __tablename__ = 'Members'

    member_id = Column(Integer, primary_key=True)
    hike = Column(ForeignKey('Hike.hike_id'), nullable=False)
    client=Column(ForeignKey('Clients.client_id'), nullable=False)
    guid=Column(ForeignKey('Guides.guid_id'), nullable=False)
    med=Column(ForeignKey('Medicine.med_number'), nullable=False)
    ticket=Column(ForeignKey('Transport.ticket_id'), nullable=False)


    def __init__(self, hike, client, guid, med, ticket):
        self.hike = hike
        self.client = client
        self.guid = guid
        self.med = med
        self.ticket = ticket

class Equipment(Base):
    __tablename__ = 'Equipment'

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    wight = Column(String, nullable=False)
    param = Column(String, nullable=False)
    code = Column(Integer, nullable=False, unique= True)
    member = Column(ForeignKey('Members.member_id'), nullable=False)


    def __init__(self, type, wight, param, code, member):
        self.type = type
        self.wight = wight
        self.param = param
        self.code = code
        self.member = member
