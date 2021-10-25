# Easy_Recycle_Telegram_Bot

![StopWatch](https://github.com/RyzhkovIlya/All_materials/blob/main/new_video%20(3).gif)

## Задача

Реализовать сервис по грамотной и быстрой сортировки отходом для их утилизации.

## План решения заачи

1) **Формирование датасета классов отходов и пунктов раздельного сбора отходов**
2) **Разметка фотографий и их аугментация**
3) **Выбор и обучение модели на нейронных сетях**
4) **Создание сервиса**

## Решение задачи

1) Были определены 6 классов отходов (Пластик, бумага, металл, органические материалы природного происхождения, стекло, композитные материалы) и сделан датасет из 1400 фотографий. Так же в ручную был сделан датасет из пунктов раздельного сбора отходо по г.Москва для наших классов (около 400 точек)
2) С помощью сайта https://roboflow.com/ была проведена аугрентация фотографий. В конечном итоге количество фотографий возросло до 5000. Они были разделены на train, test и valid.
3) В качестве модели была выбрана модель Yolov4 DarkNet и с помощью Google Colab были обучены две данные модели. Вторая модель определяет является ли пластик перерабатываемым или нет. Обучение заняло 15 и 10 часов соответственно.
