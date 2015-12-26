function main() {
  $(".video-button").click(function(){
    $(".main-container").hide();
    $(".jumbotron").removeClass("my-jumbotron").addClass("jumbotron-video");
    $(".video-modal").show();
    var e = '<iframe class="video-player" src="https://www.youtube.com/embed/Y7aEiVwBAdk?autoplay=1&rel=0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>';
    $(".video-row").append(e);
  });

  $(".video-close-button").click(function(){
    $(".jumbotron").removeClass("jumbotron-video").addClass("my-jumbotron");
    $(".video-player").remove();
    $(".video-modal").hide();
    $(".main-container").show();
  });
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
