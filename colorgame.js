var squares=document.querySelectorAll(".square");
var colors = generaterandomcolors(6);
var pickedColor = randomcolor();
var messageDisplay=document.getElementById("gameStatus");
var display = document.getElementById("colorDisplay");
var h1 = document.querySelector("h1");
var resbut = document.querySelector("#res");

resbut.addEventListener("click", function(){
  colors=generaterandomcolors(6);
  pickedColor=randomcolor();
  display.textContent = pickedColor;

  for(var i=0;i<squares.length;i++){
    squares[i].style.backgroundColor=colors[i];
  }
  h1.style.backgroundColor="#212211"
  resbut.textContent="New colors";
})
display.textContent = pickedColor;
//squares.forEach(function(thi){
//  thi.style.backgroundColor=colors[i];
//  i++;
//});
for (var i = 0; i < squares.length; i++) {
  squares[i].style.backgroundColor = colors[i];
  squares[i].addEventListener("click", function(){
    var clickedColor=this.style.backgroundColor;
    console.log(clickedColor,pickedColor)
    if(clickedColor === pickedColor){
      h1.style.backgroundColor=clickedColor;
      resbut.textContent="Play Again";
      for(var j=0; j< squares.length; j++){
        squares[j].style.backgroundColor = pickedColor;
      }
      messageDisplay.textContent = "Correct option";
    }
    else{
      this.style.backgroundColor = "#212211";
      messageDisplay.textContent = "Try again!";
    }
  });
}

function generaterandomcolors(num){
  //make an array
  var arr=[];
  for(var i=0; i<num; i++){
    arr.push(randomColor());
  }
  return arr;
}
function randomColor(){
    //to pick r,g,b from 0 to 255
    var r = Math.floor(Math.random() * 256);
    var g = Math.floor(Math.random() * 256);
    var b = Math.floor(Math.random() * 256);
    return "rgb(" + r + ", " + g + ", " +  b + ")";
}
function randomcolor(){
  var rand = Math.floor(Math.random() * 6);
  return colors[rand];
}
