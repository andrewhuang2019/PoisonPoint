
var location_number = 0;

var removed_restaurant_array = [];
var selected_restaurant = "";
var selected_foods = [];

//<input type="text" placeholder="Enter a restaurant" id="autocomplete0" />
//<script>initAutocomplete(0)</script>
//<input type="date" name="time">

function create_new_location(){

    //update_restaurant_array();

    //creates a new select tag in the html document
    //var new_select = document.createElement('select');

    if (location_number < 5){
        var new_input = document.createElement('input');

        new_input.type = "text";
        new_input.id = 'autocomplete' + location_number;
        new_input.placeholder = "Enter a restaurant";
    
        document.getElementById('location_form').append(new_input);
    
        initAutocomplete(location_number);

        var new_time = document.createElement('input');
        new_time.type = "date";
        new_time.name = "time" + String(location_number);
        new_time.id = "time" + String(location_number);
    
        document.getElementById('location_form').appendChild(new_time);
    
        //appends a break to the tag with the location_form id
        document.getElementById('location_form').appendChild(document.createElement('br'));
    
        location_number++;
        new_input.onchange = onPlaceChanged();
    
    
    } 
    if (location_number == 4) {
        removed_plus = document.getElementById('plus_id');
        removed_plus.remove();
    }


    // //sets the select tag attributes for id and name
    // new_select.id = "places" + location_number;
    // new_select.name = "location" + String(location_number);

    // //document.getElementById('places').addEventListener('click');
    

    // //new_select.onchange = select_restaurant(document.getElementById(this));

    // //creates a new option tag in the html document


    // //sets the option tag attributes for the text content and its value
    // for (let num in current_restaurant_array){
    //     var option = document.createElement('option');
    //     option.textContent = current_restaurant_array[num];
    //     option.value = option.textContent;
    //     option.id = "location_option" + num;
    //     new_select.appendChild(option);

    // }
    
    // //appends the select tag to the tag with the location_form id
    // document.getElementById('location_form').appendChild(new_select);


}

/*
function store_array(restaurants){

    for(let restaurant in restaurants){
        updated_array.push(restaurant);
    }

}*/

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

let autocomplete;
function initAutocomplete(num){
    autocomplete = new google.maps.places.Autocomplete(
        document.getElementById('autocomplete' + num),
        {
        types: ['establishment'],
        componentRestrictions: {'country':['US']},
        fields: ['place_id','geometry','name']
    });
    autocomplete.addListener('place_changed',onPlaceChanged);
}

function onPlaceChanged(){
    var place = autocomplete.getPlace();

    if (!place.geometry){
        document.getElementById('autocomplete').placeholder = 'Enter a restaurant';
    } else{

        var data = {
            "name": place.name,
            "ID": place.place_id,
            "location": place.geometry
        };
        
        var jsonData = JSON.stringify(data);

        fetch('/summary', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            },
            body: jsonData
        })

    }
}