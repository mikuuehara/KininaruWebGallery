$(function () {
    $(".2").change(function () {
        console.log("bbb")
        $('input:checked').each(function () {
            $(".2").css('display','none');

            console.log("aaa");
        })

    })
})
