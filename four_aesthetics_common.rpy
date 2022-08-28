init:
    image four_aesthetics_arrow = im.Scale("image/ui/filepicker/Btn_Next.png", 450, 960)
    image four_aesthetics_arrow flip = im.Flip(im.Scale("image/ui/filepicker/Btn_Next.png", 450, 960), horizontal=True)

    ####
    # Main cast
    ####
    image four_aesthetics_lunchboxbanner neutral = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 74, 93, 136),
        (0,0), "ui/four_aesthetics/lunchbox.png",
    )
    image four_aesthetics_adinebanner neutral = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 74, 93, 136),
        (-20,121), im.Crop("cr/adine_normal_b.png",(0,0,420,839)),
    )
    image four_aesthetics_adinebanner good = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 74, 93, 136),
        (75,121), im.Crop("cr/adine_giggle_b.png",(95,0,325,839)),
        (-20,121), im.Crop("cr/adine_giggle_b.png",(0,0,420,460)),
    )


    image four_aesthetics_annabanner neutral = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 121, 77, 128),
        (0,133), im.Crop("cr/anna_normal_b.png",(0,0,400,827)),
        (0,133), im.Crop("cr/anna_normal_b.png",(0,0,455,140)),
    )
    image four_aesthetics_annabanner good = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 121, 77, 128),
        (0,133), im.Crop("cr/anna_smirk_b.png",(0,0,400,827)),
        (0,133), im.Crop("cr/anna_smirk_b.png",(0,0,455,140)),
    )


    image four_aesthetics_brycebanner neutral = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 94, 132, 85),
        (-40,70), im.Crop("cr/bryce_normal_b.png", (0,0,440,960)),
        (-40,70), im.Crop("cr/bryce_normal_b.png", (0,0,545,230)),
    )
    image four_aesthetics_brycebanner good = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 94, 132, 85),
        (-40,70), im.Crop("cr/bryce_smirk_b.png", (0,0,440,960)),
        (-40,70), im.Crop("cr/bryce_smirk_b.png", (0,0,545,230)),
    )


    image four_aesthetics_lorembanner neutral = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 224, 188, 129),
        (75,310), im.Crop("cr/lorem_normal.png", (455,0,325,650)),
        (0,310), im.Crop("cr/lorem_normal.png", (380,0,80,200)),
    )
    image four_aesthetics_lorembanner good = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 224, 188, 129),
        (75,310), im.Crop("cr/lorem_happy.png", (455,0,325,650)),
        (0,310), im.Crop("cr/lorem_happy.png", (380,0,80,200)),
    )


    image four_aesthetics_remybanner neutral = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 147, 54, 62),
        (0,108), im.Crop("cr/remy_normal.png", (0,0,400,960)),
        (0,108), im.Crop("cr/remy_normal.png", (0,0,515,450)),
    )
    image four_aesthetics_remybanner good = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 147, 54, 62),
        (0,108), im.Crop("cr/remy_smile.png", (0,0,400,960)),
        (0,108), im.Crop("cr/remy_smile.png", (0,0,515,450)),
    )

    ####
    # Side cast
    ####
    image four_aesthetics_emerabanner neutral = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 181, 190, 131),
        (0,115), im.Crop("cr/emera_normal.png", (0,0,400,845)),
    )


    image four_aesthetics_katsubanner neutral = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 198, 198, 198),
        (0,0), im.Crop("cr/katsu_normal.png", (0,30,400,960)),
    )
    image four_aesthetics_katsubanner good = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 198, 198, 198),
        (0,0), im.Crop("cr/katsu_smile.png", (0,30,400,960)),
    )


    image four_aesthetics_kevinbanner neutral = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 105, 105, 105),
        (0,100), im.Crop("cr/kevin_normal.png", (115,0,400,895)),
        (0,100), im.Crop("cr/kevin_normal.png", (115,0,410,650)),
    )


    image four_aesthetics_sebastianbanner neutral = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 142, 112, 78),
        (0,236), im.Crop("cr/sebastian_normal_b.png", (70,0,420,300)),
        (75,236), im.Crop("cr/sebastian_normal_b.png", (145,0,325,724)),
    )
    image four_aesthetics_sebastianbanner good = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 142, 112, 78),
        (0,236), im.Crop("cr/sebastian_smile_b.png", (70,0,420,300)),
        (75,236), im.Crop("cr/sebastian_smile_b.png", (145,0,325,724)),
    )


    image four_aesthetics_clerkbanner neutral = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 126, 145, 71),
        (0,90), im.Crop("cr/zhong_normal_c.png", (30,0,400,340)),
        (75,90), im.Crop("cr/zhong_normal_c.png", (105,0,325,872)),
    )
    image four_aesthetics_zhongbanner neutral = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 126, 145, 71),
        (0,90), im.Crop("cr/zhong_normal_b.png", (30,0,400,340)),
        (75,90), im.Crop("cr/zhong_normal_b.png", (105,0,325,872)),
    )

    ####
    # Mod cast
    ####
    image four_aesthetics_naomibanner neutral = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 190, 116, 164),
        (0,60), im.Crop("cr/naomi_normal_b.png", (65,0,400,903)),
        (0,60), im.Crop("cr/naomi_normal_b.png", (65,0,500,220)),
    )
    image four_aesthetics_naomibanner good = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner.png", 190, 116, 164),
        (0,60), im.Crop("cr/naomi_smile_b.png", (65,0,400,903)),
        (0,60), im.Crop("cr/naomi_smile_b.png", (65,0,500,220)),
    )


