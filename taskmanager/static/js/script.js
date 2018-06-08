
$('.name').mouseout(function(event){
    var box = $(this);    
    $.ajax(box.data('url'), {
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
