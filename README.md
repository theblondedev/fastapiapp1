🧠 Online Psychological Profiling App (FastAPI)

This project is a FastAPI-based web application that generates a light-hearted “psychological profile” of a user based on form input. The system acts as both a server and a client, integrating with multiple third-party REST APIs to enrich the generated profile.

🚀 Project Overview

Users submit personal data through a web form. The backend then:

Stores the submitted data
Performs a simple “psychological” analysis (creative/experimental logic)
Fetches external data from third-party APIs (movies + animal images)
Generates a profile that is later displayed through the frontend SPA

The frontend communicates only with the backend server, which handles all external API calls.

🔐 Authentication
The entire application is protected using Basic HTTP Authentication
Username and password are both your 8-digit student ID

Example:

Username: 12345678  
Password: 12345678
🧩 Backend (FastAPI)

The backend provides the following endpoints:

/
Serves the main landing page (index.html)
Acts as the Single Page Application (SPA entry point)
/form
Returns an HTML form fragment (psycho.html)
Injected into the frontend dynamically
/submit
Receives form data from the client
Stores data on the server
Returns a success message
/analyze
Processes submitted form data
Generates a “psychological profile”
Includes:
Career suitability assessment
Movie recommendations (via OMDb API)
Random pet images based on selected animals (Dog/Cat/Duck APIs)
Stores results server-side (does not return full data to client)
/view/input
Returns stored user input (JSON format)
/view/profile
Returns generated psychological profile (JSON format)
🎭 Frontend (Single Page Application)

The frontend (index.html) acts as a control panel and SPA interface:

Key Features:
Dynamically loads form from /form
Submits user input to /submit
Fetches and displays:
Stored input data (/view/input)
Psychological profile (/view/profile)
Pet images from external APIs (via backend)
Uses JavaScript (or TypeScript) for dynamic interactions
Styled using CSS for clean UI presentation
Requirements:
Must not display raw JSON directly
Must parse and render data in a user-friendly format
Must behave as a Single Page Application
🌐 Third-Party APIs Used
🎬 Movie Recommendations (OMDb API)
Used to fetch movie data based on user profile
Example:
http://www.omdbapi.com/?apikey=YOUR_KEY&t=alien
🐶🐱🦆 Random Animal Images
Dog: https://dog.ceo/api/breeds/image/random
Cat: https://api.thecatapi.com/v1/images/search
Duck: https://random-d.uk/api/v2/random

Used to assign random pet images based on user selections.

🐳 Deployment
The entire application must be packaged as a Docker image
Runs inside a Docker container for submission
📦 Submission
Submit the saved Docker image as required by course instructions
Due: April 1, 2026 (11:55 PM)
Worth: 25% of final grade
🧠 Key Learning Outcomes
Building RESTful APIs with FastAPI
Server-side data processing and storage
Consuming third-party APIs
SPA frontend design with JavaScript
Authentication using HTTP Basic Auth
Docker containerisation
Full-stack architecture design
