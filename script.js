const http = require('http');
const fs = require('fs');
const path = require('path');

const server = http.createServer((req, res) => {
    if (req.url === '/home' || req.url === 'index.html') {
        // Load the HTML file
        fs.readFile(path.join(__dirname, '/index.html'), (err, data) => {
            if (err) {
                res.writeHead(500);
                return res.end('Error loading index.html');
            }

            // Set the content type
            res.writeHead(200, { 'Content-Type': 'text/html' });

            // Send the HTML file
            res.end(data);
        });
    } else if (req.url === '/style.css') {
        // Load the CSS file
        fs.readFile(path.join(__dirname, '/style.css'), (err, data) => {
            if (err) {
                res.writeHead(500);
                return res.end('Error loading style.css');
            }

            // Set the content type
            res.writeHead(200, { 'Content-Type': 'text/css' });

            // Send the CSS file
            res.end(data);
        });
    } else if (req.url === '/index.js') {
        // Load the CSS file
        fs.readFile(path.join(__dirname, '/index.js'), (err, data) => {
            if (err) {
                res.writeHead(500);
                return res.end('Error loading index.js');
            }

            // Set the content type
            res.writeHead(200, { 'Content-Type': 'application/javascript' });

            // Send the JS file
            res.end(data);
        });
    } else if (req.url === '/languages.js') {
        // Load the CSS file
        fs.readFile(path.join(__dirname, '/languages.js'), (err, data) => {
            if (err) {
                res.writeHead(500);
                return res.end('Error loading languages.js');
            }

            // Set the content type
            res.writeHead(200, { 'Content-Type': 'application/javascript' });

            // Send the JS file
            res.end(data);
        });    

    } else {
        // Handle 404 - Not Found
        res.writeHead(404);
        res.end('Not Found');
    }
});

const port = 3000;
server.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});