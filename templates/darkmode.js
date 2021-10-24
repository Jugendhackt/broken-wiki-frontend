function Darkmode(E) {
    setdarkmode(!E.target.checked);
  }
  document.getElementById("darkmode").addEventListener("click",Darkmode)

  function setdarkmode(on){
   var element = document.body;
    element.classList.toggle("dark-mode",on);
  }
  window.onload=function(){
    var scheckbox=document.getElementById("darkmode")
    setdarkmode(!scheckbox.checked)
  }