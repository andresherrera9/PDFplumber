import os
import pdfplumber
import pandas as pd

directory = '*Path al directorio con los pdf*'
final_df = pd.DataFrame()
table_settings= {
    "vertical_strategy": "lines", 
    "horizontal_strategy": "text",
    "explicit_vertical_lines": [],
    "explicit_horizontal_lines": [],
    "snap_tolerance": 3,
    "join_tolerance": 3,
    "edge_min_length": 3,
    "min_words_vertical": 3,
    "min_words_horizontal": 1,
    "keep_blank_chars": False,
    "text_tolerance": 3,
    "text_x_tolerance": None,
    "text_y_tolerance": None,
    "intersection_tolerance": 3,
    "intersection_x_tolerance": None,
    "intersection_y_tolerance": None,
}
for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        
        df= pdfplumber.open(directory + filename)
        hola = df.pages[0]
        table = hola.extract_table(table_settings)
        df = pd.DataFrame(table)
        final_df = final_df.append(df, ignore_index=True)

final_df= final_df[(final_df == '*Palabra en row deseada*').any(axis=1)]

x = final_df[1]
y = x.str.replace('$', '')
z = y.str.replace(',', '')
z = [int(float(i)) for i in z]
print(sum(z))    

