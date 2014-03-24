var w = 1280,
    h = 800,
    r = 720,
    x = d3.scale.linear().range([0, r]),
    y = d3.scale.linear().range([0, r]),
    node,
    root;

var pack = d3.layout.pack()
    .size([r, r])
    .value(function(d) { return d.size; })

var vis = d3.select("#pack").append("svg")
    .attr("width", w)
    .attr("height", h)
    .attr("transform", "translate(" + (w - r) / 2 + "," + (h - r) / 2 + ")");

d3.json("proyectos.json", function(data) {
    node = root = data;

    var nodes = pack.nodes(root);

    vis.selectAll("circle")
	.data(nodes)
	.enter().append("svg:circle")
	.attr("class", function(d) { return d.children ? "parent" : "child"; })
	.attr("cx", function(d) { return d.x; })
	.attr("cy", function(d) { return d.y; })
	.attr("r", function(d) { return d.r; })
	.on("mouseover", mouseover)
	.on("click", function(d) { return zoom(node == d ? root : d); });

    d3.select(window).on("click", function() { zoom(root); });
});

function zoom(d, i) {
    var k = r / d.r / 2;
    x.domain([d.x - d.r, d.x + d.r]);
    y.domain([d.y - d.r, d.y + d.r]);

    var t = vis.transition()
	.duration(d3.event.altKey ? 7500 : 750);

    t.selectAll("circle")
	.attr("cx", function(d) { return x(d.x); })
	.attr("cy", function(d) { return y(d.y); })
	.attr("r", function(d) { return k * d.r; });

    node = d;
    d3.event.stopPropagation();
}

function mouseover(d) {
    console.log(d);
    d3.select("#wut").text(d.name);
}
