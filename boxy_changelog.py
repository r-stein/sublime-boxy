# -*- coding: utf-8 -*-

"""
Boxy Theme Changelog
"""

import sublime
import sublime_plugin

STYLES = '''
.mdpopups {
	{{'.background'|css}}
}

.boxy-changelog a {
	text-decoration: none;
}

.boxy-changelog h1,
.boxy-changelog h2,
.boxy-changelog h3,
.boxy-changelog h4,
.boxy-changelog h5,
.boxy-changelog h6 {
	{{'.string'|css('color')}}
}
'''

class BoxyChangelogCommand(sublime_plugin.WindowCommand):

	def run(self):
		import mdpopups
		text = sublime.load_resource('Packages/Boxy Theme/CHANGELOG.md')
		view = self.window.new_file()
		view.set_name('Boxy Theme Changelog')
		view.settings().set('gutter', False)
		html = '<div class="boxy-changelog">%s</div>' % mdpopups.md2html(view, text)
		mdpopups.add_phantom(view, 'changelog', sublime.Region(0), html, sublime.LAYOUT_INLINE, css=STYLES)
		view.set_read_only(True)
		view.set_scratch(True)

	def is_enabled(self):
		try:
			import mdpopups
		except Exception:
			return False

		return (mdpopups.version() >= (1, 7, 3)) and (int(sublime.version()) >= 3118)

	is_visible = is_enabled
