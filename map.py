import requests
import pygame
from io import BytesIO
from PIL import Image


def get_img(coords, scoords):
    for i, elem in enumerate(coords):
        if 'Hours' in elem[1]:
            if 'TwentyFourHours' in elem[1]['Hours']['Availabilities'][0]:
                coords[i][1] = 'gn'
            elif 'Intervals' in elem[1]['Hours']['Availabilities'][0]:
                coords[i][1] = 'bl'
            else:
                coords[i][1] = 'gr'
        else:
            coords[i][1] = 'gr'
    map_server = 'https://static-maps.yandex.ru/1.x/'
    params = {'l': 'map',
              'pt': f"{','.join(coords[0][0])},pm2{coords[0][1]}m~"
                    f"{','.join(coords[1][0])},pm2{coords[1][1]}m~"
                    f"{','.join(coords[2][0])},pm2{coords[2][1]}m~"
                    f"{','.join(coords[3][0])},pm2{coords[3][1]}m~"
                    f"{','.join(coords[4][0])},pm2{coords[4][1]}m~"
                    f"{','.join(coords[5][0])},pm2{coords[5][1]}m~"
                    f"{','.join(coords[6][0])},pm2{coords[6][1]}m~"
                    f"{','.join(coords[7][0])},pm2{coords[7][1]}m~"
                    f"{','.join(coords[8][0])},pm2{coords[8][1]}m~"
                    f"{','.join(coords[9][0])},pm2{coords[9][1]}m~"
                    f"{','.join(scoords)},home"}
    response = requests.get(map_server, params=params)
    Image.open(BytesIO(response.content)).save('map.png')
    return 'map.png'


def show_map(mapp):
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(mapp), (0, 0))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
