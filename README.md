# ML-Ops project
Простое MlOps приложение, выполненое в качестве домашнего задания по курсу ШАД от МТС

Ссылки на Docker образы:
- [Сервер](https://hub.docker.com/repository/docker/constantfear/ml-ops-simple-project-server/general)
- [Клиент](https://hub.docker.com/repository/docker/constantfear/ml-ops-simple-project-client)

API написано с помощью фреймворка [FastAPI](https://fastapi.tiangolo.com/); 

Frontend часть написана при помощи [Streamlit](https://streamlit.io/)

### Функционал
1. Может принимать на вход данные и выдавать предсказания модели в формате CSV;
2. У пресдказаний выводит график распределения классов, который можно потом скачать;
3. Выводит топ 5 важных для модели признаков;
