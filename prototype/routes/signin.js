var express = require("express");
var router = express.Router();

/* GET users listing. */
router.route("/").get(async (req, res, next) => {
  res.render("signin");
});

module.exports = router;
