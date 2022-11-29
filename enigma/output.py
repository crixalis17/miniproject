import numpy as np
import pandas as pd
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from transformers import BertTokenizerFast
from transformers import TFBertModel



def final_output(profile_name,tokenize):
  df_dict = {}
  bully_count = 0

  df_dict['Name'] = profile_name

  df = pd.read_csv(r'C:\Users\Asus\Documents\miniproject\files\output_files\tweets_after_preprocessing.csv')
  input_values = df['text_clean'].values

  MAX_LEN=128
  
  print("LOADING BERT MODEL")
  new_model = tf.keras.models.load_model(r'C:\Users\Asus\Documents\miniproject\enigma\my_model')


  input_ids, attention_masks = tokenize(input_values, MAX_LEN)
  result_bert = new_model.predict([input_ids, attention_masks])
  
 
  #for j in range(len(result_bert)):
  #  print(max(result_bert[j])*100)
  #print('\n')
  oplabels = ['Bullying','Not Bullying']
  
  

  y_pred_bert =  np.zeros_like(result_bert)
  y_pred_bert[np.arange(len(y_pred_bert)), result_bert.argmax(1)] = 1

  df_dict['Number of Tweets']= len(y_pred_bert)
  
  for i in y_pred_bert.argmax(1):
    print(oplabels[i])
    if i==0:
      bully_count = bully_count + 1
  df_dict['No. of Bullying Tweets'] = bully_count

  percentage_bully = (bully_count/len(y_pred_bert))*100
  df_dict['Percentage of Bullying'] = percentage_bully
  print(df_dict)
  #df = pd.DataFrame(df_dict)
  #df.to_csv(r"C:\Users\Asus\Documents\miniproject\files\output_files\result.csv")
  
  return df_dict