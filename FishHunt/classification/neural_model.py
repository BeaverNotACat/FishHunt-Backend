import numpy
import tensorflow 
import pandas

from FishHunt.settings import MODEL_PATH, LABELS


model = tensorflow.keras.models.load_model(MODEL_PATH)



class Model:
    '''Class that represents pretrained Neural Model'''
    def __init__(self) -> None:
        self.model = model
        self.labels = LABELS
        self.generator = tensorflow.keras.preprocessing.image.ImageDataGenerator(
    preprocessing_function=tensorflow.keras.applications.mobilenet_v2.preprocess_input)


    def _make_image_data_frame(self, image_path: str) -> pandas.DataFrame:
        return pandas.concat(
            [pandas.Series([image_path], name='filepath'), pandas.Series(['None'], name='label')], axis=1)


    def _make_data_frame_iterator(self, data: pandas.DataFrame):
        return self.generator.flow_from_dataframe(
    dataframe=data,
    x_col='filepath',
    y_col='label',
    target_size=(224, 224),
    color_mode='rgb',
    class_mode='categorical',
    batch_size=32,
    shuffle=False)


    def predict_fish_name(self, image_path:str) -> str:
        data = self._make_data_frame_iterator(self._make_image_data_frame(image_path))
        return self.labels[
                numpy.argmax(self.model.predict(data), axis=1)[0]]

