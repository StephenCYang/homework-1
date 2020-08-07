// Function to cap first letter of string
function capFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

// D3 shortcuts
var selector = d3.select("#selDataset")
var demo_data = d3.select("#sample-metadata")

d3.json("samples.json").then(function(data){
    var participant_id = data.names;
    var metadata = data.metadata;
    var sample_data = data.samples;
    
    // Initial loading of the data to dashboard
    demo_data.html("");
    Object.entries(metadata[0]).forEach(function([key, value]){
        demo_data.append("p").text(`${capFirstLetter(key)}: ${value}`)
    });

    initial_bar_chart(sample_data[0]);
    initial_bubble_chart(sample_data[0]);

    // User selection
    participant_id.forEach(function(person, index){
        var user_selection = selector.append("option")
        user_selection.attr("value", index).text(person)
    });
    
    // Updates based on user selection
    selector.on("change",updateChart);

    function updateChart(event){
        var selected_value = selector.property("value");
        console.log(selected_value);
        console.log(sample_data[selected_value]);
        console.log(metadata[selected_value]);
        
        // Updates Demographic Info box based on user selection
        demo_data.html("");
        Object.entries(metadata[selected_value]).forEach(function([key, value]){
            demo_data.append("p").text(`${capFirstLetter(key)}: ${value}`)
        });
        
        // Updates charts based on user selection
        update_bar_chart(sample_data[selected_value]);
        update_bubble_chart(sample_data[selected_value]);
    };
});

// BAR CHART
function initial_bar_chart(selected_sample){
    // Display the top 10 OTUs found in that individual
    var bar_labels = selected_sample.otu_ids.slice(0,10);
    var bar_values = selected_sample.sample_values.slice(0,10);
    var bar_hovertext = selected_sample.otu_labels.slice(0,10);
    
    var trace1 = {
        x : bar_values.reverse(),
        y : bar_labels.map(data=>`OTU-${data}`).reverse(),
        text: bar_hovertext.reverse(),
        type : "bar",
        orientation : "h"
    };
    
    var bar_data = [trace1];
    var layout = {
        title: `<b>Top 10 Microbial Species Found</b>`,
        xaxis:{title:"Amount Found"},
        yaxis:{title: "OTU ID"}
    };
    var config = {responsive: true};
    Plotly.newPlot("bar", bar_data, layout, config);
};

function update_bar_chart(selected_sample){
    var bar_labels = selected_sample.otu_ids.slice(0,10);
    var bar_values = selected_sample.sample_values.slice(0,10);
    var bar_hovertext = selected_sample.otu_labels.slice(0,10);
    var update = { title: `<b>Top 10 Microbial Species Found</b>`};

    Plotly.restyle("bar","x",[bar_values.reverse()]);
    Plotly.restyle("bar","y",[bar_labels.map(data=>`OTU-${data}`).reverse()]);
    Plotly.restyle("bar","text",[bar_hovertext.reverse()]);
    Plotly.relayout("bar",update)
};

//  BUBBLE CHART
function initial_bubble_chart(selected_sample){
    var bubble_otu_id = selected_sample.otu_ids;
    var bubble_value = selected_sample.sample_values;
    var bubble_text_values = selected_sample.otu_labels;
    
    var trace = {
        x : bubble_otu_id,
        y : bubble_value,
        mode: "markers",
        marker: {
            size: bubble_value,
            color: bubble_otu_id,
            colorscale: "Portland"
        },
        text: bubble_text_values
    };

    var layout = {
        width:"1100",
        height: "600",
        title: `<b>Microbial Species Found Per Sample</b>`,
        showlegend: false,  xaxis:{title:"OTU ID"},
        yaxis:{title: "Amount Per Sample"}
    };

    var bubble_data = [trace];
    var config = {responsive: true};
    Plotly.newPlot("bubble",bubble_data,layout,config);
};

function update_bubble_chart(selected_sample){
    var bubble_otu_id = selected_sample.otu_ids;
    var bubble_value = selected_sample.sample_values;
    var bubble_text_values = selected_sample.otu_labels;
    var update = {title: `<b>Microbial Species Found Per Sample</b>`};
    
    Plotly.restyle("bubble","x",[bubble_otu_id]);
    Plotly.restyle("bubble","y",[bubble_value]);
    Plotly.restyle("bubble","marker",[{
        size: bubble_value,
        color: bubble_otu_id,
        colorscale: "Portland"}
    ]),
    Plotly.restyle("bubble","text",[bubble_text_values]);
    Plotly.relayout("bubble",update);
};