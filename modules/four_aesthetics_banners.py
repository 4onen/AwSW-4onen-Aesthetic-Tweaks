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

def _bannermod_playercolor_update_fn(_displaytime, _anydisplaytime, im):
    return (BlueMap(im, renpy.store.persistent.playercolor),None)

def blue_to_playercolor_displayable(im):
    return renpy.display.layout.DynamicDisplayable(_bannermod_playercolor_update_fn,im)
