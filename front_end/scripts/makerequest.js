


function add_to_database(data){

    return new Promise((resolve, reject) => {

        fetch('http://127.0.0.1:5500', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({key: data})
        }, )
        .then(response => response.json())
        .then(data => {
            resolve("Success!");
        })
        .catch((error) => {
            reject("Error!");
        })

    })

}

function get_from_database(data){

    return new Promise((resolve, reject) => {

        fetch('http://127.0.0.1:5500', {
            method: 'get',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }, )
        .then(response => response.json())
        .then(data => {
            resolve("Success!");
        })
        .catch((error) => {
            reject("Error!");
        })

    })

}

function remove_from_database(data){

    return new Promise((resolve, reject) => {

        fetch('http://127.0.0.1:5500', {
            method: 'delete',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({key: data})
        }, )
        .then(response => response.json())
        .then(data => {
            resolve("Success!");
        })
        .catch((error) => {
            reject("Error!");
        })

    })

}