var canvas = document.getElementById('canvas'),
  context = canvas.getContext('2d');
const path = "../images/"
const imageNum = 2501;
var i = 1;
var frames = {};


if (window.Worker) {

  var myWorker = new Worker('./imageloader.js');

}


function frameRenderer() {
  if (i > imageNum) end();
  context.drawImage(frames[i], 0, 0);
  i++;
}


var frameRate = setInterval(function() {
  frameRenderer();
}, 1000 / 30);



function end() {
  clearTimeout(frameRate);
}