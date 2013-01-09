# sublimetext_tidyxml
Formatting XML in Sublime Text 2 using xmllint.

Based upon this blog post: http://www.bergspot.com/blog/2012/05/formatting-xml-in-sublime-text-2-xmllint/

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
1. Done, now select XML and press Cmd + K, Cmd + F (OS X)

### Problems?

If the command is not working, have a look at the status line.
Any error messages from xmllint will be shown there.
