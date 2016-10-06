# -*- coding: utf-8 -*-

"""
Boxy Theme Presets
"""

import sublime
import sublime_plugin
from collections import OrderedDict


NO_SELECTION = -1

PREFERENCES = 'Preferences.sublime-settings'

OPTIONS = [
    'theme_accent_blue',
    'theme_accent_cyan',
    'theme_accent_green',
    'theme_accent_lime',
    'theme_accent_mono',
    'theme_accent_numix',
    'theme_accent_orange',
    'theme_accent_pink',
    'theme_accent_purple',
    'theme_accent_sky',
    'theme_accent_tangerine',
    'theme_autocomplete_item_selected_colored',
    'theme_bar',
    'theme_bar_colored',
    'theme_bar_logo_atomized',
    'theme_bar_logo_materialized',
    'theme_bar_margin_top_lg',
    'theme_bar_margin_top_md',
    'theme_bar_margin_top_sm',
    'theme_bar_shadow_hidden',
    'theme_button_rounded',
    'theme_dirty_accent_blue',
    'theme_dirty_accent_green',
    'theme_dirty_accent_orange',
    'theme_dirty_accent_purple',
    'theme_dirty_accent_tangerine',
    'theme_dirty_accent_cyan',
    'theme_dirty_accent_lime',
    'theme_dirty_accent_pink',
    'theme_dirty_accent_sky',
    'theme_dirty_accent_numix',
    'theme_dirty_colored_always',
    'theme_dirty_materialized',
    'theme_dropdown_atomized',
    'theme_dropdown_materialized',
    'theme_find_panel_atomized',
    'theme_find_panel_close_hidden',
    'theme_find_panel_font_lg',
    'theme_find_panel_font_md',
    'theme_find_panel_font_sm',
    'theme_find_panel_font_xl',
    'theme_find_panel_font_xs',
    'theme_find_panel_materialized',
    'theme_find_panel_padding_lg',
    'theme_find_panel_padding_md',
    'theme_find_panel_padding_sm',
    'theme_find_panel_padding_xl',
    'theme_find_panel_padding_xs',
    'theme_find_panel_size_lg',
    'theme_find_panel_size_md',
    'theme_find_panel_size_sm',
    'theme_find_panel_size_xl',
    'theme_find_panel_size_xs',
    'theme_find_panel_size_xxs',
    'theme_font_lg',
    'theme_font_md',
    'theme_font_sm',
    'theme_font_xl',
    'theme_font_xs',
    'theme_grid_border_size_lg',
    'theme_grid_border_size_md',
    'theme_grid_border_size_sm',
    'theme_grid_border_size_xl',
    'theme_grid_border_size_xs',
    'theme_icon_button_highlighted',
    'theme_icons_atomized',
    'theme_icons_materialized',
    'theme_panel_switcher_atomized',
    'theme_panel_switcher_materialized',
    'theme_popup_border_visible',
    'theme_quick_panel_border_visible',
    'theme_quick_panel_item_selected_colored',
    'theme_quick_panel_size_lg',
    'theme_quick_panel_size_md',
    'theme_quick_panel_size_sm',
    'theme_quick_panel_size_xl',
    'theme_quick_panel_size_xs',
    'theme_scrollbar_colored',
    'theme_scrollbar_line',
    'theme_scrollbar_semi_overlayed',
    'theme_scrollbar_rounded',
    'theme_sidebar_border',
    'theme_sidebar_close_always_visible',
    'theme_sidebar_disclosure',
    'theme_sidebar_file_icons_hidden',
    'theme_sidebar_folder_arrow',
    'theme_sidebar_folder_atomized',
    'theme_sidebar_folder_materialized',
    'theme_sidebar_folder_mono',
    'theme_sidebar_font_lg',
    'theme_sidebar_font_md',
    'theme_sidebar_font_sm',
    'theme_sidebar_font_xl',
    'theme_sidebar_font_xs',
    'theme_sidebar_heading_bold',
    'theme_sidebar_highlight_selected_text_only',
    'theme_sidebar_highlight_text_only',
    'theme_sidebar_icon_saturation_hg',
    'theme_sidebar_icon_saturation_lw',
    'theme_sidebar_icon_saturation_md',
    'theme_sidebar_icon_saturation_xh',
    'theme_sidebar_indent_lg',
    'theme_sidebar_indent_md',
    'theme_sidebar_indent_sm',
    'theme_sidebar_indent_top_level_disabled',
    'theme_sidebar_indent_xl',
    'theme_sidebar_indent_xs',
    'theme_sidebar_size_lg',
    'theme_sidebar_size_md',
    'theme_sidebar_size_sm',
    'theme_sidebar_size_xl',
    'theme_sidebar_size_xs',
    'theme_sidebar_size_xxs',
    'theme_size_lg',
    'theme_size_md',
    'theme_size_sm',
    'theme_size_xl',
    'theme_size_xs',
    'theme_statusbar_colored',
    'theme_statusbar_font_lg',
    'theme_statusbar_font_md',
    'theme_statusbar_font_sm',
    'theme_statusbar_font_xl',
    'theme_statusbar_font_xs',
    'theme_statusbar_label_bold',
    'theme_statusbar_size_lg',
    'theme_statusbar_size_md',
    'theme_statusbar_size_sm',
    'theme_statusbar_size_xl',
    'theme_statusbar_size_xs',
    'theme_tab_arrows_hidden',
    'theme_tab_close_always_visible',
    'theme_tab_font_lg',
    'theme_tab_font_md',
    'theme_tab_font_sm',
    'theme_tab_font_xl',
    'theme_tab_font_xs',
    'theme_tab_highlight_text_only',
    'theme_tab_label_bold',
    'theme_tab_line_size_lg',
    'theme_tab_line_size_sm',
    'theme_tab_mouse_wheel_switch',
    'theme_tab_rounded',
    'theme_tab_selected_filled',
    'theme_tab_selected_label_bold',
    'theme_tab_selected_overlined',
    'theme_tab_selected_prelined',
    'theme_tab_selected_transparent',
    'theme_tab_selected_underlined',
    'theme_tab_separator',
    'theme_tab_size_lg',
    'theme_tab_size_md',
    'theme_tab_size_sm',
    'theme_tab_size_xl',
    'theme_tab_size_xs',
    'theme_tab_size_xxl',
    'theme_tab_width_auto',
    "theme_tabset_line_visible",
    'theme_tooltips_font_lg',
    'theme_tooltips_font_md',
    'theme_tooltips_font_sm',
    'theme_tooltips_font_xl',
    'theme_tooltips_font_xs',
    'theme_unified'
]

