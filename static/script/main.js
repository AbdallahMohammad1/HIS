box2 =document.getElementById("box2");
box3 =document.getElementById("box3");

window.onload =function(){
    setTimeout(function(){
        box2.style.visibility='visible';
        box2.classList.add("animate__zoomIn")
    },1000);
    setTimeout(function(){
        box3.style.visibility='visible';
        box3.classList.add("animate__zoomIn")
    },2000);
}
$(function(){
    'use strict';
    $('[placeholder]').focus(function(){
        $(this).attr('data-text',$(this).attr('placeholder'));
        $(this).attr('placeholder','');
    }).blur(function(){
        $(this).attr('placeholder',$(this).attr('data-text'));
    });
    $('input').each(function(){    //add asterisk
        if($(this).attr('required')==='required'){
            $(this).after("<span class='asterisk'> * </span>");
        }
    }); 
    var show_field = $(".password");
    $(".show-pass").hover(function(){
        show_field.attr('type','text');
    },function(){
        show_field.attr('type','password');
    });
    $("#confirm").click(function(){
        return confirm("Are You Sure?");
    });

    $('.toggle-info').click(function(){
        console.log("Yes");
        $(this).toggleClass("selected").parent().next(".panel-body").fadeToggle(200);
        if($(this).hasClass("selected")){
            $(this).html("<i class='fas fa-plus'></i>");
        }else{
            $(this).html("<i class='fas fa-minus'></i>");
        }
    });
    function keyUp($input,$class){
        $($input).on("keyup",function(){
            $($class).text($(this).val());
        });
    }
    keyUp(".live-name",".live-ad .caption h5");
    keyUp(".live-desc",".live-ad .caption p");
    keyUp(".live-price",".live-ad .price_tag");
    keyUp(".live-country",".live-ad .caption .country-tag");

    
    $(".live-name").on("keyup",function(){
        $(".live-ad .caption h5").text($(this).val());
    });
    $(".heart").click(function(){
        $(this).toggleClass("like");
        if($(this).hasClass("like")){
            $(this).html("<i class='fas fa-heart heart2'></i>");
        }else{
            $(this).html("<i class='far fa-heart heart2'></i>");
        }
    })
    $(".heart3").click(function(){
        $(this).toggleClass("like");
        if($(this).hasClass("like")){
            $(this).html("<i class='fas fa-heart heart2'></i>");
        }else{
            $(this).html("<i class='far fa-heart heart2'></i>");
        }
    })
    $(".errorMsg").click(function(e){
        e.preventDefault();
        $(".Msg").fadeIn();
    });
    $(".Msg").click(function(){
        $(this).fadeOut();
    });
    $(".imgWish").mouseover(function(){
        $(".Msg2").fadeIn();
    });
    $(".imgWish").mouseleave(function(){
        $(".Msg2").fadeOut();
    });
    
}); 