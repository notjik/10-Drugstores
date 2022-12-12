import sys

from geocoder import get_coords
from map import get_img, show_map
from find_business import find_bis


def main():
    toponym_to_find = ' '.join(sys.argv[1:])
    if toponym_to_find:
        lat, lon = get_coords(toponym_to_find)
        res_find = find_bis(','.join((lat, lon)),
                            '0.005',
                            'Аптека')
        show_map(get_img(res_find, (lat, lon)))


if __name__ == '__main__':
    main()
