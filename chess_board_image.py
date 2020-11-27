
import requests

def get_chess_image(fen_string : str):

    url = 'https://chessboardimage.com/' + fen_string + ".png"
    response = requests.get(url)
    if response.status_code == 200:
        with open('tmp.png', 'wb') as f:
            for chunk in response:
                f.write(chunk)

