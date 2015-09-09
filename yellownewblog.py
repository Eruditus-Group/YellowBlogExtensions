# Tools > New Plugin
# Save as signature.py

import datetime, getpass
import sublime, sublime_plugin

class yellownewblog(sublime_plugin.TextCommand):
    def run(self, edit):
        headers = """---\nTitle: \nPublished: %s\nAuthor: %s\nTags: \n---\n""" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), getpass.getuser())
        self.view.insert(edit, 0, headers)