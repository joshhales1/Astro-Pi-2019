for (var j = 1; j < imageNum; j++) {
  image = new Image();
  image.src = "../images/zz_oba_" + j + ".jpg";
  postMessage(image);
}