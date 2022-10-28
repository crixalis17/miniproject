import numpy as np
import pandas as pd
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from transformers import BertTokenizerFast
from transformers import TFBertModel



def final_output(profile_name,tokenize):
  df_dict = {
    'attr': ['Name','No_of_tweets','bullying','percentage']
  }
  bully_count = 0
  output_value = []
  output_value.append(profile_name)

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
  
  output_value.append(len(y_pred_bert))
  for i in y_pred_bert.argmax(1):
    print(oplabels[i])
    if i==0:
      bully_count = bully_count + 1
  output_value.append(bully_count)

  percentage_bully = (bully_count/len(y_pred_bert))*100
  output_value.append(percentage_bully)
  df_dict['values'] = output_value

  df = pd.DataFrame(df_dict)
  df.to_csv(r"C:\Users\Asus\Documents\miniproject\files\output_files\result.csv")
  
  return 0