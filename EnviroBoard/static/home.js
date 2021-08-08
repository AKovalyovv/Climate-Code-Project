alert('The home.js file has been loaded');
var jobs = [];

function initialize() {
	fetch("http://127.0.0.1:5000/getjobs", {
		method: 'GET'
	})
	.then(response => response.json())
	.then(responseJson => {
		jobs = responseJson;
		console.log(jobs);
		console.log(jobs[0]);
	});
}

window.onload = initialize();