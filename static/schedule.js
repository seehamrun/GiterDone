fetch("https://api.worldweatheronline.com/premium/v1/weather.ashx?key=" + weatherApi + "&q=60607&format=json&num_of_days=1")
  .then(function(response){
    response.json().then(function(data){
      console.log(data);
      currentTemp = data.data.current_condition[0].temp_F
      temp.innerHTML = "<h1>The current weather is " + currentTemp + "F<h1>"
      condition.innerHTML = "<p>" + data.data.current_condition[0].weatherDesc[0].value + "</p>"
      pic.innerHTML = "<img src='" + data.data.current_condition[0].weatherIconUrl[0].value + "'/>"
      // jQuery.get("/schedule?temp=" + temp, () => {

      jQuery.get("/schedule?temp=" + currentTemp, () =>{
        //alert("sent")
      } )
      // })
    })
  });
  // if (temp < 80) {
  //     document.getElementById("demo").innerHTML = "It is hot outside, you should drink more water!";

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


  // var d = new Date();
  // document.getElementById("demo").innerHTML = d;
  //
  var today = new Date();
  var dd = today.getDate();
  var mm = today.getMonth()+1; //January is 0!
  var yyyy = today.getFullYear();

  if(dd<10) {
      dd = '0'+dd
  }

  if(mm<10) {
      mm = '0'+mm
  }

  date = mm + '/' + dd + '/' + yyyy;
  // document.write(date);

  var input = document.getElementById("myInput");
  input.addEventListener("keyup", function(event) {
      event.preventDefault();
      if (event.keyCode === 13) {
          document.getElementById("myBtn").click();
      }
  });



  window.addEventListener('load', () => {
    document.querySelector('#submit').addEventListener("click", submitClick)
    document.querySelector("#date").innerHTML = mm + '/' + dd + '/' + yyyy;

  });
