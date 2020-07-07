
$(function () {
    let num = 1;
    $(".one_form").change(function () {  
        var i = $(this).attr('id');  
        console.log(i);
        $(this).delay(300).fadeOut();

        if(i == 1){
            $("#submit_btn").delay(600).css('display','inline-block');
        }
    })

})
//$('.now_num').text();