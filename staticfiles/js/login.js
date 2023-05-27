
    $('#login_form').on('submit', function(event) {
        event.preventDefault();  // Prevent normal form submission

        // Submit the form via AJAX using the ajaxSubmit() function
        $(this).ajaxSubmit({
          url: login_url,  // Replace 'register' with your actual URL name
          type: 'POST',
          success: function(response) {
            // Display the response in the target element
            if (response.response == 1){
              $('.alert_msg').css('display', 'block')
              Swal.fire(
                `Logged in as`,
                `${response.username}`,
                'success'
              )
        
              setTimeout(function() { 
                location.href = "/"
              }, 2000)
            }else if (response.response == 0){
              $('.alert_msg').css('display', 'block')
              $('.alert_msg').html("Username or Password is incorrect")
            }else{
              $('.alert_msg').css('display', 'block')
              $('.alert_msg').html(response.developer_msg) 
            }
            // $('.alert_msg').css('display', 'block')
            // $('.alert_msg').html(response.developer_msg) 
            
            
            
              // console.log(response)
          },
          error: function(response) {
            // Handle the error if necessary
            console.log(response)
            $('.alert_msg').css('display', 'block')
             
            setTimeout(function() { 
              $('.alert_msg').css('display', 'none') 
          }, 2000)
          }
        });
      });