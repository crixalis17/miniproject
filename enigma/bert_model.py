import numpy as np
import pandas as pd
import tensorflow as tf


from transformers import BertTokenizerFast
from transformers import TFBertModel
from bert_tokenizer import tokenize

df = pd.read_csv(r'C:\Users\Asus\Documents\miniproject\dataset\Corona_NLP_test_saved.csv')
input_values = df['text_clean'].values

MAX_LEN=128
#input_ids, attention_masks = tokenize(input_values, MAX_LEN)

new_model = tf.keras.models.load_model(r'C:\Users\Asus\Documents\miniproject\enigma\my_model')
example_input = ['You are the worst person i have ever seen','you seem normal','I really like the way you speak']
example_input_ids, example_attention_masks = tokenize(example_input, MAX_LEN)
result_bert = new_model.predict([example_input_ids,example_attention_masks])
print(result_bert)
print('\n\n')
oplabels = ['Bullying','Not Bullying']

y_pred_bert =  np.zeros_like(result_bert)
y_pred_bert[np.arange(len(y_pred_bert)), result_bert.argmax(1)] = 1
print(y_pred_bert)
#for i in y_pred_bert.argmax(1):
#  print(oplabels[i])