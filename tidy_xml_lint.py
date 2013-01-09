import sublime, sublime_plugin, subprocess
import re # Regular Expresssions

class TidyXmlLintCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    settings = sublime.load_settings("TidyXML.sublime-settings")

    # Setting the environment variable XMLLINT_INDENT controls the indentation. The default value is two spaces " ".
    # To use TAB for indentation, prefix command with: XMLLINT_INDENT=$'\t'
    command = "XMLLINT_INDENT='" + settings.get("xmllint-indent", "'  '") + "' xmllint --format --noblanks --encode utf-8 -"

    # Get the region for the selected text
    regions = self.view.sel()
    if len(regions) == 1 and regions[0].empty():
      # No selection, so use the entire buffer
      regions = [sublime.Region(0, self.view.size())]

    # Get the text for the first region
    xmlString = self.view.substr(regions[0])

    # Remove all consecutive whitespaces in text, and then leading and trailing spaces of the text nodes
    if settings.get('strip-whitespaces') == True:
      xmlString = re.sub('\s+', ' ', xmlString)
      xmlString = re.sub('>\s', '>', xmlString)
      xmlString = re.sub('\s<', '<', xmlString)

    # Run xmllint command
    # Hot to run file contents through external command, see http://www.sublimetext.com/forum/viewtopic.php?f=2&p=12451
    p = subprocess.Popen(command, bufsize=-1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    result, err = p.communicate(xmlString.encode('utf-8'))

    if err != "":
      self.view.set_status('xmllint', "xmllint: "+err)
      sublime.set_timeout(self.clear, 15000)
    else:
      self.view.replace(edit, regions[0], result.decode('utf-8'))
      sublime.set_timeout(self.clear, 0)

  def clear(self):
    self.view.erase_status('xmllint')
