from nengo_gui import plugin


class PluginTemplate(plugin.Plugin):
    def get_assets(self):
        return [plugin.ScriptAsset(
            'plugin/nengo_gui_plugin_template/plugin_name/static/main.js')]
