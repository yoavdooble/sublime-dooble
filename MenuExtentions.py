import sublime, sublime_plugin
import re
import os
import ntpath
#TODO: concentrate filepath in same class
#TODO: why check ftp permissions fall sometimes
class DoobleIO():
	@staticmethod
	def getConfigPath(files):
		filePath = files[0].lower()
		filename, file_extension = os.path.splitext(filePath)
		#chaches the path to include the config extenstion and folder
		filePath = filename+ '.config'
		if 'content' in filePath:
			filePath = filePath.replace('content','Config\Content')
		elif 'admin' in filePath:
			filePath = filePath.replace('admin','Config\Admin')

		return filePath

	@staticmethod
	def getItemPath(files):
		filePath = files[0]
		filename, file_extension = os.path.splitext(filePath)

		#change file path
		# print("file name: " + filename)
		# print("file extension: " + file_extension)
		# if '.config' in file_extension:
		# 	config_file = filename.lower().replace("\\config", '')
		# 	print("config file: " + config_file)
		# 	# now we check what extension we need for the file
		# 	filePath = DoobleIO.get_html_extension(config_file)
		if filename.lower().endswith('master'):
			if(filename.endswith('Master')):
				filePath = filename.replace('Master','Item') + file_extension
			else:
				filePath = filename.lower().replace('master','Item') + file_extension
		else:
			filePath = filename+ '.Item' + file_extension

		return filePath

	@staticmethod
	def getMasterPath(files):
		filePath = files[0]
		filename, file_extension = os.path.splitext(filePath)

		#change file path
		print("file name: " + filename)
		print("file extension: " + file_extension)
		if '.config' in file_extension:
			config_file = filename.lower().replace("\\config", '')
			print("config file: " + config_file)
			# now we check what extension we need for the file
			filePath = DoobleIO.get_html_extension(config_file)

		elif filename.lower().endswith('.item'):
			filePath = filename.lower().replace('.item','') + file_extension
		else:
			if(filename.endswith('Item')):
				filePath = filename.replace('Item','Master') + file_extension
			else:
				filePath = filename.lower().replace('item','master') + file_extension

		return filePath

	@staticmethod
	def getBabelPath(files):
		filePath = files[0] + '.js'

		return filePath
		
	
	@staticmethod
	def get_master_path(file_name, result):
		left_path, file_name = DoobleIO.cut_path(file_name)
		if DoobleIO.is_ui_controls(result):
			const_path = "master"
			result = DoobleIO.ui_format(result)
		elif DoobleIO.is_admin(file_name):
			const_path = "master\\admin\\"
		else:
			const_path = "master\\content\\modules\\"

		lis = file_name.split("\\")
		root = ""
		for i in lis:
			if 'sites' in root:
				break
			root += i + '\\'
		root += const_path + result
		# print(left_path + root)
		return left_path + root

	@staticmethod
	def get_site_path(file_name, result):
		left_path, file_name = DoobleIO.cut_path(file_name)
		if DoobleIO.is_ui_controls(result):
			const_path = ""
			result = DoobleIO.ui_format(result)
		elif DoobleIO.is_admin(file_name):
			const_path = "admin\\"
		else:
			const_path = "content\\modules\\"

		lis = file_name.split("\\")
		root = ""
		for i in range(len(lis)):
			if 'sites' in root:
				# add the name of site
				root += lis[i] + '\\' 
				break
			if 'site' in root:
				break
			root += lis[i] + '\\'
		root += const_path + result
		# print(left_path + root)
		return left_path + root


	@staticmethod
	def is_admin(file_name):
		lis = file_name.split("\\")
		if 'admin' in file_name:
			return True
		return False

	@staticmethod
	def is_ui_controls(result):
		regex = r"ui/\w+"
		# return true for match, else return false
		return re.match(regex, result)

	@staticmethod
	def ui_format(result):
		# e.g: from ui/submit we get only the 'submit'
		return 'uicontrols\\' + result.split('/')[1] 

	@staticmethod
	def is_master(file_name):
		lis = file_name.split("\\")
		root = ""
		for i in range(len(lis)):
			if 'sites' in root:
				if lis[i] == 'master':
					return True
			root += lis[i] + '\\'
		return False

	@staticmethod
	def cut_path(file_name):
		lis = []
		left_path = ""
		right_path = ""
		if 'sites' in file_name:
			lis = file_name.split('sites')
			left_path = lis[0]
			print('sites' + lis[1])
			right_path = 'sites' + lis[1]
		elif 'site' in file_name:
			lis = file_name.split('site')
			left_path = lis[0]
			right_path = 'site' + lis[1]

		return(left_path, right_path)

	@staticmethod
	def is_folder(path):
		if os.path.isdir(path):
			return True
		return False

	@staticmethod
	def is_config_file(path):
		return '.config' in path

	@staticmethod
	def is_item_file(path):
		return 'item.' in path
	
	@staticmethod
	def get_html_extension(file_name):
		if os.path.isfile(file_name + ".html"):
			filePath = file_name + ".html"
		elif os.path.isfile(file_name + ".htm"):
			filePath = file_name + ".htm"
		else:
			filePath = ""
		return filePath
		
	@staticmethod
	def get_duplicate_file_path(file_path):
		file_name, file_extension = os.path.splitext(file_path)
		# add disabled to the destination file
		return file_name + '.disabled' + file_extension

		# add extension to the destination file
		# return file_path + '.disabled'

	@staticmethod
	def get_strudel_file_path(file_path):
		file_name, file_extension = os.path.splitext(file_path)
		base_name = os.path.basename(file_name)
		
		return file_path.replace(base_name, '@' + base_name)
		
	@staticmethod
	def is_duplicate_file(path):
		return '.disabled' in path

	@staticmethod
	def is_strudel_file(path):
		return '@' in path


