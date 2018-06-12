
$('#id_name').mouseout(function(event){
    var box = $(this);    
    $.ajax('/checkname', {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data': {
          'name': box.val(),
          'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
        },
        success: function(data){
          if (data.a == 1){
          $('.double_name_alert').removeClass('d-none');
        } else {
          $('.double_name_alert').addClass('d-none');
        }
        },
      
    });
});



  $('#category-selector select').change(function(event){
    // get value of currently selected group option
    var cat = $(this).val();

    if (cat) {
      // set cookie with expiration date 1 year since now;
      // cookie creation function takes period in days
      $.cookie('current_category', cat, {'path': '/', 'expires': 365});
    } else {
      // otherwise we delete the cookie
      $.removeCookie('current_category', {'path': '/'});
    }

    // and reload a page
    location.reload(true);

    return true;
  });


$( function() {
    $( "#id_start" ).datepicker();
  } );

$( function() {
    $( "#id_finish" ).datepicker();
  } );