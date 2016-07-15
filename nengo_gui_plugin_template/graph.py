from nengo_gui.components.component import Component


class Graph(Component):
    def javascript(self):
        info = dict(uid=id(self), label="nengo_gui plugin template")
        json = self.javascript_config(info)
        return 'new NengoGuiPluginTemplateGraph(main, sim, %s);' % json
