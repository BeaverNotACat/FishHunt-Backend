import numpy
import tensorflow 
import pandas


class Model:
    def __init__(self) -> None:
        self.model = tensorflow.keras.models.\
                load_model('../../model_weights')
        self.labels = {0: 'Black Sea Sprat',
                         1: 'Gilt-Head Bream',
                         2: 'Hourse Mackerel',
                         3: 'Red Mullet',
                         4: 'Red Sea Bream',
                         5: 'Sea Bass',
                         6: 'Shrimp',
                         7: 'Striped Red Mullet',
                         8: 'Trout'}
        self.generator = generator = tensorflow.keras.preprocessing.image.ImageDataGenerator(
        preprocessing_function=tensorflow.keras.applications.mobilenet_v2.preprocess_input)


    def _make_image_data_frame(self, image_path: str) -> pandas.DataFrame:
        return pandas.concat(
            [pandas.Series([image_path], name='Filepath'), pandas.Series(['None'], name='Label')], axis=1)

    def _make_data_frame_iterator(self, data: pandas.DataFrame):
        return self.generator.flow_from_dataframe(
                dataframe=data,
                x_col='filepath',
                y_col='label',
                target_size=(224, 224),
                color_mode='rgb',
                class_mode='categorical',
                batch_size=32,
                shuffle=True,
                seed=42,
                subset='training')

    def predict_fish_name(self, image_path:str) -> str:
        data = self._make_data_frame_iterator(self._make_image_data_frame(image_path))
        return self.labels[
                numpy.argmax(self.model.predict(data), axis=1)]

