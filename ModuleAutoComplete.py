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
		folders = sublime.active_window().folders();
		# print (folders[0].lower().endswith('sites'))
		if folders[0].lower().endswith('sites'):
			folders = get_immediate_subdirectories(self,folders[0])
		for x in folders:
			fullPath = x+self.MODULES_ROOT;
			for dir in os.listdir(fullPath):
				if '.' not in dir:
					for fileName in os.listdir(fullPath+'\\'+dir):
						mPath = dir+'/'+os.path.splitext(fileName)[0];
						if '.' not in mPath:
							modulesList.append([mPath,mPath]);
		return modulesList;
def get_immediate_subdirectories(self, a_dir):
    return [a_dir+'\\'+name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]
	
		