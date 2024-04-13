
var num = 0;
var updated_array = ["Pizza Hut", "Chipotle", "McDonalds"];
var removed_array = [];

function create_new_location(){

    //creates a new select tag in the html document
    var new_select = document.createElement('select');

    //sets the select tag attributes for id and name
    new_select.id = "places";
    new_select.name = "location" + String(num);

    //creates a new option tag in the html document


    //sets the option tag attributes for the text content and its value
    for (let num in updated_array){
        var option = document.createElement('option');
        option.textContent = updated_array[num];
        option.value = option.textContent;
        new_select.appendChild(option);

    }
    //option.textContent = "Pizza Hut";
    //option.value = option.textContent;

    //appends the option tag to the select tag as a child (contained within)
    //new_select.appendChild(option);
    
    //appends the select tag to the tag with the location_division id
    document.getElementById('location_division').appendChild(new_select);

    var new_time = document.createElement('input');
    new_time.type = "date";
    new_time.name = "time" + String(num);

    document.getElementById('location_division').appendChild(new_time);

    //appends a break to the tag with the location_division id
    document.getElementById('location_division').appendChild(document.createElement('br'));

    num++;

}

function store_array(restaurants){

    for(let restaurant in restaurants){
        updated_array.push(restaurant);
    }

}