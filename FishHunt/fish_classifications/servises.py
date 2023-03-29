import tensorflow
import numpy

from FishHunt.settings import MODEL, MODEL_LABELS


def predict_fish_name(image_path: str) -> str:
    image = tensorflow.keras.preprocessing.image.load_img(
            image_path, grayscale=False,
            color_mode="rgb", target_size=(224, 224),
            interpolation="nearest")
    input_arr = numpy.array(
            [tensorflow.keras.preprocessing.image.img_to_array(image)])  # Convert single image to a batch.
    predictions = numpy.argmax(
            MODEL.predict(input_arr),axis=1)

    return MODEL_LABELS[predictions[0]]




