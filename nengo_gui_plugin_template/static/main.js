Nengo.NetGraphItem.prototype.menu_extensions.push(function (item) {
    entries = []
    if (item.type == 'ens') {
        entries.push(
            ['Plugin template', function() { alert('Hello world!'); }]);
        entries.push(
            ['Plugin graph', function() { item.create_graph(
                'nengo_gui_plugin_template/graph_name') }]);
    }
    return entries
})


NengoGuiPluginTemplateGraph = function(parent, sim, args) {
    Nengo.Component.call(this, parent, args);
    var self = this;

    this.div.innerHTML = 'Hello world!';
};
NengoGuiPluginTemplateGraph.prototype = Object.create(Nengo.Component.prototype);
