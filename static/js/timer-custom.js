var startValuesOptions = {
	seconds: 0,
	minutes: 0,
	hours: 0,
};

$('.input-number').change(function() {
	$this = $(this);
	let prop = $this.attr('data');
	startValuesOptions[prop] = parseInt($this.val());
	console.log(startValuesOptions);
});


var timer = new Timer();

$('#countdown .startButton').click(function () {
	timer.start({
		countdown: true,
		startValues: startValuesOptions,
	});
});

$('#countdown .pauseButton').click(function () {
	timer.pause();
});

$('#countdown .stopButton').click(function () {
	timer.stop();
});

$('#countdown .resetButton').click(function () {
	$('.countdown-number').html('--');
	timer.reset();
});

timer.addEventListener('secondsUpdated', function (e) {
	let hours = timer.getTimeValues().hours;
	let minutes = timer.getTimeValues().minutes;
	let seconds = timer.getTimeValues().seconds;

	$('#countdown-hours').html(hours);
	$('#countdown-minutes').html(minutes);
	$('#countdown-seconds').html(seconds);

	if (hours == 0 && minutes == 0 && seconds <= 10) {
		document.getElementById('flute').load();
		document.getElementById('flute').play();
	}
});

timer.addEventListener('started', function (e) {
    $('#chronoExample .values').html(timer.getTimeValues().toString());
});

timer.addEventListener('reset', function (e) {
    $('#chronoExample .values').html(timer.getTimeValues().toString());
});

timer.addEventListener('targetAchieved', function (e) {
	document.getElementById('clock-alarm2').play();
});