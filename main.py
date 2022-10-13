import requests
import json
import credentials
from credentials import base_url, username, passwd, DaTa


#SIGN IN
print('res_get_login')
res_get_login = requests.get(f"{credentials.base_url}user/login", params={'username': username, 'password': passwd},
                             headers={'accept': 'application/json'})
if 'application/json' in res_get_login.headers['Content-Type']:
    print(res_get_login.json())
else:
    print(res_get_login.text)
print('\nres_get_pets_by_status')

# PET
res_get_pets_by_status = requests.get(f'{credentials.base_url}pet/findByStatus', params={'status': 'available'},
                                      headers={'accept': 'application/json'})
if 'application/json' in res_get_pets_by_status.headers['Content-Type']:
    print(res_get_pets_by_status.json())
else:
    print(res_get_pets_by_status.text)

pet_id = res_get_pets_by_status.json()[0].get('id')
print('\nres_post_update_pet_by_id')


res_post_update_pet_by_id = requests.post(f'{credentials.base_url}pet/{pet_id}',
                                          headers={'accept': 'application/json',
                                                   'Content-Type': 'application/x-www-form-urlencoded'},
                                          data={'name': 'Berserk', 'status': 'pending'})
if 'application/json' in res_post_update_pet_by_id.headers['Content-Type']:
    print(res_post_update_pet_by_id.json())
else:
    print(res_post_update_pet_by_id.text)
print('\nres_pet_image')


res_pet_image = requests.post(f'{credentials.base_url}pet/{pet_id}/uploadImage',
                              headers={'accept': 'application/json', 'Content-Type': DaTa.image_data.content_type},
                              data=DaTa.image_data)
if 'application/json' in res_pet_image.headers['Content-Type']:
    print(res_pet_image.json())
else:
    print(res_pet_image.text)
print('\nres_get_pet_by_id')


res_get_pet_by_id = requests.get(f'{credentials.base_url}pet/{pet_id}', headers={'accept': 'application/json'})
if 'application/json' in res_get_pet_by_id.headers['Content-Type']:
    print(res_get_pet_by_id.json())
else:
    print(res_get_pet_by_id.text)
print('\nres_post_new_pet')


res_post_new_pet = requests.post(f"{credentials.base_url}pet",
                                 headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                                 data=json.dumps(DaTa.post_new_pet_data, ensure_ascii=False))
if 'application/json' in res_post_new_pet.headers['Content-Type']:
    print(res_post_new_pet.json())
else:
    print(res_post_new_pet.text)
print('\nres_update_pet')


res_update_pet = requests.put(f'{credentials.base_url}pet',
                              headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                              data=json.dumps(DaTa.update_pet_data, ensure_ascii=False))
if 'application/json' in res_update_pet.headers['Content-Type']:
    print(res_update_pet.json())
else:
    print(res_update_pet.text)
print('\nres_delete_pet')


res_delete_pet = requests.delete(f'{credentials.base_url}pet/{pet_id}',
                                 headers={'api_key': 'special-key', 'accept': 'application/json'})
try:
    print(res_delete_pet.json())
except requests.JSONDecodeError as je:
    print(res_delete_pet)
print('\nres_order_place')


# STORE
res_order_place = requests.post(f'{credentials.base_url}store/order',
                                headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                                data=json.dumps(DaTa.order_place_data, ensure_ascii=False))
if 'application/json' in res_order_place.headers['Content-Type']:
    print(res_order_place.json())
else:
    print(res_order_place.text)
print('\nres_find_order')


res_find_order = requests.get(f'{credentials.base_url}store/order/{5}', headers={'accept': 'application/json'})
if 'application/json' in res_find_order.headers['Content-Type']:
    print(res_find_order.json())
else:
    print(res_find_order.text)
print('\nres_delete_order')


res_delete_order = requests.delete(f'{credentials.base_url}store/order/{5}', headers={'accept': 'application/json'})
if 'application/json' in res_delete_order.headers['Content-Type']:
    print(res_delete_order.json())
else:
    print(res_delete_order.text)
print('\nres_get_inventory')


res_get_inventory = requests.get(f'{credentials.base_url}store/inventory', headers={'accept': 'application/json'})
if 'application/json' in res_get_inventory.headers['Content-Type']:
    print(res_get_inventory.json())
else:
    print(res_get_inventory.text)
print('\nres_create_user_list')


# USER
res_create_user_list = requests.post(f'{credentials.base_url}user/createWithArray',
                                     headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                                     data=json.dumps(DaTa.create_user_data, ensure_ascii=False))
if 'application/json' in res_create_user_list.headers['Content-Type']:
    print(res_create_user_list.json())
else:
    print(res_create_user_list.text)
print('\nres_create_list_of_users')


res_create_list_of_users = requests.post(f'{credentials.base_url}user/createWithList',
                                         headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                                         data=json.dumps(DaTa.create_list_of_users_data,
                                                         ensure_ascii=False).encode('utf-8'))
if 'application/json' in res_create_list_of_users.headers['Content-Type']:
    print(res_create_list_of_users.json())
else:
    print(res_create_list_of_users.text)
print('\nres_get_username')


res_get_username = requests.get(f'{credentials.base_url}user/user1', headers={'accept': 'application/json'})
if 'application/json' in res_get_username.headers['Content-Type']:
    print(res_get_username.json())
else:
    print(res_get_username.text)
print('\nres_update_user')


res_update_user = requests.put(f'{credentials.base_url}user/user1',
                               headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                               data=json.dumps(DaTa.update_user_data, ensure_ascii=False))
if 'application/json' in res_update_user.headers['Content-Type']:
    print(res_update_user.json())
else:
    print(res_update_user.text)
print('\nres_post_user')


res_post_user = requests.post(f'{base_url}user', headers={'content-type': 'application/json'},
                              data=json.dumps(DaTa.post_user_data, ensure_ascii=False))
if 'application/json' in res_post_user.headers['Content-Type']:
    print(res_post_user.json())
else:
    print(res_post_user.text)
print('\nres_delete_user')


res_delete_user = requests.delete(f'{credentials.base_url}user/fafd')
try:
    print(res_delete_user.json())
except requests.JSONDecodeError as je:
    print(res_delete_user)
print('\nres_get_logout')


# LOG OUT
res_get_logout = requests.get(f"{credentials.base_url}user/logout", headers={'accept': 'application/json'})
if 'application/json' in res_get_logout.headers['Content-Type']:
    print(res_get_logout.json())
else:
    print(res_get_logout.text)








