var c = document.getElementById("playground"); 
var dotButton = document.getElementById("circle"); 
var stopButton = document.getElementById("stop");
var dvdButton = document.getElementById("dvd");

var ctx = c.getContext("2d");
ctx.fillStyle = "#3EB489";
var requestID; 

var clear = (e) => {
    //e.preventDefault(); //what dis?
    ctx.clearRect(0, 0, 500, 500);
};

var dvdLogoSetup = function() {
    window.cancelAnimationFrame(requestID);

    var rectWidth = 60;
    var rectHeight = 40;

    //make sure the picture doesn't spill out
    var rectX = Math.random()*(c.width-rectWidth);
    var rectY = Math.random()*(c.height-rectHeight);

    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var xPosneg = Math.pow(-1, Math.floor(Math.random()*3));
    var yPosneg = Math.pow(-1, Math.floor(Math.random()*3));

    var xVel = 2*xPosneg;
    var yVel = 2*yPosneg;

    var dvdLogo = function() {
        clear();
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
        if (rectX < 0 || rectX > c.width - rectWidth) {
            xVel = -xVel;
        }
        if (rectY < 0 || rectY > c.height - rectHeight) {
            yVel = -yVel;
        }
        rectX += xVel;
        rectY += yVel;
        requestID = window.requestAnimationFrame(dvdLogo);
    }
    dvdLogo();
 };
        
var radius = 0;
var growing = true;
 
var drawDot = () => {
    window.cancelAnimationFrame(requestID);
    clear();
    ctx.beginPath();
    ctx.arc(250, 250, radius, 0, 2 * Math.PI);
    ctx.fill();
    if (growing) {
        if (radius < 250) {
            radius = radius+1;
        }
        else { growing = false; }
    } else {
        if (radius > 0) {
            radius = radius-1;
        }
        else { growing = true; }
    }
    requestID = window.requestAnimationFrame(drawDot);
};

var stopIt = () => {
    console.log("stopIt invoked...");
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
}

dotButton.addEventListener("click", drawDot);
dvdButton.addEventListener("click", dvdLogoSetup);
stopButton.addEventListener("click", stopIt);