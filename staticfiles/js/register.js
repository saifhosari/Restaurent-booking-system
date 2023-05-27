
    $('#registration_form').on('submit', function(event) {
      event.preventDefault();  // Prevent normal form submission
      // Submit the form via AJAX using the ajaxSubmit() function
      $(this).ajaxSubmit({
        url: register_url,  // Replace 'register' with your actual URL name
        type: 'POST',
        success: function(response) {
    
        if(response.response == 1 || response.response == 3){
          $('.alert_msg').css('display', 'block')
          $('.alert_msg').html(response.developer_msg)
        }else{
             setTimeout(function() { 
            location.href = "/"
          }, 2000)
          $('.alert_msg').css('display', 'block') 
            $('.alert_msg').html(response.developer_msg)
        }
        },
        error: function(response) {
          $('.alert_msg').css('display', 'block')
          $('.alert_msg').html(response.developer_msg) 
          setTimeout(function() { 
            $('.alert_msg').css('display', 'none') 
            
        }, 2000)
        }
      });
    });