function showScrollBar(){
    var text_area = document.getElementById("content");
    text_area.className = "show";
}

function hideScrollBar(){
  var text_area = document.getElementById("content");
  text_area.className = "none";
}

function expandInput(){
  var input = document.getElementById("sr");
  input.className = "expanded-input";
  input.disabled = false;
}

function checkInput(){
  var input = document.getElementById("sr");
  if (input.value==""){
    input.className = "collapsed-input";
    input.disabled = true;
  }
}