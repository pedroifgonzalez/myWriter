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

function showWritings(){
  var content = document.getElementById('content');
  var items = document.getElementById('items');
  var sort_date_button = document.getElementById('sort_date');
  var sort_button = document.getElementById('sort');
  var all_button = document.getElementById('all');
  var save_button = document.getElementById('save');

  all_button.className = "hide";
  save_button.className = "hide";
  if(sort == false){
    sort_button.className = "button";
  }else{
    sort_button.className = "show_footer";
  }
  sort_date_button.className = "button";
  items.className = "show";
  items.className = "hidden_footer";
  window.setTimeout(function(){
    items.className = "show_footer";
  },200);
  content.id = "show_writings";
}

function restoreContent(){
  var sort_date_button = document.getElementById('sort_date');
  var sort_button = document.getElementById('sort');
  var all_button = document.getElementById('all');
  var save_button = document.getElementById('save');

  all_button.className = "button";
  save_button.className = "button";
  sort_button.className = "hide";
  sort_date_button.className = "hide";
  var content = document.getElementById('show_writings');
  var items = document.getElementById('items');

  if (items.className!="hide"){
  items.className = "hidden_footer";
  window.setTimeout(function(){
    items.className = "hide";
  },500);
  content.id = "content";
}
  setWordsQuantity();
  checkInput();
}

function hideFooter(){
  var footer = document.getElementById('footer');
  footer.className="hidden_footer";
  hideScrollBar();
}

function showFooter(){
  var footer = document.getElementById('footer');
  footer.className="show_footer";
}