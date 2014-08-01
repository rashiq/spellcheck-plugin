import sublime
import sublime_plugin

SETTINGS_FILE = 'Preferences.sublime-settings'
SETTING_NAME = 'spell_check'

class ToggleSpellCheckCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        s = sublime.load_settings(SETTINGS_FILE)
        spell_check_setting = s.get(SETTING_NAME, False)
        s.set(SETTING_NAME, not spell_check_setting)
        sublime.save_settigs(SETTINGS_FILE)
