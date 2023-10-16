from tests.conftest import client


class TestCity:

    def test_create_city(self):
        """
        Добавление существующего и несуществующего города
        """
        city = ['новосибирск', 'бруманск']
        response = client.post(url=f'city/create-city/?city={city[0]}')
        assert response.status_code == 200, "Город не добавился"
        response = client.post(url=f'city/create-city/?city={city[1]}')
        assert response.status_code == 400

    def test_get_city(self):
        """
        Получение списка городов
        """
        q = 'нов'
        response = client.get(url=f'city/get-cities/?q={q}')
        assert response.status_code == 200
        body_response = response.json()
        print(body_response)
        assert body_response == [{'id': 1, 'name': 'Новосибирск', 'weather': body_response[0]['weather']}]


class TestUser:

    def test_register_user(self):
        """
        Добавление пользователя
        """
        response = client.post(url='user/register-user/',
                               json={
                                   "name": "Daniil",
                                   "surname": "Freeman",
                                   "age": 23,
                               }
                               )
        assert response.status_code == 200, "Не удалось добавить пользователя"
        body_response = response.json()
        true_answer = {"id": 1,
                       "name": "Daniil",
                       "surname": "Freeman",
                       "age": 23
                       }
        assert body_response == true_answer
        """
        Добавление ещё одного пользователя 
        """
        response = client.post(url='user/register-user/',
                               json={
                                   "name": "Sergei",
                                   "surname": "Sergeevich",
                                   "age": 45,
                               }
                               )
        assert response.status_code == 200, "Не удалось добавить пользователя"
        body_response = response.json()
        true_answer = {"id": 2,
                       "name": "Sergei",
                       "surname": "Sergeevich",
                       "age": 45,
                       }

        assert body_response == true_answer

    def test_get_users(self):
        """
        Получение списка юзеров сортированных по возрасту
        order = desc | asc
        """
        order = 'desc'
        response = client.get(url=f'user/get-users/?order={order}')
        assert response.status_code == 200, "Не удалось получить список"
        body_response = response.json()
        true_answer = [{"id": 2,
                        "name": "Sergei",
                        "surname": "Sergeevich",
                        "age": 45,
                        },
                       {"id": 1,
                        "name": "Daniil",
                        "surname": "Freeman",
                        "age": 23
                        }
                       ]
        assert body_response == true_answer

        order = "asc"
        response = client.get(url=f'user/get-users/?order={order}')
        assert response.status_code == 200, "Не удалось получить список"
        body_response = response.json()
        true_answer.reverse()
        assert body_response == true_answer


class TestPicnic:

    def test_add_picnic(self):
        """
        Добавление пикника
        """
        response = client.post(url='picnic/picnic-add/',
                               json={
                                   "city_id": 1,
                                   "time": "2023-01-01 08:05:00"
                               })
        assert response.status_code == 200, "Не удалось добавить"
        body_response = response.json()
        true_answer = {"id": 1,
                       "city": {"id": 1,
                                "name": "Новосибирск",
                                "weather": body_response['city']['weather']
                                },
                       "time": "2023-01-01T08:05:00"
                       }
        assert body_response == true_answer

    def test_register_picnic(self):
        """
        Регистрация пикника
        """
        response = client.post(url='picnic/picnic-register/',
                               json={"user_id": 1,
                                     "picnic_id": 1
                                     })
        assert response.status_code == 200, "Не удалось добавить"
        body_response = response.json()
        true_answer = {"id": 1,
                       "user": {"id": 1,
                                "name": "Daniil",
                                "surname": "Freeman",
                                "age": 23
                                },
                       "picnic": {"id": 1,
                                  "city": {"id": 1,
                                           "name": "Новосибирск",
                                           "weather": body_response['picnic']['city']['weather']
                                           },
                                  "time": "2023-01-01T08:05:00"
                                  }
                       }
        assert body_response == true_answer

    def test_get_all_picnic(self):
        """
          Получение списка пикников по времени(включая прошедшие пикники или нет)
        """
        params1, params2 = "2023-01-01 08:05:00", "true"
        response = client.get(url=f'picnic/all-picnics/?time={params1}&past={params2}')
        assert response.status_code == 200, "Не удалось получить список"
        body_response = response.json()
        answer_true = [{"id": 1,
                        "city": {"id": 1,
                                 "name": "Новосибирск",
                                 "weather": body_response[0]['city']['weather']
                                 },
                        "time": "2023-01-01T08:05:00",
                        "users": [{"id": 1,
                                   "name": "Daniil",
                                   "surname": "Freeman",
                                   "age": 23
                                   }]
                        }]
        assert body_response == answer_true
