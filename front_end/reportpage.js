
var num = 0;

var current_restaurant_array = ["Pizza Hut", "Chipotle", "McDonalds"];
var removed_restaurant_array = [];
var selected_restaurant = "";
var selected_foods = [];


function create_new_location(){

    update_restaurant_array();

    //creates a new select tag in the html document
    var new_select = document.createElement('select');

    //sets the select tag attributes for id and name
    new_select.id = "places" + num;
    new_select.name = "location" + String(num);

    //document.getElementById('places').addEventListener('click');
    

    new_select.onchange = select_restaurant(document.getElementById(this));

    //creates a new option tag in the html document


    //sets the option tag attributes for the text content and its value
    for (let num in current_restaurant_array){
        var option = document.createElement('option');
        option.textContent = current_restaurant_array[num];
        option.value = option.textContent;
        new_select.appendChild(option);

    }
    
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

function check_checkboxes(){
    var checkboxes = document.querySelectorAll('input[name="food[]"]:checked');
    checkboxes.forEach(function(checkbox) {
        selected_foods.push(checkbox.value);
    });

    //prints out the foods that are chosen in the array
    for(let num in selected_foods){
        var paragraph = document.createElement('p');
        paragraph.textContent = selected_foods[num];
        document.getElementById('food_division').appendChild(paragraph);
    }
}

function select_restaurant(restaurant){
    /*
    if (selected_element.value){
        selected_restaurant.add(selected_element.value);
        selected_element.dataset.previous_selected = selected_element.value;
    }    
    */
    //trying to get the option value so that i can reference it and pass in the selected restaurant value
    //so that update restaurant array can splice it out
    selected_restaurant = restaurant.value;
}

function update_restaurant_array(){
    index = current_restaurant_array.indexOf(selected_restaurant);
    if (index > -1){
        current_restaurant_array.splice(index, 1);
    }
}

function add_restaurant_array(){

}