class AddItemCommand(sublime_plugin.WindowCommand):
	def run(self, files=[], paths=[]):
		# in case we dont have files, get the open files from the window
		if not files:
			files.append(sublime.active_window().active_view().file_name())
		# get file path in item format
		filePath = DoobleIO.getItemPath(files)
		# open a new file. if exists, does nothing.
		open(filePath, 'a')
		# goes to new file
		sublime.active_window().open_file(filePath)

	def is_visible(self, files=[], paths=[]):
		return self.add_item_check(files, paths)
		# # check if it's folder
		# if len(paths) == 1:
		# 	# get single folder for checking
		# 	path = paths[0]
		# 	if DoobleIO.is_folder(path):
		# 		return False

		# # in case we have multiple files selection
		# if len(files) > 1:
		# 	return False

		# # in case we dont have files, get the open files from the window 
		# if not files:
		# 	files.append(sublime.active_window().active_view().file_name())

		# # get single file for checking
		# file_path = files[0].lower()

		# # check item\config case
		# if DoobleIO.is_item_file(file_path) or \
		#    DoobleIO.is_config_file(file_path):
		# 	return False

		# # get file path in item format
		# filePath = DoobleIO.getItemPath(files)
		# # check if the file Path is existing file
		# if os.path.isfile(filePath):
		# 	return False
		# return True

	def is_enabled(self, files=[], paths=[]):
		return self.add_item_check(files, paths)

	def add_item_check(self, files=[], paths=[]):
		# check if it's folder
		if len(paths) == 1:
			# get single folder for checking
			path = paths[0]
			if DoobleIO.is_folder(path):
				return False

		# in case we have multiple files selection
		if len(files) > 1:
			return False

		# in case we dont have files, get the open files from the window 
		if not files:
			files.append(sublime.active_window().active_view().file_name())

		# get single file for checking
		file_path = files[0].lower()

		# check item\config case
		if DoobleIO.is_item_file(file_path) or \
		   DoobleIO.is_config_file(file_path):
			return False

		# get file path in item format
		filePath = DoobleIO.getItemPath(files)
		# check if the file Path is existing file
		if os.path.isfile(filePath):
			return False
		return True

	
class GoToItemCommand(sublime_plugin.WindowCommand):
	def run(self, files):
		# in case we dont have files, get the open files from the window 
		if not files:
			files.append(sublime.active_window().active_view().file_name())

		# get single file for checking
		file_path = files[0].lower()
		# check if it's not item file
		if not DoobleIO.is_item_file(file_path):
			# get file path in item format
			filePath = DoobleIO.getItemPath(files)
			# goes to new file
			sublime.active_window().open_file(filePath)

	def is_visible(self, files):
		return self.go_to_item_check(files)
		# # in case we have multiple files selection
		# if len(files) > 1:
		# 	return False

		# # in case we dont have files, get the open files from the window 
		# if not files:
		# 	files.append(sublime.active_window().active_view().file_name())

		# # get single file for checking
		# file_path = files[0].lower()

		# # check if it's item file
		# if DoobleIO.is_item_file(file_path):
		# 	return False

		# # check if it's config file
		# if DoobleIO.is_config_file(file_path):
		# 	return True

		# # get file path in item format
		# filePath = DoobleIO.getItemPath(files)
		# # check if the file Path is existing file
		# if not os.path.isfile(filePath):
		# 	return False
		# return True

	def is_enabled(self, files):
		return self.go_to_item_check(files)

	def go_to_item_check(self, files):
		# in case we have multiple files selection
		if len(files) > 1:
			return False

		# in case we dont have files, get the open files from the window 
		if not files:
			files.append(sublime.active_window().active_view().file_name())

		# get single file for checking
		file_path = files[0].lower()

		# check if it's item file
		if DoobleIO.is_item_file(file_path):
			return False

		# check if it's config file
		if DoobleIO.is_config_file(file_path):
			return True

		# get file path in item format
		filePath = DoobleIO.getItemPath(files)
		# check if the file Path is existing file
		if not os.path.isfile(filePath):
			return False
		return True

