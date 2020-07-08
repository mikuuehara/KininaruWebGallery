
$(function () {
    let num = $(".now_num").attr('id'); 
    $(".one_form").change(function () {  
        var i = $(this).attr('id');  

        $(this).delay(300).fadeOut();
        
        if(i == 1){
            $("#submit_btn").delay(600).css('display','inline-block');
        }
        else{
            $(".now_num").text(Number(num)-i+2); 
        }
    })

})