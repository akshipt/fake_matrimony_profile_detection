from keras.models import load_model
import tensorflow as tf
import string
import re

# @tf.keras.utils.register_keras_serializable(
#     package='Custom', name=None
# )
# def custom_standardization(input_data):
#     lowercase = tf.strings.lower(input_data)
#     stripped_html = tf.strings.regex_replace(lowercase, '<br />', ' ')
#     return tf.strings.regex_replace(stripped_html,
#                                     '[%s]' % re.escape(string.punctuation),
#                                     '')
#
#
# model = None
# with tf.keras.utils.custom_object_scope({'custom_standardization': custom_standardization}):
#     loaded_model = load_model('./tmp/model')

loaded_model = load_model('./tmp/model')
old_list = []


def model_result(serial_data):
    new_dict = serial_data.dict()
    new_dict.pop('submit')

    sample = {"gender": int(new_dict["gender"]),
              "marital_life": int(new_dict["marital_life"]),
              "p_marital_status": int(new_dict["p_marital_status"]),
              "caste": "Brahmin",
              "mother_tongue": "Bengali",
              "religion": "Hindu",
              "annual_income": "14-16 Lakhs",
              "city": "Udaipur",
              "state": "Rajasthan",
              "education": "MBBS",
              "occupation": "Doctor",
              "employed_in": "GovernmentPSU",
              "profile_created_by": "self",
              # "languages": "Bengali English Hindi",
              "p_age": "18 - 25 yrs",
              "p_mother_tongue": "Bengali",
              "p_religion": "Hindu",
              "age": int(new_dict["age"]),
              "photo_count": int(new_dict["photo_count"]),
              "brother": int(new_dict["brother"]),
              "sister": int(new_dict["sister"])
              }

    input_dict = {name: tf.convert_to_tensor([value]) for name, value in sample.items()}
    ywgan = loaded_model.predict(input_dict)
    print(ywgan[0][0])
    if ywgan[0][0] > 0.94:
        return True
    else:
        return False
