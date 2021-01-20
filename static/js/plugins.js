$(document).ready(function(){
  var ShowForm = function(){
    var btn = $(this);
    $.ajax({
      url: btn.attr('data-url'),
      type: 'get',
      dataType: 'json',
      beforeSend: function(){
        $('#modal-user').modal('show');
      },
      success: function(data){
        $('#modal-user .modal-content').html(data.html_form);
      }
    });
  }
  var SaveForm = function(e){
      var form = $(this);
        e.preventDefault();
        e.stopImmediatePropagation();
        $.ajax({
          url: form.attr('data-url'),
          data: form.serialize(),
          type: form.attr('method'),
          dataType: 'json',
          success: function(data){
            if(data.form_is_valid){
              console.log('data is saved');
              $('#user-table tbody').html(data.data_list);

              $('#modal-user').modal('hide');
            }
            else{
              console.log('data not saved');
              $('#modal-user .modal-content').html(data.html_form);
            }

          },
          error: function(data){
            console.log('not working');
          }
        });
      return false;
    }


//update
$("#user-table").on("click",".show-form-update",ShowForm);
$("#modal-user").on("submit",".update-form",SaveForm)
//delete
$("#user-table").on("click",".show-form-delete",ShowForm);
$("#modal-user").on("submit",".delete-form",SaveForm)

});
