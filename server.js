const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Database connection
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '', // Your MySQL password
  database: process.env.DB_DATABASE // Your database name
});

db.connect((err) => {
  if (err) throw err;
  console.log('Connected to MySQL Database!');
});

// Serve static files
app.use(express.static('public'));

// Handle Sign In request
app.post('/signin', (req, res) => {
  const { userId, password } = req.body;

  if (!userId || !password) {
    return res.status(400).send('User ID and password are required.');
  }

  // Query to check if user exists and password matches
  const query = 'SELECT * FROM users WHERE user_id = ? AND password = ?';
  db.query(query, [userId, password], (err, results) => {
    if (err) throw err;

    if (results.length > 0) {
      res.status(200).send('Login Successful!');
      // Redirect to admin dashboard or other user pages based on role
    } else {
      res.status(401).send('Invalid User ID or Password.');
    }
  });
});

// Start server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
