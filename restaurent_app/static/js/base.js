
var login_url ="{% url 'login_user' %}"
var register_url = "{% url 'register' %}"

$('#login_modal').on('click', function(){
    $('#exampleModal').modal('show');
})
$('#register_modal').on('click', function(){
    $('#exampleModal1').modal('show');
})
