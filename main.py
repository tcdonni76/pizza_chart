from mplsoccer import PyPizza, add_image, FontManager
import pandas as pd

params = ["Goals", "xG", "Shots on target", "Progressive Carries", "Dribbles Completed", "Pressures", "Tackles",
          "Interceptions", "Blocks", "Touches", "Pass Completed %", "Assists"]

PLAYER_NAME = "Kevin De Bruyne"

df = pd.read_csv('stats.csv')

player_row_df = df[df['Player'] == PLAYER_NAME]

values = [player_row_df['Gls'], player_row_df['SoT'], player_row_df['Prog'], player_row_df['Succ'], player_row_df['Press'],
          player_row_df['Tkl'], player_row_df['Int'], player_row_df['Blocks'], player_row_df['Touches'],
          player_row_df['CmpPercent'], player_row_df['Ast']]

pizza = PyPizza(

)