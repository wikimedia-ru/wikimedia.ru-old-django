function donate_block_run(id) {
	var block = $('#donate-' + id);
	if (block.length == 0) {
		$('#donations>li').removeClass('active');
		return;
	}
	if (block.hasClass('active')) {
		$('#donate-' + id).removeClass('active');
		if (window.location.hash != '#' + id) {
			window.location.hash = '';
		}
	}
	else {
		$('#donations>li').removeClass('active');
		$('#donate-' + id).addClass('active');
	}
}

function donate_block(id) {
	if (window.location.hash != '#' + id) {
		window.location.hash = '#' + id;
		if ('onhashchange' in window) {
			return;
		}
		donate_block_run(id);
	}
	else {
		window.location.hash = '';
		if ('onhashchange' in window) {
			return;
		}
		donate_block_run('');
	}
}

function donate_hash_change() {
	donate_block_run(window.location.hash.replace('#', ''));
}

$(document).ready(function() {
	if (window.location.pathname == '/donations') {
		if ('onhashchange' in window) {
			window.onhashchange = donate_hash_change;
		}
		donate_block_run(window.location.hash.replace('#', ''));
	}
});

