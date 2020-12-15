var express = require("express");
var router = express.Router();

router.route("/").get(async (req, res, next) => {
  res.render("userInfo");
});
//   .post(async (req, res, next) => {});

module.exports = router;
