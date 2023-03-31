#fast api
import fastapi
#typing
import typing as t
import pydantic


app = fastapi.FastAPI()

@app.get('/', response_model=dict[str, str])
def main_page():
    return {
        'name': 'Danial',
        'surname': 'Sadykov',
        'secondname': 'Maratovich',
        'birth_date': '02.08.2007',
        'place': 'Karaganda'
    }

class User(pydantic.BaseModel):
    id: int
    username: str
    password: str


users: list[User] = [
        {'id': 1, 'username': 'Bob', 'password': 'my_pass'},
        {'id': 2, 'username': 'Mike', 'password': 'qwerty'},
        {'id': 3, 'username': 'Jhon', 'password': 'ytrewq'}
    ]

@app.get('/users', response_model=list[User])
def get_all_users():
    return users

@app.get('/users/{us_id}', response_model=t.Optional[User])
def get_user(us_id: int):
    return [i for i in users if i.get('id') == us_id][0]


class Trade(pydantic.BaseModel):
    id: int
    user_1: int
    user_2: int
    price: int
    amount: int


trades: list[Trade] = [
        {'id': 1, 'user_1': 1, 'user_2': 2, 'price': 1098, 'amount': 4},
        {'id': 2, 'user_1': 2, 'user_2': 3, 'price': 1088, 'amount': 2},
        {'id': 3, 'user_1': 3, 'user_2': 1, 'price': 8, 'amount': 43}
    ]

@app.get('/trades', response_model=list[Trade])
def get_all_trades(): return trades

@app.get('/trades/{tr_id}', response_model=t.Optional[Trade])
def get_trade(tr_id: int):
    return [i for i in trades if i.get('id') == tr_id][0]

a = {'q': 1, 'w': 'hello'}
b = {'name': 'Mike', 'a': a}

@app.get('/bbb', response_model=dict)
def get_b():
    return b