var canvas = document.getElementById('canvas'),
  context = canvas.getContext('2d');
const path = "../images/"
const imageNum = 2501;
var i = 1;
var frames = {};

function frame() {
  image = new Image();
  image.src = "../images/zz_oba_" + j + ".jpg";
  context.drawImage(image, 0, 0);
}

var frameRate = setInterval(function() {
  if (i > imageNum) end();
  frame();
  i++;
}, 1000 / 30);


function end() {
  clearTimeout(frameRate);
}