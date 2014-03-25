var width = "800", height = "800";

var color = d3.scale.category10();

var degree_scale = d3.scale.linear()
    .domain([1, 20])
    .range([5,20]);

var weight_scale = d3.scale.linear()
    .domain([1, 4])
    .range([5,20]);

var force = d3.layout.force()
    .size([width, height])
    .friction(0.7)
    .gravity(0.09)
    .charge(-400)
    .linkDistance(100);

function dragstart(d) {
    d.fixed = true;
    d3.select(this).classed("fixed", true);
}


var drag = force.drag()
    .on("dragstart", dragstart);

var svg = d3.select("#chart").append("svg")
    .attr("width", width)
    .attr("height", height);

svg.append("svg:defs").selectAll("marker")
    .data(["link"])
    .enter().append("svg:marker")
    .attr("id", String)
    .attr("refX", -2)
    .attr("refY", 0.5)
    .attr("markerWidth", 1)
    .attr("markerHeight", 1)
    .attr("orient", "auto")
    .append("svg:circle")
    .attr("cx", 6)
    .attr("cy", 6)
    .attr("r", 10)
    .attr("fill", d3.rgb(20,200,200))





d3.json("coautores_recurrentes_jin.json", function(error, graph) {
    force
	.nodes(graph.nodes)
	.links(graph.links)
	.start();

    var link = svg.selectAll(".link")
    	.data(graph.links)
    	.enter().append("line")
    	.attr("class", "link")
        .style("stroke", function (d) { return color(d.jin);} )
    	.style("stroke-width", function(d) { return weight_scale(d.weight)})

    var gnodes = svg.selectAll('g.gnode')
        .data(graph.nodes)
        .enter()
        .append('g')
        .classed('gnode', true);


    var node = gnodes.append("circle")
        .attr("class", "node")
        .attr("r", function(d) { return degree_scale(d.degree); } )
        .call(force.drag);

    var labels = gnodes.append("text")
        .text( function(d) { return d.name; })
        .attr("font-size", "0.76em")
        .attr("text-align", "right");


    force.on("tick", function() {
	link.attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

	gnodes.attr("transform", function(d) { return 'translate(' + [d.x, d.y] + ')'; })

    });});
