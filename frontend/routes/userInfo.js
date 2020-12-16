var express = require("express");
var router = express.Router();

router.route("/")
    .get(async (req, res, next) => {
      res.render('index');
    })
    .post(async (req, res, next) => {
      try {
          console.log(req.body);
        let firstName = req.body.first_name;
        let userName = req.body.username;
        let fav_orgs = req.body.fav_orgs;
        res.render('userInfo', {firstName: firstName, fav_orgs: fav_orgs});
      } catch (error) {
        res.status(400);
        res.render('error');
      }

    })

module.exports = router;
