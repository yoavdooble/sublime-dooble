import sublime, sublime_plugin, os 

class ModuleAutoCompleteCommand(sublime_plugin.EventListener):
	SCOPE_NAME = 'text.html.pp.module';
	MODULES_ROOT = '\Content\Modules';

	def on_query_completions(self, view, prefix, locations):
		if self.SCOPE_NAME in view.scope_name(locations[0]):
			autocomplete_list = self.getDirs();
			return autocomplete_list;

	def getDirs(self):
		modulesList = [];
		for x in sublime.active_window().folders():
			fullPath = x+self.MODULES_ROOT;
			for dir in os.listdir(fullPath):
				if '.' not in dir:
					for fileName in os.listdir(fullPath+'\\'+dir):
						mPath = dir+'/'+os.path.splitext(fileName)[0];
						if '.' not in mPath:
							modulesList.append([mPath,mPath]);
		return modulesList;

	def on_new_async(self, view_id):
		print(view_id);
	
		