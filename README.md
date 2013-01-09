# sublimetext_tidyxml
Formatting XML in Sublime Text 2 using xmllint.

Based upon a [blog post by André Bergonse](http://www.bergspot.com/blog/2012/05/formatting-xml-in-sublime-text-2-xmllint/).

By default it will pretty format the XML by stripping all whitespaces.
But it will actually remove formatting in the text nodes, which may not be something you want to do.
You can disable this behaviour in the settings by setting `"strip-whitespaces": false`.

The indentation is by default set to 2 spaces, as is the default in xmllint.
Change this in the settings to what you want.

## Installation
To be able to use this plugin you need __xmllint__, which is provided by default in OS X and Linux.

In Windows you need to [download xmllint for Windows](http://code.google.com/p/xmllint/downloads/list).

### To install the plugin:

1. Go to your Sublime Text plugins directory
    * To find it, you can open Sublime Text and then: Preferences &rarr; Browse packages...
1. Clone the git repo into a folder "Tidy XML"
    * `git clone git@github.com:roypa/sublimetext_tidyxml.git "Tidy XML"`
1. Done, ready for use

## Usage
The command can be found in the menu as __Selection &rarr; Format &rarr; Tidy XML__

The shortcut is defined as Cmd+K, Cmd+F (OS X and Linux) and Ctrl+K, Ctrl+F (Windows).
If you forget the shortcut keys, you will find it in the Command Palette (Shift+Command+P) when typing "Tidy..."

Select the XML content and execute the command.

If no selection is done, it will try to format the whole file.
The file should then have only XML content, otherwise an error message will be shown in the status line describing the problem.

If `xmllint` is not able to parse the content as XML, an error message will be shown in the status line.
