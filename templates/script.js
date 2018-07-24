var checkedValue = $('.messageCheckbox:checked').val();

fetch("http://api.worldweatheronline.com/premium/v1/weather.ashx?key=" + weatherApi + "&q=93786&format=json&num_of_days=1")
  .then(function(response){
    response.json().then(function(data)){
      console.log(data);
      temp.innerHTML = "<h1>The current weather is" + data.data.current_condition[0].temp_F + "F<h1>"
      condition.innerHTML = "<p>" + data.data.current_condition[0].weatherDesc[0].value + "</p>"
      pic.innerHTML = <"img src='" + data.data.current_condition[0].weatherIconUrl[0].value + "'/>"
    }
  })

  function addWaterdatabase(waterdatabaseUrl, doneCallback) {
    jQuery.post("/history", {url: waterdatabaseUrl}, doneCallback);
  }

  function submitClick() {
    var inputBox = document.querySelector('#queryBox')
    var userInput = inputBox.value
    queryGiphy(userInput, displayResult)
  }


  window.addEventListener('load', () => {
    document.querySelector('#submit').addEventListener("click", submitClick)

  });
