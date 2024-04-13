


function add_to_database(data){

    return new Promise((resolve, reject) => {

        fetch('local-url', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }, )

        const condition = true;
        if (condition){
            resolve("Success!");
        } else {
            reject("Error!");
        }

    })

}