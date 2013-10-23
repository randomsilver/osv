// Cache selectors
var lastId,
    topMenu = $("#osv-navbar .nav"),
    topMenuHeight = topMenu.outerHeight()+15,
    // All list items
    menuItems = topMenu.find("a"),
    // Anchors corresponding to menu items
    scrollItems = menuItems.map(function(){
      var item = $($(this).attr("href"));
      if (item.length) { return item; }
    });

// Bind click handler to menu items
// so we can get a fancy scroll animation
menuItems.click(function(e){
  var href = $(this).attr("href"),
      offsetTop = href === "#" ? 0 : $(href).offset().top-topMenuHeight+1;
  $('html, body').stop().animate({
  scrollTop: offsetTop
  }, 300);
  e.preventDefault();
});

// Bind to scroll
$(window).scroll(function(){
   // Get container scroll position
   var fromTop = $(this).scrollTop()+topMenuHeight;
   
   // Get id of current scroll item
   var cur = scrollItems.map(function(){
     if ($(this).offset().top < fromTop)
       return this;
   });
   // Get the id of the current element
   cur = cur[cur.length-1];
   var id = cur && cur.length ? cur[0].id : "";
   
   if (lastId !== id) {
       lastId = id;
       // Set/remove active class
       menuItems
         .parent().removeClass("active")
         .end().filter("[href=#"+id+"]").parent().addClass("active");
   }
});
function gallery(){
  $('#ring1').click(function() { bootbox.alert('<img src="img/ring1.jpg"><h4>Fine silver ring with 24 carat gold embellishments</h4>'); });
  $('#ring2').click(function() { bootbox.alert('<img src="img/ring2.jpg"><h4>Fine silver ring, oxidised with 24 carat gold embellishments</h4>'); });
  $('#ring3').click(function() { bootbox.alert('<img src="img/ring3.jpg"><h4>Sterling silver adjustable ring, textured</h4>'); });
  $('#bracelet1').click(function() { bootbox.alert('<img src="img/bracelet1.jpg"><h4>Sterling Silver Half Persian 3-in-1 chainmaille bracelet</h4>'); });
  $('#ring4').click(function() { bootbox.alert('<img src="img/ring4.jpg"><h4>Fine silver ring, irregular edge, textured</h4>'); });
  $('#ring5').click(function() { bootbox.alert('<img src="img/ring5.jpg"><h4>Fine silver ring, irregular edge, textured</h4>'); });
  $('#earring1').click(function() { bootbox.alert('<img src="img/earring1.jpg"><h4>Fine silver earrings, textured</h4>'); });
  $('#earring2').click(function() { bootbox.alert('<img src="img/earring2.jpg"><h4>Fine silver earrings, textured</h4>'); });
  $('#ring6').click(function() { bootbox.alert('<img src="img/ring6.jpg"><h4>Fine silver ring, textured rectangular</h4>'); });
  $('#ring7').click(function() { bootbox.alert('<img src="img/ring7.jpg"><h4>Sterling silver adjustable ring, reticulated finish</h4>'); });
  $('#bracelet2').click(function() { bootbox.alert('<img src="img/bracelet2.jpg"><h4>Sterling silver Elf weave chain maille bracelet with Fine silver clasp</h4>'); });
  $('#ring8').click(function() { bootbox.alert('<img src="img/ring8.jpg"><h4>Fine silver ring, textured mid centre</h4>'); });
  $('#ring9').click(function() { bootbox.alert('<img src="img/ring9.jpg"><h4>Fine silver thick ring, heavily textured</h4>'); });
  $('#ring10').click(function() { bootbox.alert('<img src="img/ring10.jpg"><h4>Fine silver thick ring, heavily textured</h4>'); });
  $('#earring3').click(function() { bootbox.alert('<img src="img/earring3.jpg"><h4>Sterling silver free-form earrings</h4>'); });
  $('#earring4').click(function() { bootbox.alert('<img src="img/earring4.jpg"><h4>Fine silver, delicate drops, with 24 carat gold embellishments</h4>'); });
  $('#ring11').click(function() { bootbox.alert('<img src="img/ring11.jpg"><h4>Sterling silver adjustable ring, hammered texture</h4>'); });
  $('#ring12').click(function() { bootbox.alert('<img src="img/ring12.jpg"><h4>Fine silver ring, textured mid centre</h4>'); });
  $('#ring13').click(function() { bootbox.alert('<img src="img/ring13.jpg"><h4>Fine silver ring, textured rectangular</h4>'); });
  $('#earring5').click(function() { bootbox.alert('<img src="img/earring5.jpg"><h4>Sterling silver free-form earrings</h4>'); });
  $('#earring6').click(function() { bootbox.alert('<img src="img/earring6.jpg"><h4>Fine silver textured disc earrings</h4>'); });
  $('#earring7').click(function() { bootbox.alert('<img src="img/earring7.jpg"><h4>Fine silver long textured earrings</h4>'); });
  $('#earring8').click(function() { bootbox.alert('<img src="img/earring8.jpg"><h4>Fine silver large disc textured earrings</h4>'); });


}
var $itemsHolder = $('#gallery ul.thumbnails');
var $itemsClone = $itemsHolder.clone(); 
var $filterClass = "";
$('#gallery ul.filter li').click(function(e) {
e.preventDefault();
$(this).find('a').addClass('selected');
$filterClass = $(this).attr('data-value');
    if($filterClass == 'all'){ var $filters = $itemsClone.find('li'); }
    else { var $filters = $itemsClone.find('li[data-type='+ $filterClass +']'); }
    $itemsHolder.quicksand(
      $filters,
      { duration: 1000 },
      gallery
      );
});
$(document).ready(gallery);

$(document).ready(function(){

  var galleryLink = function(){
    $('#gallery a').on('click', function(e){
      $('html, body').animate({
        scrollTop: $("#gallery").offset().top - 50
    }, 1000);

    });
  };

  galleryLink();
});

// var offsetHeight = 51;

// $('.nav-collapse').scrollspy({
//     offset: offsetHeight
// });

$('.navbar li a').click(function (event) {
    var scrollPos = $('body > .container').find($(this).attr('href')).offset().top - offsetHeight;
    $('body,html').animate({
        scrollTop: scrollPos
    }, 500, function () {
        $(".btn-navbar").click();
    });
    return false;
});
