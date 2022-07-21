
image bannermod_four_banner = "ui/bannermod/banner.png"
image bannermod_four_arrow = "ui/bannermod/arrow.png"
image bannermod_four_arrow flip = im.Flip("ui/bannermod/arrow.png", horizontal=True)

image bannermod_four_menu_frame = Frame("image/ui/nvlscreen.png",195,195,tile=True)

####
# Main cast
####
image bannermod_four_lunchboxbanner neutral = im.Composite(
    (515,960),
    (0,0), im.Recolor("ui/bannermod/banner.png", 74, 93, 136),
    (0,0), "ui/bannermod/lunchbox.png",
)
image bannermod_four_adinebanner neutral = im.Composite(
    (515,960),
    (0,0), im.Recolor("ui/bannermod/banner.png", 74, 93, 136),
    (-20,121), im.Crop("cr/adine_normal_b.png",(0,0,420,839)),
)
image bannermod_four_adinebanner good = im.Composite(
    (515,960),
    (0,0), im.Recolor("ui/bannermod/banner.png", 74, 93, 136),
    (75,121), im.Crop("cr/adine_giggle_b.png",(95,0,325,839)),
    (-20,121), im.Crop("cr/adine_giggle_b.png",(0,0,420,460)),
)


image bannermod_four_annabanner neutral = im.Composite(
    (515,960),
    (0,0), im.Recolor("ui/bannermod/banner.png", 121, 77, 128),
    (0,133), im.Crop("cr/anna_normal_b.png",(0,0,400,827)),
    (0,133), im.Crop("cr/anna_normal_b.png",(0,0,455,140)),
)
image bannermod_four_annabanner good = im.Composite(
    (515,960),
    (0,0), im.Recolor("ui/bannermod/banner.png", 121, 77, 128),
    (0,133), im.Crop("cr/anna_smirk_b.png",(0,0,400,827)),
    (0,133), im.Crop("cr/anna_smirk_b.png",(0,0,455,140)),
)


image bannermod_four_brycebanner neutral = im.Composite(
    (515,960),
    (0,0), im.Recolor("ui/bannermod/banner.png", 94, 132, 85),
    (-40,70), im.Crop("cr/bryce_normal_b.png", (0,0,440,960)),
    (-40,70), im.Crop("cr/bryce_normal_b.png", (0,0,545,230)),
)
image bannermod_four_brycebanner good = im.Composite(
    (515,960),
    (0,0), im.Recolor("ui/bannermod/banner.png", 94, 132, 85),
    (-40,70), im.Crop("cr/bryce_smirk_b.png", (0,0,440,960)),
    (-40,70), im.Crop("cr/bryce_smirk_b.png", (0,0,545,230)),
)


image bannermod_four_lorembanner neutral = im.Composite(
    (515,960),
    (0,0), im.Recolor("ui/bannermod/banner.png", 224, 188, 129),
    (75,310), im.Crop("cr/lorem_normal.png", (455,0,325,650)),
    (0,310), im.Crop("cr/lorem_normal.png", (380,0,80,200)),
)
image bannermod_four_lorembanner good = im.Composite(
    (515,960),
    (0,0), im.Recolor("ui/bannermod/banner.png", 224, 188, 129),
    (75,310), im.Crop("cr/lorem_shy.png", (455,0,325,650)),
    (0,310), im.Crop("cr/lorem_shy.png", (380,0,80,200)),
)


image bannermod_four_remybanner neutral = im.Composite(
    (515,960),
    (0,0), im.Recolor("ui/bannermod/banner.png", 147, 54, 62),
    (0,108), im.Crop("cr/remy_normal.png", (0,0,400,960)),
    (0,108), im.Crop("cr/remy_normal.png", (0,0,515,450)),
)
image bannermod_four_remybanner good = im.Composite(
    (515,960),
    (0,0), im.Recolor("ui/bannermod/banner.png", 147, 54, 62),
    (0,108), im.Crop("cr/remy_smile.png", (0,0,400,960)),
    (0,108), im.Crop("cr/remy_smile.png", (0,0,515,450)),
)

####
# Main cast
####
image bannermod_four_emerabanner neutral = im.Composite(
    (515,960),
    (0,0), im.Recolor("ui/bannermod/banner.png", 181, 190, 131),
    (0,115), im.Crop("cr/emera_normal.png", (0,0,400,845)),
)


image bannermod_four_katsubanner neutral = im.Composite(
    (515,960),
    (0,0), im.Recolor("ui/bannermod/banner.png", 198, 198, 198),
    (0,0), im.Crop("cr/katsu_normal.png", (0,30,400,960)),
)
image bannermod_four_katsubanner good = im.Composite(
    (515,960),
    (0,0), im.Recolor("ui/bannermod/banner.png", 198, 198, 198),
    (0,0), im.Crop("cr/katsu_smile.png", (0,30,400,960)),
)