class GoToMasterCommand(sublime_plugin.WindowCommand):
	def run(self, files):
		# in case we dont have files, get the open files from the window 
		if not files:
			files.append(sublime.active_window().active_view().file_name())
		# get file path in master format
		filePath = DoobleIO.getMasterPath(files)

		# goes to new file
		sublime.active_window().open_file(filePath)

	def is_visible(self, files):
		return self.go_to_master_check(files)
		# # in case we have multiple files selection
		# if len(files) > 1:
		# 	return False

		# # in case we dont have files, get the open files from the window 
		# if not files:
		# 	files.append(sublime.active_window().active_view().file_name())

		# # get single file for checking
		# file_path = files[0].lower()

		# # filePath = DoobleIO.getItemPath(files)
		# # check if the file Path is existing file
		# if not os.path.isfile(file_path):
		# 	return False

		# # check item\config case
		# if DoobleIO.is_item_file(file_path) or \
		#    DoobleIO.is_config_file(file_path):
		# 	return True
		# return False

	def is_enabled(self, files):
		return self.go_to_master_check(files)

	def go_to_master_check(self, files):
		# in case we have multiple files selection
		if len(files) > 1:
			return False

		# in case we dont have files, get the open files from the window 
		if not files:
			files.append(sublime.active_window().active_view().file_name())

		# get single file for checking
		file_path = files[0].lower()

		# filePath = DoobleIO.getItemPath(files)
		# check if the file Path is existing file
		if not os.path.isfile(file_path):
			return False

		# check item\config case
		if DoobleIO.is_item_file(file_path) or \
		   DoobleIO.is_config_file(file_path):
			return True
		return False


class AddConfigCommand(sublime_plugin.WindowCommand):
	def run(self, files=[], paths=[]):
		# In case it's a folder
		if len(paths) == 1:
			# get single folder for checking
			path = paths[0]
			if DoobleIO.is_folder(path):
				file_name = path + '\\$.config'
				# if os.path.isfile(file_name):
				# 	sublime.active_window().open_file(file_name)
				# else:
				# 	# if the file does not exist, create one.
				# 	open(file_name, 'a')
				# 	sublime.active_window().open_file(file_name)
				if not os.path.isfile(file_name):
					open(file_name, 'a')
					# goes to new file
					sublime.active_window().open_file(file_name)
				
			
		# in case we dont have files, get the open files from the window 
		if not files:
			files.append(sublime.active_window().active_view().file_name())

		# get file path in config format
		filePath = DoobleIO.getConfigPath(files)

		folder = os.path.dirname(filePath)
		if not os.path.exists(folder):
			try:
				os.makedirs(folder, 0o777,True)
				open(filePath, 'a')
				sublime.active_window().open_file(filePath)
			except OSError:
   				sublime.error_message('There\'s a problem with the file manager. the file may already exist or Expendrive should be restarted.')


	def is_visible(self, files=[], paths=[]):
		return self.add_config_check(files, paths)
		# # In case it's a folder
		# if len(paths) == 1:
		# 	# get single folder for checking
		# 	path = paths[0]
		# 	if DoobleIO.is_folder(path):
		# 		# check if the file Path is existing file
		# 		if os.path.isfile(path + '\\$.config'):
		# 			return False

		# # in case we have multiple files selection
		# if len(files) > 1:
		# 	return False

		# # in case we dont have files, get the open files from the window 
		# if not files:
		# 	files.append(sublime.active_window().active_view().file_name())

		# # get single file for checking
		# file_path = files[0].lower()
		
		# # check item\config case
		# if DoobleIO.is_item_file(file_path) or \
		#    DoobleIO.is_config_file(file_path):
		# 	return False

		# # get file path in config format
		# filePath = DoobleIO.getConfigPath(files)
		# # check if the file Path is existing file
		# if os.path.isfile(filePath):
		# 	return False
		# return True


	def is_enabled(self, files=[], paths=[]):
		return self.add_config_check(files, paths)

	def add_config_check(self, files=[], paths=[]):
		# In case it's a folder
		if len(paths) == 1:
			# get single folder for checking
			path = paths[0]
			if DoobleIO.is_folder(path):
				# check if the file Path is existing file
				if os.path.isfile(path + '\\$.config'):
					return False

		# in case we have multiple files selection
		if len(files) > 1:
			return False

		# in case we dont have files, get the open files from the window 
		if not files:
			files.append(sublime.active_window().active_view().file_name())

		# get single file for checking
		file_path = files[0].lower()
		
		# check item\config case
		if DoobleIO.is_item_file(file_path) or \
		   DoobleIO.is_config_file(file_path):
			return False

		# get file path in config format
		filePath = DoobleIO.getConfigPath(files)
		# check if the file Path is existing file
		if os.path.isfile(filePath):
			return False
		return True



