
    $('#login_form').on('submit', function(event) {
        event.preventDefault();  // Prevent normal form submission

        // Submit the form via AJAX using the ajaxSubmit() function
        $(this).ajaxSubmit({
          url: login_url,  // Replace 'register' with your actual URL name
          type: 'POST',
          success: function(response) {
            // Display the response in the target element
            if (response.response == 1){
              let timerInterval
            Swal.fire({
              title:`Logged in as ${response.username}`,
              timer: 1000,
              timerProgressBar: true,
              didOpen: () => {
                Swal.showLoading()
                const b = Swal.getHtmlContainer().querySelector('b')
                timerInterval = setInterval(() => {
                  b.textContent = Swal.getTimerLeft()
                }, 100)
              },
              willClose: () => {
                clearInterval(timerInterval)
              }
            }).then((result) => {
              /* Read more about handling dismissals below */
              location.href="/"
            })

            }else{
              $('.alert_msg').css('display', 'block')
              $('.alert_msg').html("Invalid Email or Password") 
              setInterval(function () {
                $('.alert_msg').css('display', 'none')
            }, 5000);
          }
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