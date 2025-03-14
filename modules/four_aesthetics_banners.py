import renpy
import renpy.display.im as im
from renpy import ast, config, game, python, exports

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
    "Adine.":(
        'four_aesthetics_adinec5door',
        lambda selected: (" selected good" if getattr(renpy.store, 'adinestatus', 'neutral')=='good' else " selected") if selected else ""
    ),
    "Anna.": (
        'four_aesthetics_annac5door',
        lambda selected: ((" good selected "+getattr(renpy.store, 'annastatus', "good")) if selected else " good") if getattr(renpy.store, 'annagoodending', False) else (" neutral selected" if selected else " neutral")
    ),
    "Bryce.": (
        'four_aesthetics_brycec5door',
        lambda selected: "" if not selected else (" good" if getattr(renpy.store, 'brycestatus', 'neutral')=='good' else " neutral")
    ),
    "Lorem.": (
        'four_aesthetics_loremc5door',
        lambda selected: (" good" if getattr(renpy.store, 'loremstatus', "neutral") == "good" else " neutral") + (" selected" if selected else "")
    ),
    "Remy.": (
        'four_aesthetics_remyc5door',
        lambda selected: (" good selected" if selected else " good") if getattr(renpy.store, 'remygoodending', False) else (" neutral selected" if selected else " neutral")
    ),
    "Go alone.": ('four_aesthetics_alonec5door playercolorborder', lambda selected: "" if getattr(renpy.store, 'evilpoints', 0) < 30 else (" evil selected" if selected else " evil")),
    "Everyone.": ('four_aesthetics_everyonec5door playercolorborder', lambda selected: " selected" if selected else ""),
}

def register_raw_c5door(prompt, im_name, tagfunction):
    c5doors[prompt] = (im_name, tagfunction)

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

def show_charmenu(calling_node):
    ast.next_node(calling_node.next)
    ast.statement_name("four_aesthetics_banner_menu")
    
    import jz_magmalink as ml
    menu = ml.node(calling_node).search_menu()
    choices = []

    for i, (label, condition, block) in enumerate(menu.node.items):
        if config.say_menu_text_filter:
            label = config.say_menu_text_filter(label)
        
        if block is None:
            renpy.error("Angels with Scaly Wings character menus should not have menu labels without blocks.")
        else:
            if python.py_eval(condition):
                choices.append(((label % exports.tag_quoting_dict) if config.old_substitutions else label, i))

    ast.say_menu_with(menu.node.with_, game.interface.set_transition)

    if not choices:
        return None

    choice = exports.display_menu(choices, screen='four_aesthetics_banners_choice')

    if choice is not None:
        ast.next_node(menu.node.items[choice][2][0])

    return True

def show_c5doormenu(calling_node):
    ast.next_node(calling_node.next)
    ast.statement_name("four_aesthetics_c5doors_menu")
    
    import jz_magmalink as ml
    menu = ml.node(calling_node).search_menu()
    choices = []

    for i, (label, condition, block) in enumerate(menu.node.items):
        if config.say_menu_text_filter:
            label = config.say_menu_text_filter(label)
        
        if block is None:
            renpy.error("Angels with Scaly Wings character menus should not have menu labels without blocks.")
        else:
            if python.py_eval(condition):
                choices.append(((label % exports.tag_quoting_dict) if config.old_substitutions else label, i))

    ast.say_menu_with(menu.node.with_, game.interface.set_transition)

    if not choices:
        return None

    choice = exports.display_menu(choices, screen='four_aesthetics_c5doors_choice')

    if choice is not None:
        ast.next_node(menu.node.items[choice][2][0])

    return True