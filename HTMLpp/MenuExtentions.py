import sublime, sublime_plugin
import os

class AddItemCommand(sublime_plugin.WindowCommand):
	def run(self, files):
		# get file path
		filePath = files[0].lower()
		filename, file_extension = os.path.splitext(filePath)

		#change file path
		if filename.lower().endswith('master'):
			filePath = filename.lower().replace('master','item') + file_extension
		else:
			filePath = filename+ '.item' + file_extension

		#open a new file. if exists, does nothing.
		open(filePath, 'a')

		#goes to new file
		sublime.active_window().open_file(filePath)

	def is_visible(self,files):
		#che
		if(len(files) > 1):
			return False
		if("item" in files[0].lower()):
			return False

		filePath = files[0].lower()
		filename, file_extension = os.path.splitext(filePath)

		#change file path
		if filename.lower().endswith('master'):
			filePath = filename.lower().replace('master','item') + file_extension
		else:
			filePath = filename+ '.item' + file_extension

		if (os.path.isfile(filePath)):
			return False

		return True

class GoToItemCommand(sublime_plugin.WindowCommand):
	def run(self, files):
		# get file path
		filePath = files[0].lower()
		filename, file_extension = os.path.splitext(filePath)

		#change file path
		if filename.lower().endswith('master'):
			filePath = filename.lower().replace('master','item') + file_extension
		else:
			filePath = filename+ '.item' + file_extension

		#open a new file. if exists, does nothing.
		# open(filePath, 'a')

		#goes to new file
		sublime.active_window().open_file(filePath)

	def is_visible(self,files):
		if(len(files) > 1):
			return False
		if("item" in files[0].lower()):
			return False

		filePath = files[0].lower()
		filename, file_extension = os.path.splitext(filePath)

		#change file path
		if filename.lower().endswith('master'):
			filePath = filename.lower().replace('master','item') + file_extension
		else:
			filePath = filename+ '.item' + file_extension

		if (not os.path.isfile(filePath)):
			return False
		return True

class AddConfigCommand(sublime_plugin.WindowCommand):
	def run(self, files):
		#gets the file path
		filePath = files[0].lower()
		filename, file_extension = os.path.splitext(filePath)
		#chaches the path to include the config extenstion and folder
		filePath = filename+ '.config'
		if 'content' in filePath:
			filePath = filePath.replace('content','config\content')
		elif 'admin' in filePath:
			filePath = filePath.replace('content','config\\admin')

		folder = os.path.dirname(filePath)
		if not os.path.exists(folder):
			try:
				os.makedirs(folder)
			except OSError:
   				print('There\'s a problem with the file manager. the file may already exist or Expendrive should be restarted.')


		open(filePath, 'a')
		sublime.active_window().open_file(filePath)

	def is_visible(self,files):
		filePath = files[0].lower()
		filename, file_extension = os.path.splitext(filePath)

		#chaches the path to include the config extenstion and folder
		filePath = filename+ '.config'
		if 'content' in filePath:
			filePath = filePath.replace('content','config\content')
		elif 'admin' in filePath:
			filePath = filePath.replace('content','config\\admin')
		
		if(len(files) > 1):
			return False
		if("item" in files[0].lower()) or ("config" in files[0].lower()) :
			return False
		if (os.path.isfile(filePath)):
			return False
		return True

class GoToConfigCommand(sublime_plugin.WindowCommand):
	def run(self, files):

		filePath = files[0].lower()
		filename, file_extension = os.path.splitext(filePath)

		#chaches the path to include the config extenstion and folder
		filePath = filename+ '.config'
		if 'content' in filePath:
			filePath = filePath.replace('content','config\content')
		elif 'admin' in filePath:
			filePath = filePath.replace('content','config\\admin')

		sublime.active_window().open_file(filePath)


	def is_visible(self,files):
		filePath = files[0].lower()
		filename, file_extension = os.path.splitext(filePath)

		#chaches the path to include the config extenstion and folder
		filePath = filename+ '.config'
		if 'content' in filePath:
			filePath = filePath.replace('content','config\content')
		elif 'admin' in filePath:
			filePath = filePath.replace('content','config\\admin')
		

		if(len(files) > 1):
			return False
		if("item" in files[0].lower()) or ("config" in files[0].lower()) :
			return False
		if (not os.path.isfile(filePath)):
			return False

		return True

# class CheckFile():
# 	def run(files):

		
