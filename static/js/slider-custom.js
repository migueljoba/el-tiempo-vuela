$sliderTrigger = $('#slider-trigger');
$sliderTrigger.click(function() {

	$containerAgenda = $('#container-agenda')
	$containerAgenda.addClass('d-none');

	$containerAgendaImages = $('#container-agenda-images');
	$containerAgendaImages.removeClass('d-none');

	myLoop();
});

function requestImage() {
	 $.ajax({
			 url: '/rand_filename',
			 dataType: 'json',
			 success: function(data) {
					console.log(data);
					// preparar nueva imagen
					var $newImg = $('<img>', {src:data.media_url, class:'w-100'});
					$newImg.css('display', 'none');

					var $container = $('#container-dynamic-img');
					
					$container.find('img').fadeOut(1000, function() {
						$(this).remove();
						$container.append($newImg);
						$newImg.fadeIn(1000);
					});          
			 }
	 });
}

function myLoop() {
	setTimeout(function() {
		requestImage();
			myLoop();
	}, slideDuration);
}