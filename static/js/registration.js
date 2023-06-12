async function registration() {
    let email = document.getElementById("email").value
    let password = document.getElementById("password").value
    if (email === '' || password === ''){
        alert('почта и пароль должны быть')
        return
    }

    let authdata = JSON.stringify({
        'email': email,
        'password': password,
        "is_active": true,
        "is_superuser": false,
        "is_verified": false
    })

    let response = await fetch("/auth/register", {
        method: 'POST', body: authdata,
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
          },
    })

    if (response.status === 201) {
        await login(email, password)
    }else{
        response.json().then(x => alert(JSON.stringify(x)))
    }
}

async function login(email, password){
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

    if (response.status !== 200){
        response.json().then(x => alert(JSON.stringify(x)))
        return
    }

    let object = await response.json()
    let token = object['access_token']
    localStorage.setItem('accessToken', 'Bearer '+ token)
    window.location.replace('/')
}