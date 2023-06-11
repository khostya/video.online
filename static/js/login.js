async function login(){
    let email = document.getElementById("email").value

    let password = document.getElementById("password").value
    let authdata = {
        'username': email,
        'password': password,
        'grant_type': '',
        'scope': '',
        'client_id': '',
        'client_secret': '',
    }

    let response = await fetch("http://localhost:8000/auth/jwt/login",
        {
            method: 'POST',
            body: new URLSearchParams(authdata),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'accept': 'application/json'
            },
        })

    if (response.status === 200){
        alert("Успех!")
    }

    let object = await response.json()
    let token = object['access_token']
    localStorage.setItem('accessToken', 'Bearer '+ token)
}