import numpy as np
import pandas as pd


dict1 = {
    'attr': ['Name','No_of_tweets','bullying','percentage'],
    'values':['Ramesh','10','5','50.00']
}
df = pd.DataFrame(dict1)
df.to_csv(r"C:\Users\Asus\Documents\miniproject\files\input_files\data.csv")