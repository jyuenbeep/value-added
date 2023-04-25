var c = document.getElementById("playground"); // GET CANVAS
var dotButton = document.getElementById("buttonCircle"); // GET DOT BUTTON 
var stopButton = document.getElementById("buttonStop"); // GET STOP BUTTON 

var ctx = c.getContext("2d");

ctx.fillStyle = "black";

var requestID = 0; //init global var for use with animation frames

var clear = (e) => {
    ctx.clearRect(0, 0, 500, 500);
};

var radius = 0;
var growing = true; 
var grow = 0;

var drawDot = () => {d
    // defaults
    clear();
    ctx.beginPath();
    ctx.arc(250, 250, radius, 0, 2 * Math.PI);
    ctx.fill();
    if (growing) {
        if (grow==0) {
            if (radius<200) {
                radius++;
            } else {grow=1;}
        } else {
            if (radius>0) {
                radius--;
            } else {grow=0;}
        }
    }
    requestID =  window.requestAnimationFrame(drawDot);
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