$(function () {

    /* タッチパネルでの挙動 */
    var moveX, moveY, posiY, posiX;;
    // 母数
    let num = Number($(".now_num").attr('id'));
    let num2 = num - 2;

    // 表示できるサイトが0だったとき
    if(num == 0){
        $(".site_none").css("display","inline-block");
    }

    // 指が触れたらstart_checkを実行
    $(".one_form").on("touchstart", start_check);

    // 指が動いたらmove_checkを実行
    $(".one_form").on("touchmove", move_check);

    // 指が離れたらend_checkを実行
    $(".one_form").on("touchend", end_check);


    function start_check(event) {
        // 現在の座標取得 
        posiY = getY(event);
        posiX = getX(event);

        // 移動距離状態を初期化 
        moveY = '';
        moveX = '';
    }

    function move_check(event) {
        if (posiX - getX(event) > 70) // 70px以上移動でスワイプと判断
        {
            // 右→左
            moveX = "left";

        } else if (posiX - getX(event) < -70) // 70px以上移動でスワイプと判断
        {
            // 左→右
            moveX = "right";
        }

        if (posiY - getY(event) > 70) // 70px以上移動でスワイプと判断
        {
            // 下→上

        } else if (posiY - getY(event) < -70) // 70px以上移動でスワイプと判断
        {
            // 上→下			

        }
    }


    function end_check(event) {

        // 現在評価中のフィールドid
        var target_name = event.target.className;
        //console.log(num)

        if (moveX == "left") {
            // 左スワイプで気にならない
            $('input[name=' + target_name + ']:eq(1)').prop('checked', true);

            // 左にスライド
            $('.one_form' + '.' + target_name).animate({
                right: '+=100vw'
            }, 400);

            // 揺らす
            setTimeout(function () {
                $('.kininaranai_zone').css('left', '8vw');
            }, 300);
            setTimeout(function () {
                $('.kininaranai_zone').css('left', '6vw');
            }, 500);

            // 分子の変更
            if (num2 == -1) {
                $("#submit_btn").delay(600).css('display', 'inline-block');
            } else {
                $(".now_num").text(num - num2);
                num2--;
            }

        } else if (moveX == "right") {
            // 右スワイプで気になる
            $('input[name=' + target_name + ']:eq(0)').prop('checked', true);

            // 右にスライド
            $('.one_form' + '.' + target_name).animate({
                left: '+=100vw'
            }, 400);

            // 揺らす
            setTimeout(function () {
                $('.kininaru_zone').css('right', '8vw');
            }, 300);
            setTimeout(function () {
                $('.kininaru_zone').css('right', '6vw');
            }, 500);

            // 分子の変更
            if (num2 == -1) {
                $("#submit_btn").delay(600).css('display', 'inline-block');
            } else {
                $(".now_num").text(num - num2);
                num2--;
            }
        } else {
            console.log("移動してません");
        }

        if (moveY == "top") {
            msgY = "上へ移動";
        } else if (moveY == "bottom") {
            msgY = "下へ移動";
        } else {
            msgY = "移動なし";
        }


    }


    // 座標取得関数
    function getY(event) {
        //縦方向の座標を取得
        return (event.originalEvent.touches[0].pageY);
    }

    function getX(event) {
        //横方向の座標を取得
        return (event.originalEvent.touches[0].pageX);
    }


    /* ボタンでの挙動 */
    $(".one_form").change(function () {
        var i = $(this).attr('id');

        $(this).delay(200).fadeOut();

        if (i == 1) {
            setTimeout(function () {
                $("#submit_btn").css('display', 'inline-block');
            }, 1000);
        } else {
            $(".now_num").text(Number(num) - i + 2);
        }
    })


})