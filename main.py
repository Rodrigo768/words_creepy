meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "ROFL se utiliza como reacción a algo gracioso, similar a LOL"
            }

something = input("escriban una palabra que no entiendan")


if something in meme_dict.keys():
  print(meme_dict[something])
else:
  print("esa palabra aun no la tenemos")
