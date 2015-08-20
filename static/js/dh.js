 

$(document).ready(function(){
	$(".pinned").pin({containerSelector: "body"});
	
	var userAgent = window.navigator.userAgent;
	if(userAgent.indexOf("MSIE 7.0")>0 || (userAgent.indexOf("MSIE 8.0")>0 && !window.innerWidth)){ } else {
		var scrollTimeout = null;
		window.onscroll = function(){
			clearTimeout(scrollTimeout);
			scrollTimeout = setTimeout(function(){
				$.nav_autofocus();
			},20);
		}
	}
	
	$('.back-top').hide();
	$('.back-top').click(function(){$.scrollTop();});
	
	
	$(".top-reading ul li").click(function(){
		$(this).children(".read-title").children("a").attr("target","_blank");
		var url = $(this).children(".read-title").children("a").attr("href");
		window.open(url);
	});
	
	
	$("img").lazyload({
		effect: "fadeIn",
		failurelimit:20
	});

	
	$.ctrlbar_fix();
	$(window).resize(function() {
		$.ctrlbar_fix();
	});
	
	$(".setting").mouseover(function(){
	   $(this).children("a").children("img").attr("src","images/site_setting1.gif");
	}).mouseout(function(){
	   $(this).children("a").children("img").attr("src","images/site_setting0.gif");
	});

});




$.extend({
	topArr : [
			$(".floor_1").offset().top - 40,
			$(".floor_2").offset().top - 40,
			$(".floor_3").offset().top - 40,
			$(".floor_4").offset().top - 40,
			$(".floor_5").offset().top - 40,
			$(".floor_6").offset().top - 40
	],
	nav_fix : function(_selector){
		var $e = $(_selector);
		var offset = $e.offset();
		$('html,body').animate({scrollTop: (offset.top - 55) + 'px'}, 300);
	},
	nav_autofocus : function(){
		var topArr = this.topArr;
		var currScrollTop = $(window).scrollTop();
		var $nav_a = $(".nav-list ul li a");
		if(currScrollTop < topArr[0]){
			$nav_a.removeClass("active");
			$nav_a.eq(0).addClass("active");
		}else if(currScrollTop < topArr[1]){
			$nav_a.removeClass("active");
			$nav_a.eq(1).addClass("active");
		}else if(currScrollTop < topArr[2]){
			$nav_a.removeClass("active");
			$nav_a.eq(2).addClass("active");
		}else if(currScrollTop < topArr[3]){
			$nav_a.removeClass("active");
			$nav_a.eq(3).addClass("active");
		}else if(currScrollTop < topArr[4]){
			$nav_a.removeClass("active");
			$nav_a.eq(4).addClass("active");
		}else if(currScrollTop < topArr[5]){
			$nav_a.removeClass("active");
			$nav_a.eq(5).addClass("active");
		}else if(currScrollTop < topArr[6]){
			$nav_a.removeClass("active");
			$nav_a.eq(6).addClass("active");
		}else {
			
		}
		if(currScrollTop < topArr[0] - 50){
			$(".back-top").fadeOut(500);
		}else {
			$(".back-top").fadeIn(500);
		}
	},
	ctrlbar_fix: function(){
		var w = document.body.clientWidth;
		var h = $(window).height();
		$(".back-top").css(
			{
				"left":w - (w - 1050)/2 + 10 + "px",
				"top": h - 100 + "px"
			}
		);
		//$(".back-top").fadeIn(2000);
	},
	scrollTop : function(){
		$('html,body').animate({scrollTop: '0px'}, 400);
	},
	scrollDown : function(){
		$('html,body').animate({scrollTop: '11110px'}, 400);
	}
});
