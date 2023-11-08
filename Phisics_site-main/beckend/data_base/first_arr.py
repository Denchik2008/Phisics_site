from database import add_item, get_item_by_id, update_item_data
# from test_db import get_array_by_index


add_item([])

item = get_item_by_id(1)
print(f'Обновленные данные элемента с ID=1: {item.data}')

