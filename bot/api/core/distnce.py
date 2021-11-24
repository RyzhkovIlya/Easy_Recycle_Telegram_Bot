import pandas as pd
from api.core.function_dist import func_dist
from api.core.classificate import new_class
from api.static import EMPTY_DF

def distance(trash_class):
    '''Функция принимает на вход класс отхода и возвращает адрес топ-3 ближайших пунктов сбора данного класса мусора'''

    new_trash_class = new_class(trash_class) # С помощью функции new_class получает список из новых классов
    df = pd.read_excel('bot/api/database/garbage_points_msc.xlsx') # открываем датасет со списками всех пунктов сбора отходов
    df.Class = df.Class.apply(lambda x: eval(x)) # Каждый элемент признака Class переводим в питоновский формат
    df['Coordinates'] = df['Coordinates'].apply(lambda x: eval(x)) # Каждый элемент признака Coordinates переводим в питоновский формат
    if len(new_trash_class) > 1: # Проверяем,что длина списка с новыми классами была больше 1
        df_class = df[df['Class'].apply(lambda x: all([i in x for i in new_trash_class]))] # Оставляем только те записи в датасете, где в признакке Class присутствует любой класс из списка новых классов
<<<<<<< HEAD
        if df_class.empty:
            return EMPTY_DF
=======
>>>>>>> 75b424e0ae03b7d03309293a80d48961d610c888
    else:
        df_class = df[df['Class'].apply(lambda x: new_trash_class[0] in x)] # Оставляем только те записи в датасете, где в признакке Class присутствует найденный класс из списка нового класса
    df_class['dist_point'] = df_class['Coordinates'].apply(lambda x: int(func_dist(x))) # Создаем новый признак, куда заносим найденные расстояния от пользователя, до пунктов приема отходов
    df_class['str_dist_point'] = df_class['dist_point'].astype(str).apply(lambda x: f'(в {x} метрах)')
    df_class['output'] = df_class[['Address','str_dist_point']].apply(lambda x: ' '.join(x), axis=1)
    print(df_class['output'].head(1))
    return '♻️'+'\n♻️'.join(df_class.sort_values('dist_point', ascending = True).head(3)['output'].to_list()) # Возвращаем 3 ближайших пункта сбора отходов

