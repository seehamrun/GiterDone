function showReminderTimes(num){
  var reminderElem = document.getElementById("reminderTimes")
  var children = reminderElem.children
  for (var i=0; i<num; i++) {
    children[i].style.visibility = "visible";
  }
}
