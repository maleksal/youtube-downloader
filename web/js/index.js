
function download_url(url) { 
  eel.js_url_download(url);
}

function download_url_list(path) { 
  eel.js_url_list_download(path);
}

function submit(){
  if (document.getElementById('url-list').disabled){
    var url= 
      document.getElementById("text-boxI").value; 
    download_url(url);
  
  }else{
    var list_path = 
    document.getElementById("url-list").value; 
    download_url_list(list_path);
  }
}


function disable_url_list(value){
  var value = document.getElementById("text-boxI").value;
  if (value.length >  0){
    document.getElementById("url-list").disabled = true;
  } else{
    document.getElementById("url-list").disabled = false;
  }
}

function disable_url(value){
  var value1 = document.getElementById("url-list").value;
  if (value1.length >  0){
    document.getElementById("text-boxI").disabled = true;
  } else{
    document.getElementById("text-boxI").disabled = false;
  }
}


window.onload = function(){
  var c = document.getElementById("text-boxI");
  var b = document.getElementById("url-list");
     c.addEventListener("input", disable_url_list);
     b.addEventListener("input", disable_url);
}
