from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


# Маршрутизация:
# маршрут к главной странице
@app.get("/")
async def main_page():
    return "Главная страница"


# маршрут к странице администратора
@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"


# маршрут к страницам пользователей, используя параметр в пути
@app.get("/user/{user_id}")
async def user_page(
        user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="1")]):
    return f"Вы вошли как пользователь № {user_id}"


# маршрут к страницам пользователей, передавая данные в адресной строке
@app.get("/user/{username}/{age}")
async def user_page_address_str(
        username: Annotated[str, Path(min_length=5, max_length=20,
                                      description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> dict:
    return {"Информация о пользователе. Имя": username, "Возраст": age}
