fetch("http://api.worldweatheronline.com/premium/v1/weather.ashx?key=" + weatherApi + "&q=60607&format=json&num_of_days=1")
  .then(function(response){
    response.json().then(function(data){
      console.log(data);
      temp = data.data.current_condition[0].temp_F
      temp.innerHTML = "<h1>The current weather is " + temp + "F<h1>"
      condition.innerHTML = "<p>" + data.data.current_condition[0].weatherDesc[0].value + "</p>"
      pic.innerHTML = "<img src='" + data.data.current_condition[0].weatherIconUrl[0].value + "'/>"
      jQuery.get("/schedule?temp=" + temp, () => {
        alert("saved")
      })
    })
  });
var checkedDiv = document.querySelector('#checked');
var cool = 12
var inputSchedule = `<input type='checkbox'>I have drank ${cool} oz by 10AM<br>`
console.log(checkedDiv);
checkedDiv.innerHTML = inputSchedule;


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

  function submitClick() {
    var inputBox = document.querySelector('#queryBox')
    var userInput = userInput + inputBox.value
    addWaterDatabase(userInput, displayResult)
  }


  window.addEventListener('load', () => {
    document.querySelector('#submit').addEventListener("click", submitClick)

  });
