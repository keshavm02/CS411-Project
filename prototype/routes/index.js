const fetch = require('node-fetch');
const express = require('express');
const router = express.Router();
const CONFIG = require('../config/newsAPI');

router.route('/')
    .get(async (req, res, next) => {
      // let result = await fetch(CONFIG.url + '?q=boston&units=metric&appid=' + CONFIG.key);
      // let weather = await result.json();
      res.render('index');
    })
    .post(async (req, res, next) => {
        console.log(CONFIG.url);
      let result = await fetch(CONFIG.url + '?sources=' + req.body.news_outlet + '&apiKey=' + CONFIG.key);
      try {
        let newsResult = await result.json();
        res.render('news', {title: `Headline from ${req.body.news_outlet}:`, author: newsResult.articles[0].author, headline: newsResult.articles[0].title, link: newsResult.articles[0].url, body: newsResult.articles[0].description});
      } catch {
        res.status(400);
        res.render('wrongName');
      }
    })


module.exports = router;
