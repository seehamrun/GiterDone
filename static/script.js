fetch("http://api.worldweatheronline.com/premium/v1/weather.ashx?key=94349d6fea7e46ec9e1161044182307&q=&format=json&num_of_days=1&date=today" + weather_key + "&q=93786&format=json&num_of_days=1")
  .then(function(response){
    response.json().then(function(data)){
      console.log(data);
      temp.innerHTML = "<h1>The current weather is" + data.data.current_condition[0].temp_F + "F<h1>"
      condition.innerHTML = "<p>" + data.data.current_condition[0]. weatherDesc[0]. value + "</p>"
    }
  })
