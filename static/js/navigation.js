let accessToken = localStorage.getItem('accessToken')
if (accessToken !== undefined && accessToken !== null){
    document.getElementById('tag-login').remove()
    document.getElementById('tag-registration').remove()
}else{
    document.getElementById('tag-upload').remove()
}