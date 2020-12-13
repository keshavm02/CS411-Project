const fetch = require('node-fetch');
const express = require('express');
const router = express.Router();
const CONFIG_newsAPI = require('../config/newsAPI');
const CONFIG_diffbotAPI = require('../config/diffbotAPI');

router.route('/')
    .get(async (req, res, next) => {
      // let result = await fetch(CONFIG.url + '?q=boston&units=metric&appid=' + CONFIG.key);
      // let weather = await result.json();
      res.render('index');
    })
    .post(async (req, res, next) => {
        console.log(CONFIG_newsAPI.url);
      let newsAPI_result = await fetch(CONFIG_newsAPI.url + '?sources=' + req.body.news_outlet + '&apiKey=' + CONFIG_newsAPI.key);
      try {
        let newsResult = await newsAPI_result.json();
        const articleUrl = newsResult.articles[0].url;
        console.log(`articleUrl = ${articleUrl}`);
        let diffbotAPI_result = await fetch(CONFIG_diffbotAPI.url + '?token=' + CONFIG_diffbotAPI.token + '&url=' + articleUrl);
        try {
            let diffbotResult = await diffbotAPI_result.json();
            console.log(`got diff bot result ${diffbotResult.objects[0].author}`);
            res.render('news', {title: `Headline from ${req.body.news_outlet}:`, source: newsResult.articles[0].author, author: diffbotResult.objects[0].author, headline: newsResult.articles[0].title, link: newsResult.articles[0].url, body: newsResult.articles[0].description});
        } catch (error) {
            res.status(400);
            res.render('error');
        }
      } catch (error) {
        res.status(400);
        res.render('wrongName');
      }
    })


module.exports = router;
