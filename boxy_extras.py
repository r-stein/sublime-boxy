# -*- coding: utf-8 -*-

"""
Boxy Theme Extras
"""

import sublime
import sublime_plugin
import functools
from collections import OrderedDict

NO_SELECTION = -1

SUBLIME_LINTER = 'SublimeLinter'
PLAIN_TASKS = 'PlainTasks'

EXTRAS = OrderedDict(
	[
		(
			'SublimeLinter',
			{
				'name': 'Sublime Linter',
				'settings': 'SublimeLinter.sublime-settings',
				'desc': 'Activate gutter theme',
				'revert': 'Revert gutter theme to the Default',
				'boxy': 'Packages/Boxy Theme/extras/SublimeLinter/Boxy.gutter-theme',
				'default': 'Packages/SublimeLinter/gutter-themes/Default/Default.gutter-theme'
			}
		),
		(
			'PlainTasks',
			{
				'name': 'Plain Tasks',
				'settings': 'PlainTasks.sublime-settings',
				'desc': 'Choose color scheme'
			}
		)
	]
)

SCHEMES = [
	'Boxy Yesterday',
	'Boxy Tomorrow',
	'Boxy Ocean',
	'Boxy Monokai'
]

def get_settings(pkg):
	return sublime.load_settings(EXTRAS[pkg].get('settings'))

def save_settings(pkg):
	return sublime.save_settings(EXTRAS[pkg].get('settings'))

def get_theme(pkg):
	settings = get_settings(pkg)

	if pkg is SUBLIME_LINTER:
		items = settings.get('user', False)
		if items != False:
			return items.get('gutter_theme')

def set_theme(pkg, path=''):
	settings = get_settings(pkg)

	if pkg is SUBLIME_LINTER:
		items = settings.get('user', False)
		if items != False:
			if path == '':
				items['gutter_theme'] = EXTRAS[pkg].get('boxy')
			else:
				items['gutter_theme'] = path
			settings.set('user', items)

class BoxyExtrasCommand(sublime_plugin.WindowCommand):

	def display_list(self, extras):
		self.extras = extras
		self.quick_list = []

		name = ''
		desc = ''

		for extra in self.extras:
			name = self.extras[extra].get('name')
			desc = self.extras[extra].get('desc')
			if extra is SUBLIME_LINTER:
				if get_theme(SUBLIME_LINTER) == self.extras[SUBLIME_LINTER].get('boxy'):
					desc = self.extras[SUBLIME_LINTER].get('revert')
			self.quick_list.append([name, desc])

		self.window.show_quick_panel(self.quick_list, self.on_done)

	def on_done(self, index):
		if index is NO_SELECTION:
			return

		if index is 0:
			current = get_theme(SUBLIME_LINTER)
			boxy = self.extras[SUBLIME_LINTER].get('boxy')
			default = self.extras[SUBLIME_LINTER].get('default')

			if current == boxy:
				set_theme(SUBLIME_LINTER, default)
			else:
				set_theme(SUBLIME_LINTER)

			save_settings(SUBLIME_LINTER)

	def run(self):
		self.display_list(EXTRAS)

# Fix SublimeLinter Gutter Theme
# TODO: Remove it when 4.0.0 will be released

def fix_linter_gutter_theme():
	theme = get_theme(SUBLIME_LINTER)

	if theme == 'Packages/Boxy Theme/linter/Boxy.gutter-theme' or theme == 'Packages/Boxy Theme Addon - Linter Theme/Boxy.gutter-theme':
		set_theme(SUBLIME_LINTER)
		save_settings(SUBLIME_LINTER)

def plugin_loaded():
	fix_linter_gutter_theme()
