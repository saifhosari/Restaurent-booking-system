
    $('#login_form').on('submit', function(event) {
        event.preventDefault();  // Prevent normal form submission

        // Submit the form via AJAX using the ajaxSubmit() function
        $(this).ajaxSubmit({
          url: login_url,  // Replace 'register' with your actual URL name
          type: 'POST',
          success: function(response) {
            // Display the response in the target element
            $('.alert_msg').css('display', 'block')
            $('.alert_msg').html(response.developer_msg) 
            setTimeout(function() { 
              $('.alert_msg').css('display', 'none') 
              
          }, 2000)
            location.href = "/restaurent/"
              console.log(response)
          },
          error: function(xhr, errmsg, err) {
            // Handle the error if necessary
            $('.alert_msg').css('display', 'block')
            $('.alert_msg').html(response.developer_msg) 
            setTimeout(function() { 
              $('.alert_msg').css('display', 'none') 
              
          }, 2000)
          }
        });
      });