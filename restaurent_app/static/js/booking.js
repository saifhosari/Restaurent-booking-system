$('#booking_form').on('submit', function(event) {
    event.preventDefault();  // Prevent normal form submission
        alert("=== In booking ==")

    // Submit the form via AJAX using the ajaxSubmit() function
    console.log(location.href)
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
      console.log($(this).valid())
      console.log(guestList);
    if (!$(this).valid()){
        console.log("insude")
        return ;
    }
    $(this).ajaxSubmit({
        url: url,  // Replace 'register' with your actual URL name
        type: 'POST',
        data: {'guest_names': JSON.stringify(guest_names), 'guest_phone': JSON.stringify(guest_cnic)},
        success: function(response) {
            console.log(response)
        // Display the response in the target element
        Swal.fire(
            `${response.reserved_user}`,
            `Booked Successfully`,
            'success'
          )
        },
        error: function(xhr, errmsg, err) {
        // Handle the error if necessary
        console.log("Failure!!")
        }
    });
    });