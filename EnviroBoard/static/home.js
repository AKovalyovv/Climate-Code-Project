alert('The home.js file has been loaded')

function initialize() {
	fetch("http://127.0.0.1:5000/getjobs", {
		method: 'GET'
	})
	.then(response => {
		return response.text().then(text => alert(text))
	})
}

window.onload = initialize();