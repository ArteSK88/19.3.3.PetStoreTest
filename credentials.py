from requests_toolbelt.multipart.encoder import MultipartEncoder
import os


base_url = 'https://petstore.swagger.io/v2/'
username = '%D0%90%D1%80%D1%82%D0%B5%D0%BC'
passwd = '123'


class DaTa:
    file_name = 'panther.jpg'
    pet_photo = os.path.join(os.path.dirname(__file__), f'images/{file_name}')
    image_data = MultipartEncoder(fields=
                                  {'file': (file_name, open(pet_photo, 'rb'), 'image/jpeg')})


    post_new_pet_data = {
      "id": 0,
      "category": {
        "id": 0,
        "name": "string"
      },
      "name": "doggie",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }

    update_pet_data = {
      "id": 0,
      "category": {
        "id": 0,
        "name": "string"
      },
      "name": "doggie",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }


    order_place_data = {
      "id": 0,
      "petId": 0,
      "quantity": 0,
      "shipDate": "2022-10-06T18:57:08.765Z",
      "status": "placed",
      "complete": 'True'
    }

    create_user_data = [
      {
        "id": 0,
        "username": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
      }
    ]

    create_list_of_users_data = [
      {
        "id": 0,
        "username": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
      }
    ]

    update_user_data = {
      "id": 0,
      "username": "string",
      "firstName": "string",
      "lastName": "string",
      "email": "string",
      "password": "string",
      "phone": "string",
      "userStatus": 0
    }

    post_user_data = {
      "id": 0,
      "username": "string",
      "firstName": "string",
      "lastName": "string",
      "email": "string",
      "password": "string",
      "phone": "string",
      "userStatus": 0
    }