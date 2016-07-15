from setuptools import setup, find_packages


setup(
    name='nengo_gui_plugin_template',
    version='0.1',
    description="Template for nengo_gui plugins.",
    author="Jan Gosmann",
    packages=find_packages(),
    install_requires=['nengo_gui'],  # TODO minimal version
    entry_points={
        'nengo_gui.plugins': [
            'plugin_name = nengo_gui_plugin_template.plugin:PluginTemplate'
        ],
        'nengo_gui.components': [
            'graph_name = nengo_gui_plugin_template.graph:Graph'
        ],
    }
)
