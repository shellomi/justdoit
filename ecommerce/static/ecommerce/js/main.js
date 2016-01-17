function main() {
  $(".video-button").click(function(){
    $(".main-container").hide();
    $(".jumbotron").removeClass("my-jumbotron").addClass("jumbotron-video");
    $(".video-modal").show();
    var e = '<iframe class="video-player" src="https://www.youtube.com/embed/Y7aEiVwBAdk?autoplay=1&rel=0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>';
    $(".video-row").append(e);
    //$("#videoModal").modal('show');
  });

  $(".video-close-button").click(function(){
    $(".jumbotron").removeClass("jumbotron-video").addClass("my-jumbotron");
    $(".video-player").remove();
    $(".video-modal").hide();
    $(".main-container").show();
  });

  $(".dropdown").hover(function(){
    $("#dropdown"+$(this).attr("id")).removeClass("hidden");
  }, function(){
	  $("#dropdown"+$(this).attr("id")).addClass("hidden");
  });

  // $("#videoModal").on('show.bs.modal', function(){
  //   var e = '<iframe class="video-player" src="https://www.youtube.com/embed/Y7aEiVwBAdk?autoplay=1&rel=0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>';
  //   $("#videoDiv").append(e);
  // });
  // $("#videoModal").on('hide.bs.modal', function(){
  //   $(".video-player").remove();
  // })
}

// function autoPlayYouTubeModal() {
//     var trigger = $("body").find('[data-toggle="modal"]');
//     trigger.click(function () {
//         var theModal = $(this).data("target"),
//             videoSRC = $(this).attr("data-theVideo"),
//             videoSRCauto = videoSRC + "?autoplay=1";
//         $(theModal + ' iframe').attr('src', videoSRCauto);
//         $(theModal + ' button.close').click(function () {
//             $(theModal + ' iframe').attr('src', videoSRC);
//         });
//     });
//}

$(document).ready(main);
