async function login(){
    let email = document.getElementById("email").value
    let password = document.getElementById("password").value
    if (email === '' || password === ''){
        alert('почта и пароль должны быть')
        return
    }
    let authdata = {
        'username': email,
        'password': password,
        'grant_type': '',
        'scope': '',
        'client_id': '',
        'client_secret': '',
    }

    let response = await fetch("/auth/jwt/login",
        {
            method: 'POST',
            body: new URLSearchParams(authdata),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'accept': 'application/json'
            },
        })

    if (response.status === 200){
        window.location.replace('/')
    }else {
        response.json().then(x => alert(JSON.stringify(x)))
        return
    }

    let object = await response.json()
    let token = object['access_token']
    localStorage.setItem('accessToken', 'Bearer '+ token)
}