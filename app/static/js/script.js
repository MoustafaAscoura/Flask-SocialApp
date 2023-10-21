$(".delete-post").on("click", (e) => {
    e.preventDefault()
    $.ajax({
      url: e.target.href,
      type: "DELETE",
    });
    e.target.closest('.card').remove()
  });

$("form[mode='edit'").submit(function(evt){   
  evt.preventDefault();
  var formData = new FormData($(this)[0]);
  $.ajax({
    url: window.location.href,
    type: 'PUT',
    data: formData,
    async: false,
    cache: false,
    contentType: false,
    enctype: 'multipart/form-data',
    processData: false,
  });
  window.location.href = window.location.origin + '/posts'
}); 
    

// $("form button[mode='edit']").on("click", (e) => {
//   e.preventDefault()
//   var formData = new FormData();
//   formData.append("title", $("#posttitle:eq(0)").val());
//   formData.append("body", $("#postbody:eq(0)").val());
//   formData.append("image", $("#postimage:eq(0)").prop('files')[0]);

//   $.ajax({
//     url: window.location.href,
//     type: "PUT",
//     data: formData,
//     enctype: 'multipart/form-data',
//   });
// });