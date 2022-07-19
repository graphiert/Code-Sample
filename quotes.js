const axios = require("axios")
const getQuote = () => {
  const apiEndpoint = "https://api.quotable.io/random";
  const params = { minLength: 5, maxLength: 65 };
  axios.get(apiEndpoint, { params })
    .then(res => res.data.content)
    .then(res => console.log(res)); // Do anything
};
