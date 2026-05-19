function fetch_form() {
    fetch('/form')
        .then(response => response.text())

        .then(html => {
      const formContainer = document.getElementById('form-container');
formContainer.innerHTML = html;
formContainer.style.display = 'block';

                         const submitBtn = document.getElementById('submitButton');
                          if (submitBtn) {
                submitBtn.style.display = 'inline-block';
            } else {
                console.error('Submit button not found!');
            }

                     const inputContainer = document.getElementById('inputData');
            const profileContainer = document.getElementById('profileData');
            if (inputContainer) inputContainer.style.display = 'none';
            if (profileContainer) profileContainer.style.display = 'none';
        })
        .catch(err => console.error('Error loading form:', err));
}

function submit_form() {
    const form = document.forms["psychoform"];
    const formData = new FormData(form);
    const data = {};

    // convert JSON
    formData.forEach((value, key) => {

        if (data[key]) {
            if (!Array.isArray(data[key])) data[key] = [data[key]];
            data[key].push(value);
        } else {
            data[key] = value;
        }
    });

    // convert to integers
    for (let i = 1; i <= 20; i++) {
        const q = "question" + i;
        if (data[q]) data[q] = parseInt(data[q]);
    }
    if (data["birthyear"]) data["birthyear"] = parseInt(data["birthyear"]);

    // array incase multiple selected
    if (data["pets"] && !Array.isArray(data["pets"])) data["pets"] = [data["pets"]];

    fetch("/submit", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    })
   .then(async res => {
    let message;

    try {
        const data = await res.json();
        message = data.message || JSON.stringify(data);
    } catch {
        message = await res.text();
    }

    alert(message);

        // hide the form and submit button for ux between tabs
        form.style.display = "none";
        document.getElementById("submitButton").style.display = "none";
    })
    .catch(err => console.error(err));
}

function analyze() {
    fetch('/analyze')
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        })
        .catch(err => console.error('Error running analysis try again', err));
}





async function viewInput() {
        const container = document.getElementById("inputData");
  try {
        const response = await fetch("/view/input");
        const data = await response.json();

        //view for taks to view in human readable viewing html in text
        let html = "<h3>Stored Input Data</h3>";

        html += `<p><strong>Name:</strong> ${data.name}</p>`;
        html += `<p><strong>Gender:</strong> ${data.gender}</p>`;
        html += `<p><strong>Birthyear:</strong> ${data.birthyear}</p>`;
        html += `<p><strong>Birthplace:</strong> ${data.birthplace}</p>`;
        html += `<p><strong>Residence:</strong> ${data.residence}</p>`;
        html += `<p><strong>Job:</strong> ${data.job}</p>`;
        html += `<p><strong>Pets:</strong> ${data.pets ? data.pets.join(", ") : "None"}</p>`;
        html += `<p><strong>Message:</strong> ${data.message.trim()}</p>`;


        html += "<h4>Question Responses:</h4><ul>";
        for (let i = 1; i <= 20; i++) {
            const qKey = "question" + i;
            if (data[qKey] !== undefined) {
                html += `<li><strong>Question ${i}:</strong> ${data[qKey]}</li>`;
            }
        }
        html += "</ul>";

        container.innerHTML = html;
        container.style.display = "block";
         const formContainer = document.getElementById('form-container');
        const submitBtn = document.getElementById('submitButton');
        if (formContainer) formContainer.style.display = 'none';
        if (submitBtn) submitBtn.style.display = 'none';

        // hide profile for ux
        const profileContainer = document.getElementById('profileData');
        if (profileContainer) profileContainer.style.display = 'none';



    } catch (err) {
        console.error(err);
        container.textContent = "Failed to load input data.";
        container.style.display = "block";
    }
}



async function view_profile() {
    const container = document.getElementById("profileData");

    try {
        const response = await fetch("/view/profile");
        const data = await response.json();

        // Build human-readable view
        let html = "<h3>User Profile</h3>";

       html += `<p><strong>Recommended Career:</strong> ${data.career}</p>`;
        html += `<p><strong>Score:</strong> ${data.score}</p>`;

        // Answers
        if (data["answers questions"]) {
            html += "<h4>Answered Questions:</h4><ul>";
            for (const key in data["answers questions"]) {
                html += `<li><strong>${key}:</strong> ${data["answers questions"][key]}</li>`;
            }
            html += "</ul>";
        }

        // Movies
        if (data.movies && data.movies.length > 0) {
            html += "<h4>Recommended Movies:</h4>";
            data.movies.forEach(movie => {
                html += `
                    <div style="margin-bottom:15px;">
                        <p><strong>${movie.Title}</strong> (${movie.Year})</p>
                        <p><em>${movie.Genre}'Genre'</em></p>
                        <p>${movie.Plot}</p>
                    </div>
                `;
            });
        }

        container.innerHTML = html;
        container.style.display = "block"; // show only when button pressed
document.getElementById('form-container').style.display = 'none';
        document.getElementById('submitButton').style.display = 'none';
        document.getElementById('inputData').style.display = 'none'
    } catch (err) {
        console.error(err);
        container.textContent = "Failed to load profile data.";
        container.style.display = "block";
    }
}