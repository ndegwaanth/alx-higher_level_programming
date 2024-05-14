$.get('https://swapi.co/api/films/?format=json', function (data) {
	let episodes = data.results;
	$.each(episodes, function (episode.title) {
		$('#list_movies').append('<li>' + episode.title + '</li>');
	});
});