class GoToConfigCommand(sublime_plugin.WindowCommand):
	def run(self, files=[], paths=[]):
		# print(paths)
		# print(files)
		# In case it's a folder
		if len(paths) == 1:
			# get single folder for checking
			path = paths[0]
			if DoobleIO.is_folder(path):
				file_name = path + '\\$.config'
				# check if the file Path is existing file
				if os.path.isfile(file_name):
					sublime.active_window().open_file(file_name)

		# in case we dont have files, get the open files from the window 
		if not files:
			files.append(sublime.active_window().active_view().file_name())

		# get file path in config format
		filePath = DoobleIO.getConfigPath(files)
		sublime.active_window().open_file(filePath)


	def is_visible(self, files=[], paths=[]):
		return self.go_to_config_check(files, paths)
		# # In case it's a folder
		# if len(paths) == 1:
		# 	# get single folder for checking
		# 	path = paths[0]
		# 	if DoobleIO.is_folder(path):
		# 		# check if the file Path is existing file
		# 		if os.path.isfile(path + '\\$.config'):
		# 			return True

		# # in case we have multiple files selection
		# if len(files) > 1:
		# 	return False

		# # in case we dont have files, get the open files from the window 
		# if not files:
		# 	files.append(sublime.active_window().active_view().file_name())

		# # get single file for checking
		# file_path = files[0].lower()
		# # check if it's config file
		# if DoobleIO.is_config_file(file_path):
		# 	return False		
		
		# # get file path in config format
		# filePath = DoobleIO.getConfigPath(files)
		# # check if the file Path is existing file
		# if not os.path.isfile(filePath):
		# 	return False
		# return True

	def is_enabled(self, files=[], paths=[]):
		return self.go_to_config_check(files, paths)
		# # in case we dont have files, get the open files from the window 
		# if not files:
		# 	files.append(sublime.active_window().active_view().file_name())

		# # get single file for checking
		# file_path = files[0].lower()

		# if '$.config' in file_path:
		# 	print('ERROR MESSAGE: can\'t go to config file if the source file is \'$.config\'')
		# 	return False
		# return True

	def go_to_config_check(self, files=[], paths=[]):
		# In case it's a folder
		if len(paths) == 1:
			# get single folder for checking
			path = paths[0]
			if DoobleIO.is_folder(path):
				# check if the file Path is existing file
				if os.path.isfile(path + '\\$.config'):
					return True

		# in case we have multiple files selection
		if len(files) > 1:
			return False

		# in case we dont have files, get the open files from the window 
		if not files:
			files.append(sublime.active_window().active_view().file_name())

		# get single file for checking
		file_path = files[0].lower()
		# check if it's config file
		if DoobleIO.is_config_file(file_path):
			return False		
		
		# get file path in config format
		filePath = DoobleIO.getConfigPath(files)
		# check if the file Path is existing file
		if not os.path.isfile(filePath):
			return False
		return True

