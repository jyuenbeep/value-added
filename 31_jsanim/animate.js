var c = document.getElementById("playground"); // GET CANVAS
var dotButton = document.getElementById("buttonCircle"); // GET DOT BUTTON 
var stopButton = document.getElementById("buttonStop"); // GET STOP BUTTON 

var ctx = c.getContext("2d");

ctx.fillStyle = "black";

var requestID = "stop"; //init global var for use with animation frames

var clear = (e) => {
    ctx.clearRect(0, 0, 500, 500);
};

var radius = 0;
var growing = true; 

var drawDot = () => {
    requestID = "dot";
    if (radius >= 250) {
        growing = false;
    }
    if (radius <= 0) {
        growing = true; 
    }

    clear();
    if (growing) {
        ctx.beginPath();
        ctx.arc(250, 250, radius, 0, 2 * Math.PI);
        ctx.fill();
        radius = radius+10;
        window.requestAnimationFrame(drawDot);
    } else {
        ctx.beginPath();
        ctx.arc(250, 250, radius, 0, 2 * Math.PI);
        ctx.fill();
        radius = radius-10;
        window.requestAnimationFrame(drawDot);
    }

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
    //window.cancelAnimationFrame()
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);