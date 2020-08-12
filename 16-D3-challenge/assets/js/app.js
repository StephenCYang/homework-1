// setting dimensions for the chart.
var svgWidth = 800;
var svgHeight = 600;

var margin = {
    top: 80,
    right: 80,
    bottom: 80,
    left: 80
};

// Setting dimensions to hold the chart
var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Cerating the SVG container
var svg = d3.select("#scatter")
.append("svg")
.attr("width", svgWidth)
.attr("height", svgHeight);

// Creating a group to then hold chart data
var chartGroup = svg
.append("g")
.attr("transform", "translate(" + margin.left + ", "+margin.top+")");

// Import data file
var dataFile = "assets/data/data.csv"

// Function is called and passes csv data
d3.csv(dataFile).then(vizData);

// Function takes in argument stateData
function vizData(stateData) {
    stateData.map(function (data) {
        data.poverty = +data.poverty;
        data.obesity = +data.obesity;
    });

// Setting up axes to aling with the min and max values of the data
// TODO: Insted of using 8.5, predefine the min like with the max.
  var xScale = d3.scaleLinear()
    .domain([8.5, d3.max(stateData, d => d.poverty)])
    .range([0, width]);

  var yScale = d3.scaleLinear()
    .domain([20, d3.max(stateData, d => d.obesity)])
    .range([height, 0]);

  var bottomAxis = d3.axisBottom(xScale);
  var leftAxis = d3.axisLeft(yScale);

// Append the axes to the chart group
  chartGroup.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis);
  chartGroup.append("g")
    .call(leftAxis);

// Create dots/circles for the plot
  var circlesGroup = chartGroup.selectAll("circle")
    .data(stateData)
    .enter()
    .append("circle")
    .attr("cx", d => xScale(d.poverty))
    .attr("cy", d => yScale(d.obesity))
    .attr("r", "13")
    .attr("fill", "#333333")

// Add text to circles 
  var circlesGroup = chartGroup.selectAll()
    .data(stateData)
    .enter()
    .append("text")
    .attr("x", d => xScale(d.poverty))
    .attr("y", d => yScale(d.obesity))
    .style("font-size", "12px")
    .style("text-anchor", "middle")
    .style('fill', 'white')
    .text(d => (d.abbr));
}

// Create axes labels
chartGroup.append("text")
.attr("transform", "rotate(-90)")
.attr("y", -50)
.attr("x", 0 - (height/2)-60) /* Need to figure out better way to do spacing*/
.text("Lacks Healthcare (%)");


chartGroup.append("text")
.attr("y", height+50)
.attr("x", (width/2)-30) /* Need to figure out better way to do spacing*/
.attr("class", "axisText")
.text("In Poverty (%)");