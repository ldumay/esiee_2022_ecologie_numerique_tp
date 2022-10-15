export default class APIService{
    // Insert an article
    static SendData(body){
        return fetch(`http://127.0.0.1:5000/testapps`,{
            'method':'POST',
             headers : {
                'Content-Type':'application/json',
                'Access-Control-Allow-Origin' : 'http://192.168.1.24:3000',
                'Access-Control-Allow-Credentials' : true
      },
      body:JSON.stringify(body)
    })
    .then(response => response.json())
    .catch(error => console.log(error))
    }

}