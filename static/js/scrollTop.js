  
  $(function(){
    $(window).scroll(function(){  //jquery的scroll()方法
      if($(this).scrollTop()>200)
        {$("#gotobg").fadeIn(500);}  //jquery的fadeIn()显示方法
      else
        {$("#gotobg").fadeOut(300);}  //jquery的fadeIn()隐藏方法
    })

    $("#gotobg").mouseover(function(){$(this).css("background-position","-50px 0");});
    $("#gotobg").mouseout(function(){$(this).css("background-position","0 0");});
    $("#gotobg").click(function(){$("html,body").animate({scrollTop:0},"fast");return false;});  //animate()是jquery的动画
  });