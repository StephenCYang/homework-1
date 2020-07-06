// LOADING DATA
var tableData = data;

// ADDING DATA TO TABLE
var table = d3.select("tbody");

function populateData(){
	for (var i = 0; i < tableData.length; i++){
		var row = table.append("tr");

		var cell = row.append("td");
		cell.text(tableData[i].datetime);

		cell = row.append("td");
		cell.text(tableData[i].city);

		cell = row.append("td");
		cell.text(tableData[i].state);

		cell = row.append("td");
		cell.text(tableData[i].country);

		cell = row.append("td");
		cell.text(tableData[i].shape);

		cell = row.append("td");
		cell.text(tableData[i].durationMinutes);

		cell = row.append("td");
		cell.text(tableData[i].comments);
	}
};
populateData(); // displaying the data to the user

// FILTERING BASED ON USER INPUTS
var filterButton = d3.select("button")
var form = d3.select("form")

filterButton.on("click",userInput);
form.on("submit",userInput);

function userInput(event){
    d3.event.preventDefault(); // without this, page refreshes immediately after filtering.
    var inputElement = d3.select(".form-control");
    var inputValue = inputElement.property("value");
    var filteredData = tableData.filter(ufo => ufo.datetime === inputValue);
	table.html("");
    filteredData.forEach(function(sighting){
        var row = table.append("tr");
        Object.entries(sighting).forEach(function([key,value]){
            var cell = row.append("td");
            cell.text(value);
        });
    });
};

// NOT NECESSARY, JUST TRYING OUT. REFRESHING THE TABLE, NOT THE PAGE.
function drop_table(){
	var tabledrop = document.getElementById("ufo-table");
	for(var i = tabledrop.rows.length - 1; i > 0; i--)
	{
		tabledrop.deleteRow(i);
	}
	populateData();
};

var refresh_button = d3.select("button_2")
refresh_button.on("click",drop_table);