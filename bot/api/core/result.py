from api.static import PH
import os
from api.static import TRY_AGAIN, CAN_RECYCLE

def result_out():
    '''Функция принимает возвращает список классов, которые были обнаружены на фотографии.'''

    os.system(f'{PH}darknet detector test {PH}cfg/coco.data {PH}cfg/custom-yolov4-detector.cfg {PH}72custom-yolov4-detector_best.weights data/prediction.jpg -thresh 0.7 -dont-show -ext_output < {PH}data/train.txt > {PH}result.txt')
    with open(f'{PH}result.txt') as f:
        text = f.read()
        text = text.split('\n')
        text = list(filter(None, text))
        print(len(text))
        if len(text) > 10:
            text_1 = text[10:]
            all_results = [i.split(':')[0] for i in text_1]
            return all_results
        else:
            return TRY_AGAIN
    
def result_out_plastic():
    '''Функция принимает возвращает список классов, которые были обнаружены на фотографии пластика.'''

    with open(f'{PH}result_plastic.txt') as f:
        text = f.read()
        text = text.split('\n')
        text = list(filter(None, text))
        if len(text) > 10:
            text_2 = text[10:]
            plastic_results = [i.split(':')[0] for i in text_2]
            return plastic_results
        else:
            return CAN_RECYCLE
