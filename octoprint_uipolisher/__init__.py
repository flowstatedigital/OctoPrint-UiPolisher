# coding=utf-8

import octoprint.plugin

class uipolisher(octoprint.plugin.AssetPlugin,octoprint.plugin.SettingsPlugin,octoprint.plugin.TemplatePlugin):

	##~~ AssetPlugin mixin
	
	def get_assets(self):
		return dict(js=["js/uipolisher.js"])
		
	##~~ SettingsPlugin mixin

	def get_settings_defaults(self):
		return dict(buffer_size=20)
		
	def get_version(self):
		return self._plugin_version
		
	##~~ Softwareupdate hook
	def get_update_information(self):
		return dict(
			floatingnavbar=dict(
				displayName="UI Polisher",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="flowstatedigital",
				repo="OctoPrint-UiPolisher",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/flowstatedigital/OctoPrint-UiPolisher/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "UI Polisher"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = floatingnavbar()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}