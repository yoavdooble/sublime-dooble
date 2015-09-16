# sublime-dooble
dooble extension

author - sahar zehavi

To add the Dooble Package to  Sublime, add the files into the packages folder.
if you don't know where the packages folder is, in Sublime, go to Preferences -> Browse Packages.

also, for the first time you add this to your sublime, you need to go to Preferences -> Settings - User and add the following lines at the beginning of the json:

	"word_separators": "./\\()\"'-:,.;<>~!%^*|+=[]{}`~?",
		"auto_complete_triggers":
	[
		{
			"characters": "#",
			"selector": "text, source"
		},
		{
			"characters": "@",
			"selector": "text.html"
		},
		{
			"characters": "\\$",
			"selector": "source.js"
		}
	],
	
a list containing all the current shortcuts, with a short explanation about the functions,can be found here:


for key binding, this format needs to be added the the key binding user file:

to change syntex:

	{
		"keys": ["f9"], 
		"command": "set_file_type",
		"args": {
			"syntax": "Dooble/HTMLpp.tmLanguage"
		}
	},

for word wrap:

	{ "keys": ["f6"], "command": "toggle_setting", "args": {"setting": "word_wrap"} },


https://github.com/doobleweb/sublime-dooble/blob/master/Shortcuts.md
(open on raw)
