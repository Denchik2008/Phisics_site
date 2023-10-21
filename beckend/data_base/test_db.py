# from sqlalchemy import create_engine, Column, String, JSON, Integer
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# # Создание базы данных
# engine = create_engine('postgresql://postgres:Distant12357@localhost:5432/dasha_plus_phisics_is_love', echo=True)
# Base = declarative_base()

# # Определение модели данных
# class Array(Base):
#     __tablename__ = 'arrays'

#     id = Column(Integer, primary_key=True)
#     data = Column(JSON)

# Session = sessionmaker(bind=engine)
# session = Session()

# def get_array_by_id(array_id):
#     array = session.query(Array).filter_by(id=array_id).first()
#     session.close()

#     return array.data if array else None

# Base.metadata.create_all(engine)

# if __name__ == '__main__':
#     arrays = [
#         ['aaaa', 'nigers', 'hhh.png', ['bbb', 'dasfsdf', 'hhh.png', 'right_answer']],
#         ['bbbb', 'aaaaaa', 'hhh.png', ['aaaaaa', 'nnnnn', 'hhh.png', 'wrong_answer']]
#     ]
#     array = Array(id=1, data=arrays)
#     session.add(array)
#     array_id = input("Введите ID массива: ")
#     array_data = get_array_by_id(array_id)
#     if array_data:
#         print(f"Массив с ID {array_id}: {array_data}")
#     else:
#         print(f"Массив с ID {array_id} не найден.")
#     print(array_data)
