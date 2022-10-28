from typing import final
from rylai.scrape import webscrape
from enigma.preprocessing import preprocess_tweets
from enigma.output import final_output
from enigma.bert_tokenizer import tokenize
website1 = "https://twitter.com/mrr59999123"
website2 = "https://twitter.com/RAMESH_ROKETMAN"
website3 = "https://twitter.com/hateboy_r"

if __name__ == "__main__":
    profile_name = webscrape(website3)
    preprocess_tweets()
    final_output(profile_name,tokenize)
