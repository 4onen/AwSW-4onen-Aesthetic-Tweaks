import renpy
import renpy.display.im as im

banners = {
    "Meet with Remy.": ('four_aesthetics_remybanner','remystatus'),
    "Meet with Anna.": ('four_aesthetics_annabanner','annastatus'),
    "Meet with Bryce.": ('four_aesthetics_brycebanner','brycestatus'),
    "Meet with Adine.": ('four_aesthetics_adinebanner','adinestatus'),
    "Order some lunch.": ('four_aesthetics_lunchboxbanner',''),
    "Meet with Lorem.": ('four_aesthetics_lorembanner','loremstatus'),
    "Meet with Sebastian.": ('four_aesthetics_sebastianbanner','sebastianstatus'),
    "Meet with Emera.": ('four_aesthetics_emerabanner',''),
    "Meet with the store clerk.": ('four_aesthetics_clerkbanner', ''),
    "Meet with Katsuharu.": ('four_aesthetics_katsubanner', ''),
    "Meet with Kevin.": ('four_aesthetics_kevinbanner', ''),
    "Meet with Zhong.": ('four_aesthetics_zhongbanner', ''),
    "Get some well deserved rest.": ('four_aesthetics_pillowbanner', ''),
    "Spend the day reading.": ('four_aesthetics_bookbanner', ''),
    "Listen to your records.": ('four_aesthetics_recordplayerbanner', ''),
}

def register_raw_banner(prompt, im_name, statusvariable=''):
    banners[prompt] = (im_name, statusvariable)

def select_banners(items):
    banner_items = []
    non_banners = []
    for item in items:
        (banner_items if item[0] in banners else non_banners).append(item)
    return banner_items, non_banners



c5doors = {
    "Remy.": (
        'four_aesthetics_remyc5door',
        lambda selected: (" good selected" if selected else " good") if getattr(renpy.store, 'remygoodending', False) else (" neutral selected" if selected else " neutral")
    ),
    # "Anna.": (
    #     'four_aesthetics_annac5door',
    #     lambda selected: (" good selected" if selected else " good") if getattr(renpy.store, 'annagoodending', False) else (" neutral selected" if selected else " neutral")
    # ),
    # "Bryce.": ('four_aesthetics_brycec5door', lambda selected: " good" if getattr(renpy.store, 'brycegoodending', False) else " neutral"),
    # "Adine.": ('four_aesthetics_adinec5door', None),
    # "Lorem.": ('four_aesthetics_loremc5door', lambda selected: " good" if getattr(renpy.store, 'loremstatus', "neutral") == "good" else " neutral"),
    "Go alone.": ('four_aesthetics_alonec5door', None), #lambda selected: " good" if getattr(renpy.store, 'evilpoints', 0) < 30 else " neutral"),
    # "Everyone.": ('four_aesthetics_everyonec5door', None),
}

def register_raw_c5door(prompt, im_name, statusvariable=''):
    banners[prompt] = (im_name, statusvariable)

def select_c5doors(items):
    door_items = []
    non_doors = []
    for item in items:
        (door_items if item[0] in c5doors else non_doors).append(item)

    data = {door[0]: c5doors[door[0]] for door in door_items}

    return door_items, non_doors, data



class BlueMap(im.MatrixColor):
    """
    Retints the image so that blues remap to the
    player color while grey shades map to themselves 
    """
    def __init__(self, im, color, **properties):
        c = renpy.easy.color(color)
        self.color = c

        rgb = c.rgb

        matrix = renpy.display.im.matrix(1-rgb[0], 0, rgb[0], 0, 0,
                                         1-rgb[1], 0, rgb[1], 0, 0,
                                         1-rgb[2], 0, rgb[2], 0, 0,
                                                1, 0,      0, 1, 0)
        super(BlueMap, self).__init__(im, matrix, **properties)

def _bannermod_blue_playercolor_update_fn(_displaytime, _anydisplaytime, im):
    return (BlueMap(im, renpy.store.persistent.playercolor),None)

def blue_to_playercolor_displayable(im):
    return renpy.display.layout.DynamicDisplayable(_bannermod_blue_playercolor_update_fn,im)

def _bannermod_playercolor_update_fn(_displaytime, _anydisplaytime, image):
    return (im.Color(image, renpy.store.persistent.playercolor),None)

def recolor_to_playercolor_displayable(im):
    return renpy.display.layout.DynamicDisplayable(_bannermod_playercolor_update_fn,im)