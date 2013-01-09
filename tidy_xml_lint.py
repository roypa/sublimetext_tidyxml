import sublime, sublime_plugin, subprocess
import re

class TidyXmlLintCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # Setting the environment variable XMLLINT_INDENT controls the indentation. The default value is two spaces " ".
    # To use TAB for indentation, prefix command with: XMLLINT_INDENT=$'\t'
    command = "xmllint --format --noblanks --encode utf-8 -"

    # help from http://www.sublimetext.com/forum/viewtopic.php?f=2&p=12451
    xmlRegion = sublime.Region(0, self.view.size())

    xmlString = self.view.substr(self.view.sel()[0])
    # Remove new line characters
    xmlString = re.sub('\r\n?|\n', '', xmlString)

    # Run xmllint command
    p = subprocess.Popen(command, bufsize=-1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    result, err = p.communicate(xmlString.encode('utf-8'))

    if err != "":
      self.view.set_status('xmllint', "xmllint: "+err)
      sublime.set_timeout(self.clear,10000)
    else:
      self.view.replace(edit, self.view.sel()[0], result.decode('utf-8'))
      sublime.set_timeout(self.clear,0)

  def clear(self):
    self.view.erase_status('xmllint')
