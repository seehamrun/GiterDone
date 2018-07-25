fetch("http://api.worldweatheronline.com/premium/v1/weather.ashx?key=" + weatherApi + "&q=60607&format=json&num_of_days=1")
  .then(function(response){
    response.json().then(function(data){
      console.log(data);
      currentTemp = data.data.current_condition[0].temp_F
      temp.innerHTML = "<h1>The current weather is " + currentTemp + "F<h1>"
      condition.innerHTML = "<p>" + data.data.current_condition[0].weatherDesc[0].value + "</p>"
      pic.innerHTML = "<img src='" + data.data.current_condition[0].weatherIconUrl[0].value + "'/>"
      jQuery.get("/schedule?temp=" + temp, () => {
      })
    })
  });
var checkedDiv = document.querySelectorAll('.checked');
var cool = 12
var times = ["10AM", "12PM", "2PM", "4PM", "6PM"]
console.log(checkedDiv)
var i = 0;
checkedDiv.forEach(function(element) {
  var inputSchedule = document.createElement('input');
    inputSchedule.type = 'checkbox';
    //make the 5 individual labels to sync to the html
    inputSchedule.innerHTML = 'I have drank ${cool}oz by ${times[i]}';
  element.appendChild(inputSchedule);
  i++;
});

//"<input type='checkbox'>I have drank"+ %s +"oz by 10AM<br>" % (12)
  // fetch("http://api.apixu.com/v1/current.json?key=" + weatherApi + "&q=60607")
  //   .then(function(response){
  //     response.json().then(function(data){
  //       console.log(data);
  //
  //     });
  //   })



  function addWaterDatabase(waterdatabaseUrl, doneCallback) {
    jQuery.post("/history", {url: waterdatabaseUrl}, doneCallback);
  }

  function submitHistory() {
    var inputBox = document.getElementById('historyform')
    //{var data= }
    var userInput = userInput + inputBox.value
    addWaterDatabase(userInput, displayResult)
  }




  window.addEventListener('load', () => {
    document.querySelector('#submit').addEventListener("click", submitClick)

  });
