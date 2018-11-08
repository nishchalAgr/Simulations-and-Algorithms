
var pointsX = [];
var pointsY = [];
var mPX = [];
var mPY = [];
var lineX = [];
var lineY = [];
var winX = 400;
var winY = 400;
var denX = 10;
var denY = 10;
var offset = 5;
var isMouse = true;


function setup(){
  createCanvas(winX,winY);
  //button = createButton("Log");
  //button.mousePressed(logArr);
}

function draw(){
  stroke(255);
  line(0, 0, winX, winY);
  background(51);

  if(!mouseIsPressed){

    isMouse = true;

  }
  if(mouseIsPressed && isMouse){

    pointsX.push(mouseX);
    pointsY.push(winY - mouseY);
    mPX.push(mouseX);
    mPY.push(mouseY)
    isMouse = false;
    //console.log(pointsX);
    //console.log(pointsY);
  }

  drawPoints();
  drawLine();
  drawG();
}

function drawPoints(){

  fill(255,255,255); // blue points
  noStroke(); // white stroke
  for(i = 0; i < mPX.length; i++){

    ellipse(mPX[i], mPY[i], 3, 3);
    //console.log(pointsX[i]);
    //console.log(pointsY[i]);

  }

}

function logArr(){

  console.log(lineX);
  console.log(lineY);

}

function drawG(){
  //translate(10, winY-10);
  stroke(255, 255, 255);
  strokeWeight(1);
  line(offset, 0, offset, winY - offset);// y line
  line(offset, winY - offset, winX, winY - offset);// x line

  var x = offset;
  var y = winY - offset;

  for(i = 0; i < denX; i++){
    line(x, winY - offset, x, winY - 2 * offset);
    x += winX / denX;
  }

  for(i = 0; i < denY; i++){
    line(offset, y, 2 * offset, y);
    y -= winY / denY;
  }

}


function drawLine(){

  lineX = [];
  lineY = [];

  var m = 0;
  var b = 0;

  var sumX = 0;
  var sumY = 0;
  var sumXexp = 0;
  var sumXY = 0;

  for(i = 0; i < pointsX.length; i++){

    sumX += pointsX[i];
    sumY += pointsY[i];
    sumXexp += pointsX[i] * pointsX[i];
    sumXY += pointsX[i] * pointsY[i];

  }

  //calculation of slope of line and y intercept
  m = (pointsX.length * sumXY - sumX * sumY) / (pointsX.length * sumXexp - sumX * sumX);
  b = (sumY - m * sumX) / pointsX.length;

  //y intercept
  lineX.push(0);
  lineY.push(Math.round(b));

  for(i = 0; i < pointsX.length; i++){

    //calculating predicted y for x
    lineX.push(pointsX[i]);
    lineY.push(pointsX[i] * m + b);

  }

  //drawing line using predicted y and x
  stroke(0,0,255);
  strokeWeight(3);
  var max = 0;
  var maxI = 0;
  for(i = 0; i < lineY.length - 1; i++){

    ellipse(lineX[i], winY - lineY[i], 3,3)

  }
  //console.log(lineX);
  //console.log(lineY);
  //console.log(lineX[maxI], lineY[maxI]);
  //console.log(maxI);
  //console.log(lineX[maxI]);

  //console.log(lineX);
  //console.log(lineY);

}
