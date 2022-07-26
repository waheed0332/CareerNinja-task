
from flask import Flask, jsonify
from flask import request
from sklearn.metrics.pairwise import cosine_similarity
import spacy

  
app = Flask(__name__)

def prepare_models():

    nlp = spacy.load('en_core_web_md')
    tokenize = spacy.load('en_core_web_sm', disable=['parser', 'ner',
                                            'tok2vec', 'attribute_ruler'])
    return  nlp, tokenize

def word2vec(sentences):
    # word2vec with cosine similarity
    docs = [nlp(sentence) for sentence in sentences]
    return docs[0].similarity(docs[1])

@app.route('/check-similarity', methods=['POST'])
def sentence_similarity():
    if request.method == "POST":

        request_data = request.get_json()

        try:
            sentance1 = request_data['sentance1']
            sentance2 = request_data['sentance2']
            
            if (sentance1==None or sentance2==None):
                return jsonify({
                    "status": "error",
                    "error_message": "Please pass two sentances to check similarity!"
                    })
            else:
                return jsonify({
                    'status':'success',
                    'sentence1': sentance1,
                    'sentence2': sentance2,
                    'similarity-score': round(word2vec([sentance1, sentance2]), 1)
                    })

        except Exception as e:
            return jsonify({
                "status": "error",
                "error_message": str(e)})

if __name__ =='__main__':
    nlp, tokenize = prepare_models()
    app.run(debug = True, use_reloader = True)