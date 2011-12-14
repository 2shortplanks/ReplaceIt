ReplaceIt
---------

This is ReplaceIt, a plugin for [Sublime Text 2][subl] that gives
you a way to bind find and replaces to a keyboard shortcut.

Usage
-----

To use this you'll need to place something like this inside your key bindings:

    {
        "keys": ["ctrl+alt+super+g"],

        "command": "replace_it",
        "args": {
	        "find": "old text",
	        "replace": "new text"
	    }
    },

The command takes the following arguments:

### find

The string the plugin will search for and replace.  This argument is mandatory.

### replace

The string that the plugin will replace found text with.  This argument is mandatory

### regex

A boolean indicating that we should treat the the string we're searching for as a regular expression
to match instead of a string.  This argument is optional, and by default this feature is off.

### ignore_case

A boolean indicating that we should ignore the case when we're searching for text.  This argument is optional, and by default this feature is off.

### only_next

A boolean indicating that we shouldn't do a global search and replace but just replace the next occurrence after the start of the current selection / cursor position.  This argument is optional, and by default this feature is off.

Installation
------------

Assuming you've got git installed (you don't? shame on you!)

	cd ~/Library/Application Support/Sublime Text 2/Packages
	git co git://github.com/2shortplanks/ReplaceIt.git

To update

	cd ~/Library/Application Support/Sublime Text 2/Packages/ReplaceIt
	git pull

[subl]: http://www.sublimetext.com/2