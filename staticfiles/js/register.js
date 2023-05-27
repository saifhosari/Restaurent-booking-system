
    $('#registration_form').on('submit', function(event) {
      event.preventDefault();  // Prevent normal form submission
      // Submit the form via AJAX using the ajaxSubmit() function
      $(this).ajaxSubmit({
        url: register_url,  // Replace 'register' with your actual URL name
        type: 'POST',
        success: function(response) {
          // Display the response in the target element
          
          setTimeout(function() { 
            $('.alert_msg').css('display', 'none') 
            $('.alert_msg').css('display', 'block')
          $('.alert_msg').html(response.developer_msg) 
          location.href = "/"
        }, 2000)
            
        },
        error: function(response) {
          // Handle the error if necessary
          $('.alert_msg').css('display', 'block')
          $('.alert_msg').html(response.developer_msg) 
          setTimeout(function() { 
            $('.alert_msg').css('display', 'none') 
            
        }, 2000)
        }
      });
    });