import renpy
import renpy.display.im as im

banners = {
    "Meet with Remy.": ('bannermod_four_remybanner','remystatus'),
    "Meet with Anna.": ('bannermod_four_annabanner','annastatus'),
    "Meet with Bryce.": ('bannermod_four_brycebanner','brycestatus'),
    "Meet with Adine.": ('bannermod_four_adinebanner','adinestatus'),
    "Order some lunch.": ('bannermod_four_lunchboxbanner',''),
    "Meet with Lorem.": ('bannermod_four_lorembanner','loremstatus'),
    "Meet with Sebastian.": ('bannermod_four_sebastianbanner','sebastianstatus'),
    "Meet with Emera.": ('bannermod_four_emerabanner',''),
    "Meet with the store clerk.": ('bannermod_four_clerkbanner', ''),
    "Meet with Katsuharu.": ('bannermod_four_katsubanner', ''),
    "Meet with Zhong.": ('bannermod_four_zhongbanner', ''),
    "Get some well deserved rest.": ('bannermod_four_pillowbanner', ''),
}

def register_raw_banner(prompt, im_name, statusvariable=''):
    banners[prompt] = (im_name, statusvariable)

def select_banners(items):
    banner_items = []
    non_banners = []
    for item in items:
        (banner_items if item[0] in banners else non_banners).append(item)
    return banner_items, non_banners

class BannermodPlayerColorMapBlue(im.MatrixColor):
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
        super(BannermodPlayerColorMapBlue, self).__init__(im, matrix, **properties)

def _bannermod_playercolor_update_fn(_displaytime, _anydisplaytime, im):
    return (BannermodPlayerColorMapBlue(im, renpy.store.persistent.playercolor),None)

def blue_to_playercolor_displayable(im):
    return renpy.display.layout.DynamicDisplayable(_bannermod_playercolor_update_fn,im)
