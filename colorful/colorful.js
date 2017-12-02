document.onmousemove = function (e) {
    mousePos(e);
    changeBackgroundColor();
};

var mouseX = 0;
var mouseY = 0;
var colorrPreRound;
var colorbPreRound;
var coloryPreRound;
var ratioClosest;

function mousePos(event) {
    mouseX = event.clientX + document.body.scrollLeft;
    mouseY = event.clientY + document.body.scrollTop;

    var windowWidth = window.innerWidth;
    var windowHeight = window.innerHeight;
    document.show.mouseXField.value = mouseX;
    document.show.mouseYField.value = mouseY;
    document.show.windowWidth.value = windowWidth;
    document.show.windowHeight.value = windowHeight;

    var xCenter = windowWidth / 2;
    var yCenter = windowHeight / 2;

    var relCursorX = xCenter - mouseX;
    var relCursorY = yCenter - mouseY;

    var thetaPoint = Math.atan2(relCursorY, relCursorX);
    var absoluteTheta = Math.abs(thetaPoint);

    var minus60x = (relCursorX * Math.cos(-60) - relCursorY * Math.sin(-60));
    var minus60y = (relCursorX * Math.sin(-60) + relCursorY * Math.cos(-60));
    var minusThetaPoint = Math.atan2(minus60y, minus60x);
    var absoluteMinusThetaPoint = Math.abs(minusThetaPoint);

    var plus60x = (relCursorX * Math.cos(60) - relCursorY * Math.sin(60));
    var plus60y = (relCursorX * Math.sin(60) + relCursorY * Math.cos(60));
    var plusThetaPoint = Math.atan2(plus60y, plus60x);
    var absolutePlusThetaPoint = Math.abs(plusThetaPoint);

    // These are to get distance from origin
    var xSquared = Math.pow(relCursorX, 2);
    var ySquared = Math.pow(relCursorY, 2);
    var pointSquared = xSquared + ySquared;
    var distToOrigin = Math.sqrt(pointSquared);

    colorrPreRound = (absoluteTheta / Math.PI) * 255;
    colorbPreRound = (absoluteMinusThetaPoint / Math.PI) * 255;
    coloryPreRound = (absolutePlusThetaPoint / Math.PI) * 255;

    if (windowHeight >= windowWidth) {
        ratioClosest = 2 * distToOrigin / windowWidth;
    } else {
        ratioClosest = 2 * distToOrigin / windowHeight;
    }
}


function changeBackgroundColor() {
    // Change the fixed number to adjust brightness
    var intensity = .5 - ratioClosest;
    var colorIntensify = function (n) {
        var z = n + (intensity * 255);
        if (z >= 255) {
            return 255
        } else if (z <= 0) {
            return "00"
        } else return Math.round(z)
    };

    var colorr = colorIntensify(colorrPreRound);
    var colorb = colorIntensify(colorbPreRound);
    var colory = colorIntensify(coloryPreRound);
    var colorr0fixed = colorr.toString(16);
    var colorb0fixed = colorb.toString(16);
    var colory0fixed = colory.toString(16);

    var concatC = [colorr0fixed, colorb0fixed, colory0fixed];
    var strungC = concatC.join("");
    
    var color_combined = "#" + strungC;

    var y = document.getElementById("body");
    y.style.background = color_combined;

    document.show.colorg.value = color_combined;
    document.show.distToOrigin.value = intensity;
}