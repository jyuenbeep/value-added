var c = document.getElementById("playground"); // GET CANVAS
var dotButton = document.getElementById("buttonCircle"); // GET DOT BUTTON 
var stopButton = document.getElementById("buttonStop"); // GET STOP BUTTON 

var ctx = c.getContext("2d");

ctx.fillStyle = "#3EB489";

var requestID = "stop"; //init global var for use with animation frames

var clear = (e) => {
    ctx.clearRect(0, 0, 500, 500);
};

var radius = 0;
var growing = true;

var drawDot = () => {
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
    /* 
        Wipe the canvas, 
        Repaint the circle,
        ... and somewhere (where/when is the right time?)
        Update requestID to propagate the animation.
        You will need 
        window.cancelAnimationFrame()
        window.requestAnimationFrame()
    */
};

//var stopIt = function() {
var stopIt = () => {
    console.log("stopIt invoked...");
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);