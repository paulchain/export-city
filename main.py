import shutil
import matplotlib.font_manager as fm
import pandas as pd
from matplotlib import pyplot as plt
from prettymaps import *


cache_path = "./cache"
# the path to cites data
data_path = "./data/worldcities.csv"
# the necessary fields for processing
cities_columns = ["city", "country"]
# Here to change the font
font_name = './fonts/PermanentMarker-Regular.ttf'
# Here to change the radius
default_radius = 1500


def get_image(names=[]):
    if names is None or len(names) == 0:
        return

    # General style parameters
    palette = ['#433633', '#FF5E5B']
    background_c = '#F2F4CB'
    dilate = 100

    # Setup plot
    fig, ax = plt.subplots(figsize=(12, 12), constrained_layout=True)

    backup = plot(
        ",".join(names),

        radius=default_radius,

        ax=ax,

        layers={
            'perimeter': {},
            'streets': {
                'width': {
                    'motorway': 5,
                    'trunk': 5,
                    'primary': 4.5,
                    'secondary': 4,
                    'tertiary': 3.5,
                    'cycleway': 3.5,
                    'residential': 3,
                    'service': 2,
                    'unclassified': 2,
                    'pedestrian': 2,
                    'footway': 1,
                },
                'circle': False, 'dilate': dilate
            },
            'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': True, 'circle': False, 'dilate': dilate},
            'water': {'tags': {'natural': ['water', 'bay']}, 'circle': False, 'dilate': dilate},
            'forest': {'tags': {'landuse': 'forest'}, 'circle': False, 'dilate': dilate},
            'green': {'tags': {'landuse': ['grass', 'orchard'], 'natural': ['island', 'wood'], 'leisure': 'park'}, 'circle': False, 'dilate': dilate},
            'beach': {'tags': {'natural': 'beach'}, 'circle': False, 'dilate': dilate},
            'parking': {'tags': {'amenity': 'parking', 'highway': 'pedestrian', 'man_made': 'pier'}, 'circle': False}
        },

        drawing_kwargs={
            'perimeter': {'fill': False, 'lw': 0, 'zorder': 0},
            'background': {'fc': background_c, 'zorder': -1},
            'green': {'fc': '#8BB174', 'ec': '#2F3737', 'hatch_c': '#A7C497', 'hatch': 'ooo...', 'lw': 1, 'zorder': 1},
            'forest': {'fc': '#64B96A', 'ec': '#2F3737', 'lw': 1, 'zorder': 2},
            'water': {'fc': '#a8e1e6', 'ec': '#2F3737', 'hatch_c': '#9bc3d4', 'hatch': 'ooo...', 'lw': 1, 'zorder': 3},
            'beach': {'fc': '#FCE19C', 'ec': '#2F3737', 'hatch_c': '#d4d196', 'hatch': 'ooo...', 'lw': 1, 'zorder': 3},
            'parking': {'fc': background_c, 'ec': '#2F3737', 'lw': 1, 'zorder': 3},
            'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 4},
            'building': {'palette': palette, 'ec': '#2F3737', 'lw': .5, 'zorder': 5},
        }

    )

    # Set bounds
    xmin, ymin, xmax, ymax = backup['perimeter'].bounds
    dx, dy = xmax-xmin, ymax-ymin
    a = .2
    ax.set_xlim(xmin+a*dx, xmax-a*dx)
    ax.set_ylim(ymin+a*dy, ymax-a*dy)

    ax.text(
        xmin+.39*dx, ymin+.305*dy,
        "\n".join(names),
        color='#2F3737',
        zorder=6,
        rotation=+1.75,
        fontproperties=fm.FontProperties(
            fname=font_name,
            size=24
        )
    )

    file_name = "-".join([n.strip().replace(" ", "_")for n in names])
    plt.savefig(f'./prints/{file_name}.png')
    plt.savefig(f'./prints/{file_name}.svg')

    pass


if __name__ == "__main__":
    print(f"Loading cities from {data_path}")
    data = pd.read_csv(data_path)
    cities = data[cities_columns]
    print(cities.head())
    # TODO: comment this line 110 if running all cities
    #count = 0
    for city in cities.to_numpy():
        print(f"Processing {city}")
        get_image(names=city)
        print(f"Processed {city}")
        # TODO: comment these lines 116-118 if running all cities
        # count += 1
        # if count > 2:
        #     break

    try:
        shutil.rmtree(cache_path)
    except Exception as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

    pass