PRESETS = OrderedDict(
    [
        (
            'Atom',
            [
                'theme_accent_sky',
                'theme_button_rounded',
                'theme_find_panel_close_hidden',
                'theme_grid_border_size_lg',
                'theme_icon_button_highlighted',
                'theme_icons_atomized',
                'theme_popup_border_visible',
                'theme_scrollbar_rounded',
                'theme_sidebar_disclosure',
                'theme_sidebar_indent_top_level_disabled',
                'theme_tab_rounded',
                'theme_tab_selected_prelined',
                'theme_tab_separator'
            ]
        ),
        (
            'Code',
            [
                'theme_accent_purple',
                'theme_bar',
                'theme_sidebar_disclosure',
                'theme_sidebar_indent_sm',
                'theme_statusbar_colored',
                'theme_tab_highlight_text_only',
                'theme_tab_selected_filled',
                'theme_tab_size_md',
                'theme_tabset_line_visible'
            ]
        ),
        (
            'Default',
            []
        ),
        (
            'Material',
            [
                'theme_accent_cyan',
                'theme_bar',
                'theme_bar_logo_atomized',
                'theme_bar_shadow_hidden',
                'theme_button_rounded',
                'theme_dirty_colored_always',
                'theme_icons_materialized',
                'theme_scrollbar_rounded',
                'theme_sidebar_highlight_selected_text_only',
                'theme_sidebar_highlight_text_only',
                'theme_sidebar_indent_top_level_disabled',
                'theme_size_md',
                'theme_tab_highlight_text_only',
                'theme_tab_selected_transparent',
                'theme_tab_selected_underlined',
                'theme_tab_size_xxl',
                'theme_unified'
            ]
        ),
        (
            'Numix',
            [
                'theme_accent_numix',
                'theme_autocomplete_item_selected_colored',
                'theme_dropdown_atomized',
                'theme_find_panel_materialized',
                'theme_grid_border_size_xs',
                'theme_popup_border_visible',
                'theme_quick_panel_border_visible',
                'theme_quick_panel_item_selected_colored',
                'theme_scrollbar_colored',
                'theme_scrollbar_line',
                'theme_sidebar_disclosure',
                'theme_tab_selected_transparent',
                'theme_tab_selected_underlined',
                'theme_tab_size_lg',
                'theme_unified'
            ]
        ),
        (
            'Predawn',
            [
                'theme_accent_tangerine',
                'theme_autocomplete_item_selected_colored',
                'theme_bar_margin_top_sm',
                'theme_dirty_materialized',
                'theme_dropdown_atomized',
                'theme_find_panel_size_xl',
                'theme_icon_button_highlighted',
                'theme_panel_switcher_atomized',
                'theme_quick_panel_item_selected_colored',
                'theme_scrollbar_colored',
                'theme_scrollbar_line',
                'theme_sidebar_close_always_visible',
                'theme_sidebar_folder_atomized',
                'theme_sidebar_folder_mono',
                'theme_statusbar_size_md',
                'theme_tab_close_always_visible',
                'theme_tab_selected_overlined',
                'theme_tab_size_md'
            ]
        )
    ]
)


