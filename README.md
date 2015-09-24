# sublime-dooble
dooble extension

author - sahar zehavi

To add the Dooble Package to  Sublime,you first need to add a new repository to your package manager.
To do so, while in sublime, open the Command Palette. To open the palette, press ctrl+shift+p (Win, Linux) or cmd+shift+p (OS X). there, you should type "Add Repoitory" and then paste this link: "https://github.com/doobleweb/sublime-dooble".
after that, open the Command Palette again and type "Install Package". next you should search for this package (named "sublime-dooble") and press enter. you shoudld now restart your sublime, and enjoy.

After the package is install you can always check for upgrades by typeing "upgrade package" on the Command Pallette.
	
a list containing all the current shortcuts, with a short explanation about the functions,can be found here:
https://github.com/doobleweb/sublime-dooble/blob/master/Shortcuts.md
(open on raw)


Key nimding is NOT part of the package, so each user can add his own shortcuts the way he see fit.
for key binding, this format needs to be added the the key binding user file:

to change syntex:

	{
		"keys": ["f9"], 
		"command": "set_file_type",
		"args": {
			"syntax": "Packages/sublime-dooble/HTMLpp.tmLanguage"
		}
	},

for word wrap:

	{ "keys": ["f6"], "command": "toggle_setting", "args": {"setting": "word_wrap"} },



