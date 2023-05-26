$('#booking_form').on('submit', function(event) {
    event.preventDefault();  // Prevent normal form submission

    // Submit the form via AJAX using the ajaxSubmit() function
    guest_names = $('.guest_name')
    guest_cnic = $('.guest_phone')
    var guest_cnic = guest_cnic.map(function() {
        return this.value;
    }).get();

    var guest_names = guest_names.map(function() {
        return this.value;
    }).get();
    
    var guestList = guest_names.map(function(name, index) {
        var guest = {};
        guest[name] = guest_cnic[index];
        return guest;
      });

    if (!$(this).valid()){
        return ;
    }
    $(this).ajaxSubmit({
        url: url,  // Replace 'register' with your actual URL name
        type: 'POST',
        data: {'guest_names': JSON.stringify(guest_names), 'guest_phone': JSON.stringify(guest_cnic)},
        success: function(response) {
        // Display the response in the target element
        if (response.developer_msg){
            Swal.fire(
                `${response.developer_msg}`,  
              )
            }else{
                Swal.fire(
                    `${response.reserved_user}`,
                    `Booked Successfully`,
                    'success'
                  )
                }
            },
    
        error: function(xhr, errmsg, err) {
        // Handle the pb error if necessary
        }
    });
    });