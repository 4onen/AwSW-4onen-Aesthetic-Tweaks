import renpy
from renpy import ast, config, game, python, exports

from modloader.modclass import Mod, loadable_mod
from modloader.modinfo import has_mod

import jz_magmalink as ml

from four_aesthetics_banners import register_raw_banner


def _show_charmenu(calling_node):
    ast.next_node(calling_node.next)
    ast.statement_name("four_aesthetics_banner_menu")
    
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

def link_bannermod():
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
        ml.ast_utils._create_hook(node_from=paginationif.node, func=_show_charmenu, tag=tag)

    c5menutrailer = ml.find_label('chapter5') \
        .search_say("(Today is the day of the big fireworks. Who shall I bring?)") \
        ._search(lambda n: isinstance(n.next, ast.Menu), 50, "Chapter 5 character menu not within 50 nodes of 'if loremdead == False'")

    ml.ast_utils._create_hook(node_from=c5menutrailer.node, func=_show_charmenu, tag="four_aesthetics_bannermenu_c5pm") 

def link_trimrecolor():
    say_box_trimrecolor = "Frame('image/ui/dialogbox.png' if persistent.four_aesthetics_disable_character_trim_color else four_aesthetics.four_aesthetics_banners.BlueMap('image/ui/dialogbox.png', renpy.get_widget_properties('who').get('color',None) or (persistent.playercolor if not who else None) or '#FFF'), 0, 0)"

    saywindowif = ml.find_screen('say').search_if()

    if not hasattr(saywindowif, 'branch'):
        print("4onen's Aesthetic Tweaks !!WARNING!!: MagmaLink version is too old to safely deconstruct the `say` screen. Trim recoloring will be disabled...")
        return

    ( saywindow
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
    version = "v0.5"
    author = "4onen"
    nsfw = False
    dependencies = ["MagmaLink", "?Chaos_Knight core mod."]

    @classmethod
    def mod_load(cls):
        # Testing link
        # ( ml.find_label('seccont')
        #     .hook_to('bannermod_test_scene')
        # )

        link_bannermod()
        link_trimrecolor()

        if has_mod("Chaos_Knight core mod."):
            register_raw_banner("Meet with Naomi.",'four_aesthetics_naomibanner','naomistatus')

        ml.register_mod_settings(cls, 'four_aesthetics_modsettings')

    @staticmethod
    def mod_complete():
        pass
