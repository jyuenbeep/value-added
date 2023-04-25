// TOOLBOX:
// clearRect()
// getElementById()
// addEventListener()
// fillStyle()
// strokeStyle()
// clearRect()
// fillText()
// beginPath()
// fillStype
// arc()
// fill()
// stroke()
// Math.PI
// offsetX
// offsetY

//retrive node in DOM via ID
var c = document.getElementById("slate");

//instantate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init global state var 
var mode = "rect";

//var toggleMode = function(e) {
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode === "rect") {
        mode = "circ";
    }
    else {
        mode = "rect";
    }
}

var drawRect = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;    
    ctx.fillRect(mouseX, mouseY, 10, 10);
    console.log("mouseclick registered at ", mouseX, mouseY);
}

var drawCircle = function(e){
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 10, 0, 2 * Math.PI);
    ctx.fill();
}

//var draw = function(e) {
var draw = (e) => {
    if (mode == "rect") {
        drawRect(e);
    } 
    else {
        drawCircle(e);
    }
}

//var wipeCanvas = function() {
var wipeCanvas = () => {
    ctx.clearRect(0, 0, 600, 600);
}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);
var bClear = document.getElementById("buttonClear");
bClear.addEventListener("click", wipeCanvas);