var express = require("express");
var router = express.Router();

/* GET users listing. */
router.route("/").get(async (req, res, next) => {

    // res.render("signin");
    var url = 'localhost:8000/login/google-oauth2/';
    var data = {username: 'unknown'};
    fetch(url, {
        method: 'POST', // or 'PUT'
        body: JSON.stringify(data), // data can be `string` or {object}!
        headers:{
            'Content-Type': 'application/json'
        }
    }).then(res => res.json())
        .then(response => console.log('Success:', JSON.stringify(response)))
        .catch(error => console.error('Error:', error));
});

module.exports = router;
