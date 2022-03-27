console.log('connect')
function completeTask(u_id,id) { 
    console.log(u_id)
    $.ajax({
        type:"GET",
        url: 'complete/'+id,
        data: {
           
        },
        success: function (response) {
            console.log(response)  
            $("#id_"+id).delay(1000).fadeOut(800); 
        },
        error: function (response) {
            console.log(response)
        }
    }
    )
 }
 