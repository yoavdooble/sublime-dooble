import sublime, sublime_plugin
import os
#TODO: concentrate filepath in same class
#TODO: why check ftp permissions fall sometimes
class doobleIO():
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
		if filename.lower().endswith('master'):
			if(filename.endswith('Master')):
				filePath = filename.replace('Master','Item') + file_extension
			else:
				filePath = filename.lower().replace('master','Item') + file_extension
		else:
			filePath = filename+ '.Item' + file_extension

		return filePath

	@staticmethod
	def getBabelPath(files):
		filePath = files[0] + '.js'

		return filePath

class AddItemCommand(sublime_plugin.WindowCommand):
	def run(self, files):
		# get file path
		filePath = doobleIO.getItemPath(files)
		#open a new file. if exists, does nothing.
		open(filePath, 'a')

		#goes to new file
		sublime.active_window().open_file(filePath)

	def is_visible(self,files):
		
		if(len(files) > 1):
			return False
		if("item." in files[0].lower()):
			return False

		filePath = doobleIO.getItemPath(files)

		if (os.path.isfile(filePath)):
			return False

		return True

class GoToItemCommand(sublime_plugin.WindowCommand):
	def run(self, files):
		# get file path
		filePath = doobleIO.getItemPath(files)

		#goes to new file
		sublime.active_window().open_file(filePath)

	def is_visible(self,files):
		if(len(files) > 1):
			return False
		if("item." in files[0].lower()):
			return False

		filePath = doobleIO.getItemPath(files)

		if (not os.path.isfile(filePath)):
			return False
		return True

class AddConfigCommand(sublime_plugin.WindowCommand):
	def run(self, files):
		#gets the file path
		filePath = doobleIO.getConfigPath(files)

		folder = os.path.dirname(filePath)
		if not os.path.exists(folder):
			try:
				os.makedirs(folder, 0o777,True)
				open(filePath, 'a')
				sublime.active_window().open_file(filePath)
			except OSError:
   				sublime.error_message('There\'s a problem with the file manager. the file may already exist or Expendrive should be restarted.')


	def is_visible(self,files):
		
		if(len(files) > 1):
			return False
		if("config" in files[0].lower()) :
			return False

		filePath = doobleIO.getConfigPath(files)
		if (os.path.isfile(filePath)):
			return False
		return True

class GoToConfigCommand(sublime_plugin.WindowCommand):
	def run(self, files):

		filePath = doobleIO.getConfigPath(files)
		sublime.active_window().open_file(filePath)


	def is_visible(self,files):
		
		if(len(files) > 1):
			return False

		if("config" in files[0].lower()) :
			return False		
		
		filePath = doobleIO.getConfigPath(files)
		if (not os.path.isfile(filePath)):
			return False

		return True

class BabelIt(sublime_plugin.WindowCommand):

	def run(self, files):
		import subprocess
		try:
			newFile = subprocess.check_output("babel "+files[0],shell=True)

			# print(files[0])
			filePath = doobleIO.getBabelPath(files)

			jsFile = open(filePath, 'w')
			jsFile.write(newFile.decode(encoding='UTF-8'))
			jsFile.close()
			sublime.active_window().open_file(filePath)
			print('TransCompiled Successfully.')
		except:
			print("babel "+files[0])
			sublime.error_message("There's something wrong with your code.")
		# sublime.active_window().open_file(filePath)

	def is_visible(self,files):
		if(".bbl" in files[0].lower()) : 
			return True
		else:
			return False

# class CheckFile():
# 	def run(files):

		
