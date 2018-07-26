function showReminderTimes(num){
  var reminderElem = document.getElementById("reminderTimes")
  var children = reminderElem.children
  for (var i=0; i<children.length; i++) {
    children[i].style.visibility = "hidden";
  }
  for (var i=0; i<num; i++) {
    children[i].style.visibility = "visible";
  }
}

window.addEventListener('load', () => {
  var dropdown = document.querySelector('#reminder')
  showReminderTimes(dropdown.value)
})
