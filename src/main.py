from flask import Flask, request, render_template
from flask_restful import Resource, Api
from simpletransformers.ner import NERModel
import logging

if __name__ == '__main__':

    def convert_prediction_dict_to_pretty_output(paragraph, prediction):
        # Initialization
        is_concatenate = False
        concatenate_word = str()
        temp_entity = str()
        output = str()

        for index, element in enumerate(paragraph):
            for word_dict in prediction[index]:
                # stop concatenate if entity is O (str.length = 1)
                if list(word_dict.items())[0][1][0] == 'O':
                    is_concatenate = False
                    if concatenate_word:
                        # rebuild dictionary with key=concatenateWord: value=namedEntity
                        # send an output
                        output += '{}:{}\n'.format(concatenate_word, temp_entity)
                    # clear temporary variables
                    concatenate_word = ''
                    temp_entity = ''
                # start concatenate if word's value is start with B
                if list(word_dict.items())[0][1][0] == 'B':
                    is_concatenate = True
                    # store named entity temporary
                    temp_entity = list(word_dict.items())[0][1][2:]

                if is_concatenate:
                    concatenate_word += list(word_dict.items())[0][0]

        return output


    def model_prediction(text):
        logging.basicConfig(level=logging.DEBUG)
        transformers_logger = logging.getLogger('transformers')
        transformers_logger.setLevel(logging.WARNING)
        load_model = NERModel('bert', '../model_output/checkpoint-35835-epoch-15')
        sample = text.replace('\n', '').replace('\r', '').split('。')
        prediction, _ = load_model.predict(sample, split_on_space=False)

        return convert_prediction_dict_to_pretty_output(sample, prediction)


    app = Flask(__name__, template_folder='../templates')
    api = Api(app)

    history = list()


    @app.route('/')
    def web_page():
        return render_template('index.html')


    class calculateApi(Resource):
        # send to website
        def get(self):
            return history[0]

        # website send to backend
        def post(self):
            paragraph = request.get_json()
            predict_result = model_prediction(paragraph['Paragraph_text_area'])
            history.clear()
            history.append(predict_result)
            return paragraph


    api.add_resource(calculateApi, '/calc')

    app.run(debug=True)
