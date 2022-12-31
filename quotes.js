// With NodeJS
const { request } = require("http");
const getQuote = () => {
  request({
    host: "api.quotable.io",
    path: "/random?maxLength=65"
  }, res => {
    let value;
    res.on('data', stuff => {
      let conc = Buffer.concat([stuff]);
      let fromStr = conc.toString("utf-8");
      value = JSON.parse(fromStr).content;
    });
    res.on('end', () => console.log(value)); // Do anything
  }).end();
};

// With Web API
const getQuote = () => {
  fetch("https://api.quotable.io/random?maxLength=65")
  .then(res => res.json())
  .then(res => {
    let data = data.content;
    console.log(data); // Do anything
  });
};