class AddDuplicateFileCommand(sublime_plugin.WindowCommand):
	def run(self, files=[], paths=[]):
		# in case we dont have files, get the open files from the window 
		if not files:
			files.append(sublime.active_window().active_view().file_name())

		# get single file for checking
		file_path = files[0]
		print("file path: " + file_path)

		new_file_path = DoobleIO.get_duplicate_file_path(file_path)
		print("new file path: " + new_file_path)

		# only if not exist, open new file
		open(new_file_path, 'a')
		# copy file src to new dst
		shutil.copyfile(file_path, new_file_path)
		# show status bar message
		sublime.status_message("Duplicate file was created Successfully")
		# open the file in view
		self.window.open_file(new_file_path)

	def is_visible(self, files=[], paths=[]):
		return self.add_duplicate_check(files, paths)

	def is_enabled(self, files=[], paths=[]):
		return self.add_duplicate_check(files, paths)

	def add_duplicate_check(self, files=[], paths=[]):
		# in case we have multiple folder selection
		if len(paths) > 1:
			return False

		# In case it's a folder
		if len(paths) == 1:
			# get single folder for checking
			path = paths[0]
			if DoobleIO.is_folder(path):
				return False

		# in case we dont have files, get the open files from the window 
		if not files:
			files.append(sublime.active_window().active_view().file_name())

		# in case we have multiple files selection
		if len(files) > 1:
			return False

		if len(files) == 1:
			path = files[0]
			has_duplicate_file = DoobleIO.get_duplicate_file_path(path)
			has_strudel_file = DoobleIO.get_strudel_file_path(path)
			if DoobleIO.is_duplicate_file(path) or \
			   os.path.isfile(has_duplicate_file) or \
			   DoobleIO.is_strudel_file(path) or \
			   os.path.isfile(has_strudel_file):
				return False

		return True
	
class CheckScopeCommand(sublime_plugin.WindowCommand):
	def run(self):
		# get current view
		view = sublime.active_window().active_view()
		# get the current cursor point
		sel = view.sel()[0].begin()
		# get the line with current cursor
		get_line = view.line(sel)
		print("Line: " + view.substr(get_line))
		print("scope: " + view.scope_name(get_line.begin()))


