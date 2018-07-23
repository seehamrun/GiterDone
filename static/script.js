fetch("http://api.worldweatheronline.com/premium/v1/weather.ashx?key=94349d6fea7e46ec9e1161044182307&q=&format=json&num_of_days=1&date=today")
  .then(function(response){
    response.json().then(function(data)){
      console.log(data);
      temp.innerHTML = "<h1>The current weather is" + data.DatabaseForCoolPeople
      condition.innerHTML = "<p>" + data.data.current_condition[0]
      pic.inner_
    }
  })
