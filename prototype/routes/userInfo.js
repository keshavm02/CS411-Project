var express = require('express');
var router = express.Router();

router.route('/')
    .get(async (req, res, next) => {
        res.render('index');
    })
    .post(async (req, res, next) => {

    })

module.exports = router;
