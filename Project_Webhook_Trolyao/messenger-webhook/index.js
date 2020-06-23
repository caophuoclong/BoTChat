'use strict';

// Imports dependencies and set up http server
const
  express = require('express'),
  bodyParser = require('body-parser'),
  app = express().use(bodyParser.json()); // creates express http server

// Sets server port and logs message on success
app.listen(process.env.PORT || 1337, () => console.log('webhook is listening'));

// Creates the endpoint for our webhook 
app.post('/webhook', function(req, res) {
    var entries = req.body.entry;
    for (var entry of entries) {
      var messaging = entry.messaging;
      for (var message of messaging) {
        var senderId = message.sender.id;
        if (message.message) {
          // If user send text
          if (message.message.text) {
            var text = message.message.text;
            console.log(text); 
            sendMessage(senderId,"Long dep traai")
        }
            
          }
        }
    }
});
function sendMessage(senderId, message) {
    request({
      url: 'https://graph.facebook.com/v2.6/me/messages',
      qs: {
        access_token: "EAAHPTZBQbRLABAIK9B7hqMpIVa6yPLPVp5mIbZAq6kZAoZCf86MKP7ZAfRxirM0GyBG35Eugp427XzoUxwkd7VMFNjDrweXFZBVw1vaja2VHixnnL6dTbOyzd9kk4jJQKg6RQ66k6tpgM8nODSsosQ0YlyPx8TYAoCz5PkadNB2xXB2ZANV6ZB7K",
      },
      method: 'POST',
      json: {
        recipient: {
          id: senderId
        },
        message: {
          text: message
        },
      }
    });
  }
  // Adds support for GET requests to our webhook
app.get('/webhook', (req, res) => {

    // Your verify token. Should be a random string.
    let VERIFY_TOKEN = "26032001"
      
    // Parse the query params
    let mode = req.query['hub.mode'];
    let token = req.query['hub.verify_token'];
    let challenge = req.query['hub.challenge'];
      
    // Checks if a token and mode is in the query string of the request
    if (mode && token) {
    
      // Checks the mode and token sent is correct
      if (mode === 'subscribe' && token === VERIFY_TOKEN) {
        
        // Responds with the challenge token from the request
        console.log('WEBHOOK_VERIFIED');
        res.status(200).send(challenge);
      
      } else {
        // Responds with '403 Forbidden' if verify tokens do not match
        res.sendStatus(403);      
      }
    }
  });