init python in four_aesthetics:
    import four_aesthetics_banners
    from four_aesthetics_banners import select_banners

    select_banners = renpy.pure(select_banners)

    n_banner = 5
    n_non_banner = 3

init:
    image four_aesthetics_pillowbanner neutral = four_aesthetics.four_aesthetics_banners.blue_to_playercolor_displayable(
        im.Composite(
            (515,960),
            (0,0), im.Recolor("ui/four_aesthetics/banner.png", 0, 0, 255),
            (0,0), "ui/four_aesthetics/pillow.png",
            (0,0), "ui/four_aesthetics/skipmark.png",
        )
    )

    image four_aesthetics_bookbanner neutral = four_aesthetics.four_aesthetics_banners.blue_to_playercolor_displayable(
        im.Composite(
            (515,960),
            (0,0), im.Recolor("ui/four_aesthetics/banner.png", 0, 0, 255),
            (0,0), "ui/four_aesthetics/books.png",
            (0,0), "ui/four_aesthetics/skipmark.png",
        )
    )

    image four_aesthetics_recordplayerbanner neutral = im.Composite(
        (515,960),
        (0,0), im.Recolor("ui/four_aesthetics/banner_swoopbottom.png", 126, 145, 71),
        (0,0), "ui/four_aesthetics/record_player.png",
    )

init python:
    style.four_aesthetics_banners_menu_window = Style(style.nvl_window)
    style.four_aesthetics_banners_menu_window.yfill = False
    style.four_aesthetics_banners_menu_window.xpadding = 20
    style.four_aesthetics_banners_menu_window.ypadding = 30

    style.four_aesthetics_banners_menu_banner = Style(style.menu_choice_button)
    style.four_aesthetics_banners_menu_banner.xminimum = 0
    style.four_aesthetics_banners_menu_banner.xmaximum = 225


transform four_aesthetics_banners_menu_selection_alpha:
    on idle:
        linear 0.25 alpha 0.7
    on hover:
        alpha 1.0


