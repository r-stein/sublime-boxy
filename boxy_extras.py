# -*- coding: utf-8 -*-

"""
Boxy Theme Extras
"""

import sublime
import sublime_plugin
import functools

NO_SELECTION = -1
PREFERENCES = 'Preferences.sublime-settings'
THEMES = [
	'Boxy Yesterday',
	'Boxy Tomorrow',
	'Boxy Ocean',
	'Boxy Monokai'
]

# Fix SublimeLinter Gutter Theme
# Remove after 3.4.0 will be released

def fix_linter_gutter_theme():
	settings = sublime.load_settings('SublimeLinter.sublime-settings')
	items = settings.get('user', False)

	if items != False:
		theme = items.get('gutter_theme')
		if theme == 'Packages/Boxy Theme/linter/Boxy.gutter-theme' or theme == 'Packages/Boxy Theme Addon - Linter Theme/Boxy.gutter-theme':
			items['gutter_theme'] = 'Packages/Boxy Theme/extras/SublimeLinter/Boxy.gutter-theme'
			settings.set('user', items)

def plugin_loaded():
	fix_linter_gutter_theme()

