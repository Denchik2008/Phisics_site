from sqlalchemy import create_engine, Column, Integer, String, ARRAY, JSON, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True)
    data = Column(JSON)

engine = create_engine('postgresql://postgres:Distant12357@localhost:5432/phisics_site')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def add_item(data):
    session = Session()
    new_item = Item(data=data)
    session.add(new_item)
    session.commit()
    session.close()

def get_item_by_id(item_id):
    session = Session()
    try:
        item = session.query(Item).filter_by(id=item_id).one()
        return item
    except NoResultFound:
        return None
    finally:
        session.close()
        
def update_item_data(item_id, new_data):
    session = Session()
    try:
        item = session.query(Item).filter_by(id=item_id).one()
        item.data = new_data
        session.commit()
        return True
    except NoResultFound:
        return False
    finally:
        session.close()