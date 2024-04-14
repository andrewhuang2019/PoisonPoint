
var location_number = 0;

var removed_restaurant_array = [];
var selected_restaurant = "";
var selected_foods1 = [];
var selected_foods2 = [];
var selected_foods3 = [];
var times = [];

function create_new_location(){

    if (location_number < 3){
        var new_input = document.createElement('input');

        new_input.type = "text";
        new_input.id = 'autocomplete' + location_number;
        new_input.placeholder = "Enter a restaurant";
    
        document.getElementById('location_form').append(new_input);
    
        initAutocomplete(location_number);

        var new_time = document.createElement('input');
        new_time.type = "date";
        new_time.name = "time" + location_number;
        new_time.id = "time" + location_number;
        
        //new_time.onchange = ;
        //new_time.addEventListener("change", checkTimes(location_number));
    
        document.getElementById('location_form').appendChild(new_time);
    
        //appends a break to the tag with the location_form id
        document.getElementById('location_form').appendChild(document.createElement('br'));

        location_number++;
        //new_input.onchange = onPlaceChanged();

    } 
    if (location_number == 3) {
        removed_plus = document.getElementById('plus_id');
        removed_plus.remove();
    }

}

function check_checkboxes(){
    var checkboxes1 = document.querySelectorAll('input[name="restaurant1"]:checked');
    var checkboxes2 = document.querySelectorAll('input[name="restaurant2"]:checked');
    var checkboxes3 = document.querySelectorAll('input[name="restaurant3"]:checked');
    checkboxes1.forEach(function(checkbox) {
        selected_foods1.push(checkbox.value);
    });
    checkboxes2.forEach(function(checkbox) {
        selected_foods2.push(checkbox.value);
    });
    checkboxes3.forEach(function(checkbox) {
        selected_foods3.push(checkbox.value);
    });

    data = {
        'foods1': selected_foods1,
        'foods2': selected_foods2,
        'foods3': selected_foods3
    }

    jsonData = JSON.stringify(data);

    fetch('food_summary', {
        method: "POST",
        headers: {
            'Content-type': 'application/json'
        },
        body: jsonData
    })

    selected_foods1 = [];
    selected_foods2 = [];
    selected_foods3 = [];

}

function checkTimes(num){
    
    data_value = document.getElementById('time' + num).value;
    var data = {'time': data_value}
    //window.alert("reached checkTimes");
    jsonData = JSON.stringify(data);

    fetch('time_summary', {
        method: "POST",
        headers: {
            'Content-type': 'application/json'
        },
        body: jsonData
    })
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

        fetch('/location_summary', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            },
            body: jsonData
        })

    }
}