from transformers import TFBertModel
import tensorflow as tf
from bert_tokenizer import tokenize


bert_model = TFBertModel.from_pretrained('bert-base-uncased')


def create_model(bert_model, max_len):
    
    ##params###
    opt = tf.keras.optimizers.Adam(learning_rate=1e-5, decay=1e-7)
    loss = tf.keras.losses.CategoricalCrossentropy()
    accuracy = tf.keras.metrics.CategoricalAccuracy()


    input_ids = tf.keras.Input(shape=(max_len,),dtype='int32')
    attention_masks = tf.keras.Input(shape=(max_len,),dtype='int32')
    embeddings = bert_model.bert([input_ids,attention_masks])[1]
    output = tf.keras.layers.Dense(2, activation="softmax")(embeddings)
    model = tf.keras.models.Model(inputs = [input_ids,attention_masks], outputs = output)
    model.compile(opt, loss=loss, metrics=accuracy)

    return model

model = create_model(bert_model, 128)
model.summary()