def get_options(prefs):
    opts = []
    get_opt = prefs.get
    append_opt = opts.append

    for opt in OPTIONS:
        if get_opt(opt) is True:
            append_opt(opt)

    erase_options(prefs)

    return opts


def set_options(prefs, opts):
    set_opt = prefs.set

    for opt in opts:
        set_opt(opt, True)


def erase_options(prefs):
    erase_opt = prefs.erase

    for opt in OPTIONS:
        erase_opt(opt)


def disable_preset(prefs, opts):
    erase_opt = prefs.erase

    for opt in opts:
        erase_opt(opt)


def revert_options(prefs, opts):
    erase_options(prefs)
    set_options(prefs, opts)


def preview_preset(prefs, opts):
    set_options(prefs, opts)


def activate_preset(prefs, opts):
    commit()


def commit():
    return sublime.save_settings(PREFERENCES)


class BoxyPresetsCommand(sublime_plugin.WindowCommand):

    def display_list(self, presets):
        self.presets = presets
        self.prefs = sublime.load_settings(PREFERENCES)
        self.initial_options = get_options(self.prefs)
        self.previous_index = -1

        quick_list = [preset for preset in self.presets]
        self.quick_list = quick_list

        self.window.show_quick_panel(quick_list, self.on_done,
                                     on_highlight=self.on_highlighted)

    def on_highlighted(self, index):
        if self.previous_index != -1:
            sublime.set_timeout_async(disable_preset(
                self.prefs, self._quick_list_to_preset(self.previous_index)
            ), 0)

        sublime.set_timeout_async(preview_preset(
            self.prefs, self._quick_list_to_preset(index)
        ), 0)
        self.previous_index = index

    def on_done(self, index):
        if index is NO_SELECTION:
            revert_options(self.prefs, self.initial_options)
            return

        preset = self._quick_list_to_preset(index)
        activate_preset(self.prefs, preset)

    def _quick_list_to_preset(self, index):
        return self.presets[self.quick_list[index]]

    def run(self):
        self.display_list(PRESETS)
