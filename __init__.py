import renpy
import renpy.ast
from modloader.modclass import Mod, loadable_mod
from modloader.modinfo import has_mod

def link_bannermod(ml):
    from four_aesthetics_banners import show_charmenu
    c1csplayed = ml.find_label("chapter1chars") \
        .search_if("chapter1csplayed == 0")

    c2csplayed = ml.find_label("chapter2chars") \
        .search_if("playmessage == True") \
        .search_if("chapter2csplayed == 0")

    cpaginationifs = [
        ("four_aesthetics_bannermenu_c1pm1",c1csplayed.branch().search_say("(What should I do?)")),
        ("four_aesthetics_bannermenu_c1pm2",c1csplayed.branch('chapter1csplayed == 1').search_say("(More free time. What should I do?)")),
        ("four_aesthetics_bannermenu_c2pm1",c2csplayed.branch().search_if('chapter2count >= 7')),
        ("four_aesthetics_bannermenu_c2pm2",c2csplayed.branch('chapter2csplayed == 1').search_if('chapter2count >= 7')),
        ("four_aesthetics_bannermenu_c3pm1",ml.find_label('chapter3chars2').search_if('chapter3count >= 7')),
        ("four_aesthetics_bannermenu_c3pm2",ml.find_label('chapter3chars3').search_if('chapter3count >= 7')),
        ("four_aesthetics_bannermenu_c4pm1",ml.find_label('chapter4chars2').search_if('chapter4count >= 7')),
        ("four_aesthetics_bannermenu_c4pm2",ml.find_label('chapter4chars3').search_if('chapter4count >= 7')),
    ]

    for tag, paginationif in cpaginationifs:
        # Disabling of Saunders' pagination is left to MagmaLink
        ml.ast_utils._create_hook(node_from=paginationif.node, func=show_charmenu, tag=tag)

def link_c5doors(ml):
    from four_aesthetics_banners import show_c5doormenu
    c5menutrailer = ml.find_label('chapter5') \
        .search_say("(Today is the day of the big fireworks. Who shall I bring?)") \
        ._search(lambda n: isinstance(n.next, renpy.ast.Menu), 50, "Chapter 5 character menu not within 50 nodes of 'if loremdead == False'")

    ml.ast_utils._create_hook(
        node_from=c5menutrailer.node,
        func=show_c5doormenu,
        tag="four_aesthetics_c5doors_menu"
    )

def link_trimrecolor(ml):
    say_box_trimrecolor = "Frame('image/ui/dialogbox.png' if persistent.four_aesthetics_disable_character_trim_color else four_aesthetics.four_aesthetics_banners.BlueMap('image/ui/dialogbox.png' if persistent.four_aesthetics_disable_scale_color else 'image/ui/four_aesthetics/dialogbox.png', renpy.get_widget_properties('who').get('color',None) or (persistent.playercolor if not who else None) or '#FFF'), 0, 0)"

    saywindowif = ml.find_screen('say').search_if()

    if not hasattr(saywindowif, 'branch'):
        print("4onen's Aesthetic Tweaks !!WARNING!!: MagmaLink version is too old to safely deconstruct the `say` screen. Trim recoloring will be disabled...")
        return

    saywindow = ( saywindowif
        .branch('not two_window')
        .search_window()
    )

    saywindow.node.keyword.append(('background', say_box_trimrecolor))

    saywindow_line_replacement = ( ml.overlay.Overlay()
        .add("add ('image/ui/dialogline.png' if persistent.four_aesthetics_disable_character_trim_color else renpy.display.im.Recolor('image/ui/dialogline.png', *renpy.easy.color(renpy.get_widget_properties('who').get('color',None) or '#FFF')))")
        .build().first()
    )

    ( saywindow.branch().first().branch()
        .search_if().branch('who')
        .search_add()
        .replace_by(saywindow_line_replacement)
    )

    menu_bg_recolor = ( ml.overlay.Overlay()
        .add("add ('image/ui/choicebg.png' if persistent.four_aesthetics_disable_character_trim_color else four_aesthetics.four_aesthetics_banners.BlueMap('image/ui/choicebg.png', persistent.playercolor or '#00F'))")
        .build().first()
    )

    ( ml.find_screen('choice')
        .search_add()
        .replace_by(menu_bg_recolor)
    )

    nvlwindow_box_trimrecolor = "Frame('image/ui/nvlscreen.png' if persistent.four_aesthetics_disable_character_trim_color else four_aesthetics.four_aesthetics_banners.BlueMap('image/ui/nvlscreen.png', persistent.playercolor or '#00F'), 0, 0)"

    saywindow = ( ml.find_screen('nvl')
        .search_window()
    )
    saywindow.node.keyword.append(('background', nvlwindow_box_trimrecolor))


@loadable_mod
class AwSWMod(Mod):
    name = "4onen's Aesthetic Tweaks"
    version = "v0.6"
    author = "4onen"
    nsfw = False
    dependencies = ["MagmaLink", "?Chaos_Knight core mod.", "?Redemption"]

    @classmethod
    def mod_load(cls):
        import jz_magmalink as ml
        # Testing link
        # ( ml.find_label('seccont')
        #     .hook_to('four_c5doorsmod_test_scene')
        # )

        link_bannermod(ml)
        link_c5doors(ml)
        link_trimrecolor(ml)

        if has_mod("Chaos_Knight core mod."):
            from four_aesthetics_banners import register_raw_banner, register_raw_c5door
            register_raw_banner("Meet with Naomi.",'four_aesthetics_naomibanner','naomistatus')
            register_raw_c5door("Naomi.",'four_aesthetics_naomic5door', lambda selected: (" selected" if selected else "") + (" good" if getattr(renpy.store, 'naomiromance', 0) > 50 else (" worstend" if getattr(renpy.store, 'ecknaomim3earlyleave', True) else " neutral")))
        
        if has_mod("Redemption"):
            from four_aesthetics_banners import register_raw_banner, register_raw_c5door
            register_raw_banner("Meet with Maverick.",'four_aesthetics_maverickbanner','maverickstatus')
            register_raw_c5door("Maverick.",'four_aesthetics_maverickc5door', lambda selected: (" selected" if selected else "") + (" good" if getattr(renpy.store, 'maverick_redem_dream', True) and getattr(renpy.store, 'maverick_redem_mapgiven', True) else (" neutral" if getattr(renpy.store, 'maverick_redem_dream', False) or getattr(renpy.store, 'maverick_redem_mapgiven', False) else " worstend")))
            

        ml.register_mod_settings(cls, 'four_aesthetics_modsettings')

    @staticmethod
    def mod_complete():
        pass