class GoToModuleCommand(sublime_plugin.WindowCommand):

	# [[Module/template]] or [[Module/template attr=""]]
	REGEX = r".*\[\[(\w+[\\|/]\w+).*((.|\n)*)\]\].*"

	def run(self):
		# start the program
		result = self.start()

		if result:
			sublime.active_window().run_command("show_overlay", {"overlay": "goto", "show_files": True, "text":result})


		# global list_of_files
		# list_of_files = []
		# # note: if string or array empty the result return false
		# # if the result is string its single file
		# # else, its an array
		# if result:
		# 	if isinstance(result, str):
		# 		# open the file in new window
		# 		self.window.open_file(result) 
		# 	else:
		# 		list_of_files = result
		# 		panel_list = self.quick_panel_list(list_of_files)
		# 		# open the quick panel
		# 		self.window.show_quick_panel(panel_list, self.on_done, sublime.MONOSPACE_FONT)
		# else:
		# 	sublime.message_dialog("File not found")

			
	# def on_done(self, result):
	# 	self.window.open_file(list_of_files[result])	


	# def is_visible(self):
	# 	# start the program
	# 	result = self.start()
	# 	if result:
	# 		return True
	# 	sublime.error_message("File not found")
	# 	return False
		

	# def is_file(self, path):
	# 	fixed_path = ""

	# 	if os.path.isfile(path + ".html"):
	# 		fixed_path += path + ".html"
	# 	elif os.path.isfile(path + ".htm"):
	# 		fixed_path += path + ".htm"
	# 	elif os.path.isfile(path + ".hpp"):
	# 		fixed_path += path + ".hpp"
		
	# 	return fixed_path

	
	def start(self):
		# get user selection
		sel = self.user_selection()
		# do match with user selection and return the result
		search_result = self.match_selection(sel)
		# get current path of file
		file_name = sublime.active_window().active_view().file_name().lower()
		
		print("result: " + search_result)
		# print(len(search_result))
		if search_result:
			if DoobleIO.is_ui_controls(search_result):
				search_result = 'uicontrols\\' + search_result.split('/')[1]
			elif 'admin' in file_name:
				search_result = 'admin\\' + search_result
			elif 'content' in file_name:
				search_result = 'modules\\' + search_result

			search_result = search_result.replace('/', '\\')
		
		return search_result 



		# # check if the current file is master
		# if DoobleIO.is_master(file_name):
		# 	files_list = self.get_files_list(search_result)
		# 	if len(files_list) > 0:
		# 		return files_list

		# # first try search in site folder
		# result = self.is_site_path(file_name, search_result)
		# # if the file site exist
		# if result:
		# 	return result

		# # if its not in site folder try search in master folder
		# result = self.is_master_path(file_name, search_result)

		# if result:
		# 	return result

		# # in case the file not exist at all
		# return ""

	def user_selection(self):
		# get current view
		view = sublime.active_window().active_view()
		# get the current cursor point
		sel = view.sel()[0].begin()
		# get the line with current cursor
		get_line = view.line(sel)
		print("the line: " + view.substr(get_line).strip())
		# get the start line region
		# start_position = get_line.a
		# find the regex from the current cursor until you get the whole exp
		# sel = view.find(self.REGEX, start_position)
		# get the selection in string
		# sel = view.substr(sel)
		# return sel

		return view.substr(get_line).strip()

	def match_selection(self, sel):
		print("sel: " + sel)
		try:
			# do match with the selected exp
			search_result = re.match(self.REGEX, sel).group(1)
		except:
			# in case the sel = None
			print("there is no match")
			search_result = ""

		return search_result.lower()

	# def is_site_path(self, file_name, result):
	# 	# get the site fixed path
	# 	site_fixed_path = DoobleIO.get_site_path(file_name, result)
	# 	fixed_path = self.is_file(site_fixed_path)

	# 	return fixed_path

	# def is_master_path(self, file_name, result):
	# 	# get the master fixed path
	# 	master_fixed_path = DoobleIO.get_master_path(file_name, result)
	# 	fixed_path = self.is_file(master_fixed_path)

	# 	return fixed_path

	# def quick_panel_list(self, list_of_files):
	# 	view_list = []
	# 	for item in list_of_files:
	# 		# this split create two parts: one with the root path
	# 		# and the other with name of site and so on
	# 	  if 'sites' in item.lower():
	# 	  	file_format = item.lower().split('sites\\')
	# 	  	# get the name of site and module name
	# 	  	view_list.append(file_format[1])
	# 	  elif 'site' in item.lower():
	# 	  	file_format = item.lower().split('site\\')
	# 	  	# get the name of site and module name
	# 	  	view_list.append('site\\' + file_format[1])
	# 	  else:
	# 	  	view_list.append("This is NOT site")

	# 	return view_list

	# def get_files_list(self, search_result):
	# 	# in case the search_result pattern is [[ui/template]]
	# 	if DoobleIO.is_ui_controls(search_result):
	# 		search_result = DoobleIO.ui_format(search_result)
	# 	search_result = search_result.replace('/', '\\')
	# 	# get the open folders from the side bar
	# 	open_folders = self.get_open_folders() 
		 
	# 	files_list = []
	# 	for folder in open_folders:
	# 		# in case the search result is ui controls
	# 		result = self.is_file(folder + '\\' + search_result)
	# 		if result:
	# 			files_list.append(result)
	# 		# in case the file in admin folder
	# 		result = self.is_file(folder + '\\admin\\' + search_result)
	# 		if result:
	# 			files_list.append(result)
	# 		# in case the file in content folder
	# 		result = self.is_file(folder + '\\' + 'content\\modules\\' + search_result)
	# 		if result:
	# 			files_list.append(result)


	# 	return files_list
		
	# def sub_dir_path(self, a_dir):
	# 	return filter(os.path.isdir, [os.path.join(a_dir,f) for f in os.listdir(a_dir)])

	# def get_open_folders(self):
	# 	# get the opened folders from the side bar
	# 	folders = self.window.folders()
	# 	folder_list = []
	# 	for folder in folders:
	# 		if folder.lower().endswith('sites'):
	# 			folder_list += list(self.sub_dir_path(folder))
	# 		else:
	# 			folder_list.append(folder)

	# 	return folder_list


	



# class BabelIt(sublime_plugin.WindowCommand):

# 	def run(self, files):
# 		import subprocess
# 		try:
# 			newFile = subprocess.check_output("babel "+files[0],shell=True)

# 			# print(files[0])
# 			filePath = DoobleIO.getBabelPath(files)

# 			jsFile = open(filePath, 'w')
# 			jsFile.write(newFile.decode(encoding='UTF-8'))
# 			jsFile.close()
# 			sublime.active_window().open_file(filePath)
# 			print('TransCompiled Successfully.')
# 		except:
# 			print("babel "+files[0])
# 			sublime.error_message("There's something wrong with your code.")
# 		# sublime.active_window().open_file(filePath)

# 	def is_visible(self,files):
# 		if(".bbl" in files[0].lower()) : 
# 			return True
# 		else:
# 			return False

# class CheckFile():
# 	def run(files):
