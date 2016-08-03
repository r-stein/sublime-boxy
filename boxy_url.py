# -*- coding: utf-8 -*-

"""
Boxy Theme URLs
"""

import sublime
import sublime_plugin
import webbrowser

class BoxyChangelogCommand(sublime_plugin.WindowCommand):
	def run(self):
		webbrowser.open_new_tab('https://github.com/oivva/boxy/blob/master/CHANGELOG.md')

class BoxyDocsCommand(sublime_plugin.WindowCommand):
	def run(self):
		webbrowser.open_new_tab('https://github.com/oivva/boxy/wiki')

class BoxyDonateCommand(sublime_plugin.WindowCommand):
	def run(self):
		webbrowser.open_new_tab('https://github.com/oivva/boxy#share-the-love')

class BoxyForumCommand(sublime_plugin.WindowCommand):
	def run(self):
		webbrowser.open_new_tab('https://forum.sublimetext.com/t/boxy-the-most-hackable-theme-for-sublime-text-3/20564')

class BoxyIssuesCommand(sublime_plugin.WindowCommand):
	def run(self):
		webbrowser.open_new_tab('https://github.com/oivva/boxy/issues')

class BoxyPackageControlCommand(sublime_plugin.WindowCommand):
	def run(self):
		webbrowser.open_new_tab('https://packagecontrol.io/packages/Boxy%20Theme')

class BoxyRepoCommand(sublime_plugin.WindowCommand):
	def run(self):
		webbrowser.open_new_tab('https://github.com/oivva/boxy')