image bannermod_four_sebastianbanner neutral = im.Composite(
    (515,960),
    (0,0), im.Recolor("ui/bannermod/banner.png", 142, 112, 78),
    (0,236), im.Crop("cr/sebastian_normal_b.png", (70,0,420,500)),
    (75,236), im.Crop("cr/sebastian_normal_b.png", (145,0,325,724)),
)
image bannermod_four_sebastianbanner good = im.Composite(
    (515,960),
    (0,0), im.Recolor("ui/bannermod/banner.png", 142, 112, 78),
    (0,236), im.Crop("cr/sebastian_smile_b.png", (70,0,420,500)),
    (75,236), im.Crop("cr/sebastian_smile_b.png", (145,0,325,724)),
)


image bannermod_four_clerkbanner neutral = im.Composite(
    (515,960),
    (0,0), im.Recolor("ui/bannermod/banner.png", 126, 145, 71),
    (0,90), im.Crop("cr/zhong_normal_c.png", (30,0,400,340)),
    (75,90), im.Crop("cr/zhong_normal_c.png", (105,0,325,872)),
)
image bannermod_four_zhongbanner neutral = im.Composite(
    (515,960),
    (0,0), im.Recolor("ui/bannermod/banner.png", 126, 145, 71),
    (0,90), im.Crop("cr/zhong_normal_c.png", (30,0,400,340)),
    (75,90), im.Crop("cr/zhong_normal_c.png", (105,0,325,872)),
)





init python in bannermenu_four:

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
        "[[Show more banners.]": ('bannermod_four_arrow',''),
        "[[Show prev banners.]": ('bannermod_four_arrow flip',''),
    }

    @renpy.pure
    def select_banners(items):
        banner_items = []
        non_banners = []
        for item in items:
            (banner_items if item[0] in banners else non_banners).append(item)
        return banner_items, non_banners

init python:
    style.bannermenu_four_menu_window = Style(style.nvl_window)
    style.bannermenu_four_menu_window.background = 'bannermod_four_menu_frame'
    style.bannermenu_four_menu_window.yfill = False
    style.bannermenu_four_menu_window.xpadding = 20
    style.bannermenu_four_menu_window.ypadding = 30

    style.bannermenu_four_menu_banner = Style(style.menu_choice_button)
    style.bannermenu_four_menu_banner.xminimum = 0
    style.bannermenu_four_menu_banner.xmaximum = 225


transform bannermenu_four_menu_banner_selection_alpha:
    on idle:
        linear 0.25 alpha 0.7
    on hover:
        alpha 1.0


screen bannermenu_four_choice(items):
    window:
        style "bannermenu_four_menu_window"
        xalign 0.5
        yalign 0.0

        has vbox at zoom_fade_in:
            style "nvl_vbox"
            xalign 0.5

        if renpy.get_screen("say"):
            ysize 700
        else:
            yfill True

        $ banner_items, non_banners = bannermenu_four.select_banners(items)

        if banner_items:
            hbox:
                yalign 0.0
                xalign 0.5

                if len(banner_items) > 1 and (banner_items[-1][0] == "[[Show prev banners.]"):
                    button at bannermenu_four_menu_banner_selection_alpha:
                        action [banner_items[-1][1], Play("audio", "se/sounds/select3.ogg")]
                        hovered Play("audio", "se/sounds/select.ogg")
                        style "bannermenu_four_menu_banner"

                        add 'bannermod_four_arrow flip':
                            zoom 0.5

                for caption, action, _ in banner_items:
                    if caption not in ["[[Show more banners.]","[[Show prev banners.]"]:
                        python:
                            banner_image, banner_status = bannermenu_four.banners[caption]
                            banner_status_label = " good" if getattr(renpy.store, banner_status, None) == "good" else " neutral"

                        button at bannermenu_four_menu_banner_selection_alpha:
                            action [action, Play("audio", "se/sounds/select3.ogg")]
                            hovered Play("audio", "se/sounds/select.ogg")
                            style "bannermenu_four_menu_banner"

                            has vbox:
                                add (banner_image+banner_status_label):
                                    zoom 0.5

                                text caption style "menu_choice"

                if len(banner_items) > 1 and (banner_items[-2][0] == "[[Show more banners.]"):
                    button at bannermenu_four_menu_banner_selection_alpha:
                        action [banner_items[-2][1], Play("audio", "se/sounds/select3.ogg")]
                        hovered Play("audio", "se/sounds/select.ogg")
                        style "bannermenu_four_menu_banner"

                        add 'bannermod_four_arrow':
                            zoom 0.5

        if banner_items and non_banners:
            fixed:
                xfill True
                ysize 5
                add 'white'

        if non_banners:
            vbox:
                style "menu"
                xalign 0.5

                for caption, action, _ in non_banners:

                    if action:

                        button:
                            action [action, Play("audio", "se/sounds/select3.ogg")]
                            hovered Play("audio", "se/sounds/select.ogg")
                            style "menu_choice_button"

                            text caption style "menu_choice"

                    else:
                        text caption style "menu_caption"


label bannermod_test_scene:
    python:
        print(renpy.display_menu(
            [ (p,p) for p in bannermenu_four.banners.keys()]+
            [ ("Spend the day reading.","read") ],
            screen='bannermenu_four_choice'
        ))

    $ renpy.quit()
