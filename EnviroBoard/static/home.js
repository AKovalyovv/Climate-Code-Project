// alert('The home.js file has been loaded');
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
	})
	.then(() => {
		renderAllJobs();
	});
}

function renderAllJobs() {
	var ul = document.getElementById("row");
	jobs.forEach(job => {
			ul.appendChild(createListItem(job));
	});
}

/* Constructs this html element and returns it:
<a href="http://google.ca/">
	<div class="column">
		<h2>Job Name</h2>
		<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sit amet pretium urna. Vivamus venenatis velit nec neque ultricies, eget elementum magna tristique. Quisque vehicula, risus eget aliquam placerat, purus leo tincidunt eros, eget luctus quam orci in velit. Praesent scelerisque tortor sed accumsan convallis.</p>
		<p>Location</p>
	</div>
</a>
*/
function createListItem(job) {
	var wrapper = document.createElement('a');
	wrapper.href = job.link;
	var div = document.createElement('div');
	div.className = "column";
	var jobName = document.createElement('h2');
	jobName.textContent = job.name;
	var description = document.createElement('p');
	description.textContent = job.organization;
	var location = document.createElement('p');
	location.textContent = job.location;

	div.appendChild(jobName);
	div.appendChild(description);
	div.appendChild(location);
	wrapper.appendChild(div);

	return wrapper;
}

/*
	Pulls jobs based on the location
	1. Clear the ul
	2. Filter jobs list and return list of jobs that match location
	3. Use createListItem() to re-render job list
*/

function input() {
	return document.getElementById("fname").value;
}

function submitForm() {
	console.log("form was submitted");
	var userInput = input();
	document.getElementById("row").innerHTML = "";

	if (input == "") {
		renderAllJobs();
	} else {
		var ul = document.getElementById("row");
		jobs.filter( job => {
			console.log(job.location)
			if (job.location.includes(userInput)) {
				ul.appendChild(createListItem(job));
			}
		})
	}

	console.log(userInput);
	return false;
}

window.onload = initialize();