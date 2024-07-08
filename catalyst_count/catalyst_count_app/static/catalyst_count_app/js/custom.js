$(document).ready(function(){
    //file uploader
    $("#form1").submit(function(e){
        e.preventDefault();
        let formData = new FormData();
        formData.append('myfile',$('#file1')[0].files[0])

        $.ajaxSetup({
          
                headers: {
                    "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
                }
            });


        $.ajax({
            xhr: function () {
                let xhr= new window.XMLHttpRequest();
                xhr.upload.addEventListener('progress',function(e){
                    if (e.lengthComputable) {
                        
                        percentage=Math.round((e.loaded / e.total) * 100)

                        $("#progress").attr("aria-valuenow",percentage)
                        $("#progressBar").css('width',percentage+'%').html(percentage + '%');
                    }
                })
                return xhr
            },
            url : 'http://127.0.0.1:8000/post/',
            type : 'POST',
            data : formData,
            processData: false, 
            contentType: false,
            success : function(data) {
          
             var results = $.trim(data);
             console.log(results);
          
            },
            error: function(request, status, error){
             alert('Something went wrong; please try again');
            }
           });
    })



    // select query
    $("#form2").submit(function(e){
        e.preventDefault();
        const industry=$("#industry :selected").text()
        let formData = new FormData();
        formData.append("industry",industry)

    $.ajax({
        url:"http://127.0.0.1:8000/post/",
        type:"POST",
        data:formData,
        processData:false,
        contentType:false,
        success: function (data) {
            var results = $.trim(data);
             console.log(results);
        },
        error: function(request, status, error){
             alert('Something went wrong; please try again');
        
        
    });
        
        
                      
    })
})


