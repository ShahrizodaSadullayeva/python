
$('#Cards').carousel('pause');


window.onclick = function(event){
  if(!event.target.matches('.py_dict')){
    var dropdowns = document.getElementsByClassName('py_dict_item');
    var i;
    for(i = 0; i < dropdowns.length; i++){
      var openDropdown = dropdowns[i];
      if(openDropdown.classList.contains('show')){
        openDropdown.classList.remove('show');
      }
    }
  }
}

//
// document.getElementById('Run1').onclick = function(){
//   window.open('Run1.html');
// }

function Night(id1, id2){
  if(document.getElementById(id2).style.bacgroundColor = "white"){
    document.getElementById(id1).style.backgroundColor = "gray";
    document.getElementById(id2).style.backgroundColor = "gray";
  }
  else{
    document.getElementById(id1).style.backgroundColor = "white";
    document.getElementById(id2).style.backgroundColor = "white";
  }
}

function home(){
  window.open("python.html");
}


function Rotate(id1, id2, id3){
  if(document.getElementById(id1).style.flexDirection = "row"){
    document.getElementById(id1).style.flexDirection = "column";
    document.getElementById(id1).style.rowGap = "10px";
    document.getElementById(id2).style.width = '100%';
    document.getElementById(id2).style.height = "200px";
    document.getElementById(id3).style.width = "100%";
    document.getElementById(id3).style.height = "200px";
  }
  else{
    alert("salom");
    document.getElementById(id1).style.flexDirection = "row";
    document.getElementById(id1).style.columnGap = "20px";
    document.getElementById(id2).style.width = '49%';
    document.getElementById(id2).style.height = "500px";
    document.getElementById(id3).style.width = "49%";
    document.getElementById(id3).style.height = "500px";

  }
}
$(document).ready(function(){
  $("#myCarousel").carousel();
});

$(document).ready(function(){
  $("#Run_Carousel").carousel();
});


function carusell(id1, id2){
  if(document.getElementById(id1).style.opacity = "0%"){
    document.getElementById(id1).style.opacity = "100%";
    document.getElementById(id1).style.zIndex = "1";
    document.getElementById(id2).style.filter = "blur(5px)";
    document.getElementById(id2).style.position = "fixed";
  }
  else{
    document.getElementById(id2).style.filter = "blur(0px)";
    document.getElementById(id2).style.position = "absolute";
    document.getElementById(id1).style.opacity = "0%";
    document.getElementById(id1).style.zIndex = "-1";
  }
}



// function infor(id1, id2){
//   document.getElementById(id1).style.display = "block";
//   document.getElementById(id2).style.display = "none";
// }

function menu1(id1, id2, id3, id4, id5, id6, id7, id8, id9, id10, id11, id12, id13, id14, id15, id16, id17, id18, id19, id20, id21, id22, id23, id24, id25, id26, id27, id28, id29, id30, id31, id32, id33, id34, id35, id36, id37){
  document.getElementById(id1).classList.toggle("show");
  document.getElementById(id2).classList.remove("show");
  document.getElementById(id3).classList.remove("show");
  document.getElementById(id4).classList.remove("show");
  document.getElementById(id5).classList.remove("show");
  document.getElementById(id6).classList.remove("show");
  document.getElementById(id7).classList.remove("show");
  document.getElementById(id8).classList.remove("show");
  document.getElementById(id9).classList.remove("show");
  document.getElementById(id10).classList.remove("show");
  document.getElementById(id11).classList.remove("show");
  document.getElementById(id12).classList.remove("show");
  document.getElementById(id13).classList.remove("show");
  document.getElementById(id14).classList.remove("show");
  document.getElementById(id15).classList.remove("show");
  document.getElementById(id16).classList.remove("show");
  document.getElementById(id17).classList.remove("show");
  document.getElementById(id18).classList.remove("show");
  document.getElementById(id19).classList.remove("show");
  document.getElementById(id20).classList.remove("show");
  document.getElementById(id21).classList.remove("show");
  document.getElementById(id22).classList.remove("show");
  document.getElementById(id23).classList.remove("show");
  document.getElementById(id24).classList.remove("show");
  document.getElementById(id25).classList.remove("show");
  document.getElementById(id26).classList.remove("show");
  document.getElementById(id27).classList.remove("show");
  document.getElementById(id28).classList.remove("show");
  document.getElementById(id29).classList.remove("show");
  document.getElementById(id30).classList.remove("show");
  document.getElementById(id31).classList.remove("show");
  document.getElementById(id32).classList.remove("show");
  document.getElementById(id33).classList.remove("show");
  document.getElementById(id34).classList.remove("show");
  document.getElementById(id35).classList.remove("show");
  document.getElementById(id36).classList.remove("show");
  document.getElementById(id37).classList.remove("show");
}


