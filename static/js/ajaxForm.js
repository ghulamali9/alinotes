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
  var file;
  $('#id_img_file').on('change', function(){
  file = event.target.files;
  });
  var SaveForm = function(e){
      var form = $(this);
        e.preventDefault();
        e.stopImmediatePropagation();
        var dataf = new FormData($(form).get(0));
        dataf.append('file', $('#id_img_file')[0].files);
        $.ajax({
          url: form.attr('data-url'),
          data: dataf,
          type: form.attr('method'),
          dataType: 'json',
          processData: false,
          contentType: false,
          cache: false,
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
