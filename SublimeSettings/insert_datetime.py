import datetime

import sublime_plugin


DATETIME_FORMAT = '%d-%m-%Y %H:%M'


class InsertDatetimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        current_datetime = datetime.datetime.now()
        formatted = current_datetime.strftime(DATETIME_FORMAT)
        for s in selection:
            self.view.replace(edit, s, formatted)
