import sublime, sublime_plugin

class ReplaceItCommand(sublime_plugin.TextCommand):
	def run(self, edit, find, replace, regex = False, ignore_case = False, only_next = False):
		flags = 0;
		if not regex:
			flags = flags | sublime.LITERAL
		if ignore_case:
			flags = flags | sublime.IGNORECASE

		if only_next:
			point = self.view.sel()[0]
			regions = [ self.view.find(find, point.begin(), flags) ]
		else:
			regions = self.view.find_all(find, flags)

		offset = 0
		length = len(replace)
		for region in regions:
			adjusted_region = sublime.Region( region.a + offset, region.b + offset)
			self.view.replace( edit, adjusted_region, replace)
			offset = offset - region.size() + length

	def is_visible():
		return False

	def description():
		"A version of find and replace that can be bound to a keyboard shortcut"