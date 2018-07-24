fetch("http://api.worldweatheronline.com/premium/v1/weather.ashx?key=" + weatherApi + "&q=60607&format=json&num_of_days=1")
  .then(function(response){
    response.json().then(function(data){
      console.log(data);
      currentTemp = data.data.current_condition[0].temp_F
      temp.innerHTML = "<h1>The current weather is " + currentTemp + "F<h1>"
      condition.innerHTML = "<p>" + data.data.current_condition[0].weatherDesc[0].value + "</p>"
      pic.innerHTML = "<img src='" + data.data.current_condition[0].weatherIconUrl[0].value + "'/>"
      jQuery.get("/schedule?temp=" + temp, () => {
        alert("saved")
      })
    })
  });
<<<<<<< HEAD
=======

>>>>>>> 72a28b035b35d770a4b0a570910862aa52035431
var checkedDiv = document.querySelectorAll('#checked');
var cool = 12
var times = ["10AM", "12PM", "2PM", "4PM", "6PM"]
console.log(checkedDiv)
checkedDiv.forEach(function(element) {
  for(i = 0; i < times.length; i++){
    var inputSchedule = `<input type='checkbox'>I have drank ${cool}oz by ${times[i]}<br>`
    element.innerHTML = inputSchedule;
  }
});
<<<<<<< HEAD
=======


var checkedDiv = document.querySelector('#checked');
var cool = 12
var inputSchedule = `<input type='checkbox'>I have drank ${cool} oz by 10AM<br>`
console.log(checkedDiv);
checkedDiv.innerHTML = inputSchedule;


>>>>>>> 72a28b035b35d770a4b0a570910862aa52035431

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