screen four_aesthetics_banners_choice(items):
    default banneroffset = 0
    default nonbanneroffset = 0
    window:
        style "four_aesthetics_banners_menu_window"
        background (Frame("image/ui/nvlscreen.png" if persistent.four_aesthetics_disable_character_trim_color else four_aesthetics.four_aesthetics_banners.BlueMap("image/ui/nvlscreen.png", persistent.playercolor or '#FFF'), 195, 195, tile=True))
        xalign 0.5
        yalign 0.0

        has vbox at zoom_fade_in:
            style "nvl_vbox"
            xalign 0.5

        if renpy.get_screen("say"):
            ysize 700
        else:
            yfill True

        $ banner_items, non_banners = four_aesthetics.select_banners(items)

        if banner_items:
            hbox:
                yalign 0.0
                xalign 0.5

                if len(banner_items) > four_aesthetics.n_banner:
                    button at four_aesthetics_banners_menu_selection_alpha:
                        action [
                            SetScreenVariable('banneroffset', banneroffset-four_aesthetics.n_banner if banneroffset >= four_aesthetics.n_banner else len(banner_items)-(len(banner_items) % four_aesthetics.n_banner)),
                            Play("audio", "se/sounds/select3.ogg")
                        ]
                        hovered Play("audio", "se/sounds/select.ogg")
                        style "four_aesthetics_banners_menu_banner"

                        add 'four_aesthetics_arrow flip':
                            zoom 0.5

                for caption, action, _ in banner_items[banneroffset:banneroffset+four_aesthetics.n_banner]:
                    if caption not in ["[[Show more banners.]","[[Show prev banners.]"]:
                        python:
                            banner_image, banner_status = four_aesthetics.four_aesthetics_banners.banners[caption]
                            banner_status_label = " good" if getattr(renpy.store, banner_status, None) == "good" else " neutral"

                        button at four_aesthetics_banners_menu_selection_alpha:
                            action [action, Play("audio", "se/sounds/select3.ogg")]
                            hovered Play("audio", "se/sounds/select.ogg")
                            style "four_aesthetics_banners_menu_banner"

                            has vbox:
                                add (banner_image+banner_status_label):
                                    zoom 0.5

                                text caption style "menu_choice"

                if len(banner_items) > four_aesthetics.n_banner:
                    button at four_aesthetics_banners_menu_selection_alpha:
                        action [
                            SetScreenVariable('banneroffset', 0 if banneroffset+four_aesthetics.n_banner>=len(banner_items) else banneroffset+four_aesthetics.n_banner),
                            Play("audio", "se/sounds/select3.ogg")
                        ]
                        hovered Play("audio", "se/sounds/select.ogg")
                        style "four_aesthetics_banners_menu_banner"

                        add 'four_aesthetics_arrow':
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

                for caption, action, _ in non_banners[nonbanneroffset:nonbanneroffset+four_aesthetics.n_non_banner]:

                    if action:

                        button:
                            action [action, Play("audio", "se/sounds/select3.ogg")]
                            hovered Play("audio", "se/sounds/select.ogg")
                            style "menu_choice_button"

                            text caption style "menu_choice"

                    else:
                        text caption style "menu_caption"

                if len(non_banners) > four_aesthetics.n_non_banner + 1:
                    button:
                        action [
                            SetScreenVariable('nonbanneroffset', 0 if nonbanneroffset+four_aesthetics.n_non_banner>=len(non_banners) else nonbanneroffset+four_aesthetics.n_non_banner), 
                            Play("audio", "se/sounds/select3.ogg")
                        ]
                        hovered Play("audio", "se/sounds/select.ogg")
                        style "menu_choice_button"

                        text "[[Show more options.]" style "menu_choice"



label bannermod_test_scene:
    python:
        print(renpy.display_menu(
            [ (p,p) for p in four_aesthetics_banners.four_aesthetics.banners.keys()]+
            [ ("Spend the day reading.","read") ],
            screen='four_aesthetics_banners_choice'
        ))

    $ renpy.quit()


screen four_aesthetics_modsettings():
    tag smallscreen2
    modal True
    window id "four_aesthetics_modsettings" at popup2:
        style "smallwindow"
        vbox:
            align (0.5, 0.5)

            hbox:
                align (0.5, 0.5)
                spacing 10

                imagebutton:
                    xcenter 0.5
                    ycenter 0.5
                    idle im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70)
                    hover im.Recolor(im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70), 64, 64, 64)
                    selected_idle im.Scale("ui/nsfw_chbox-checked.png", 70, 70)
                    selected_hover im.Recolor(im.Scale("ui/nsfw_chbox-checked.png", 70, 70), 64, 64, 64)
                    action [MTSTogglePersistentBool("four_aesthetics_disable_character_trim_color"),
                            Play("audio", "se/sounds/yes.wav")]
                    hovered Play("audio", "se/sounds/select.ogg")
                    focus_mask None
                text _("Disable menu trim recoloring")
        imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Show("_ml_mod_settings"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button
