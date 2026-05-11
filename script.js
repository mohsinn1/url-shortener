// 1. Get references to your input, button, and result div

const input_field = document.getElementById("url-input")
const button = document.getElementById("shorten-btn")
const result = document.getElementById("result")



// 2. Add an event listener to the button



button.addEventListener('click', () => {
    const url = document.querySelector('#url-input').value; //    - Grab the value from the input field
    console.log(`sending ${url} to backend`);

    // Automatically detect if you are running locally or in production
    const isLocal = window.location.hostname === "127.0.0.1" || window.location.hostname === "localhost" || window.location.protocol === "file:";
    
    // Because we are hosting both on Vercel, the production URL is just the same domain! (empty string means relative path)
    const BACKEND_URL = isLocal ? "http://127.0.0.1:8000" : "";

    fetch(`${BACKEND_URL}/shorten`, { // 3. Make a POST request using fetch()
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ url: url })
    }).then(response => response.json()) // 4. Wait for the response, convert it to text/JSON 
        .then(data => {
            console.log('backend replied with', data)
            const result = document.getElementById('result')
            result.innerHTML = `
                <div class="result-label">Your Short Link</div>
                <p>${data}</p>
            `; // 5. Display the newly created short link inside your result div!
        })



})







