import numpy as np
import pandas as pd
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from transformers import BertTokenizerFast
from transformers import TFBertModel
from bert_tokenizer import tokenize

df = pd.read_csv(r'C:\Users\Asus\Documents\miniproject\files\output_files\tweets_after_preprocessing.csv')
input_values = df['text_clean'].values

MAX_LEN=128
#input_ids, attention_masks = tokenize(input_values, MAX_LEN)
print("LOADING BERT MODEL")
new_model = tf.keras.models.load_model(r'C:\Users\Asus\Documents\miniproject\enigma\my_model')
example_input = ['You are the worst person i have ever seen',
                'you seem normal',
                'I really like the way you speak']

input_ids, attention_masks = tokenize(input_values, MAX_LEN)
result_bert = new_model.predict([input_ids, attention_masks])
print("SCORE : \n")
for j in range(len(result_bert)):
  print(max(result_bert[j])*100)
print('\n')
oplabels = ['Bullying','Not Bullying']

y_pred_bert =  np.zeros_like(result_bert)
y_pred_bert[np.arange(len(y_pred_bert)), result_bert.argmax(1)] = 1
#print(y_pred_bert)
for i in y_pred_bert.argmax(1):
  print(oplabels[i])