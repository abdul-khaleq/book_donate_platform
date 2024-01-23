// import Swiffy Slider JS
import { swiffyslider } from 'swiffy-slider'
window.swiffyslider = swiffyslider;

window.addEventListener("load", () => {
    window.swiffyslider.init();
});


// Message timer 
var message_timeout = document.getElementById("message-timer");

setTimeout(function () {
    message_timeout.style.display = "none";
}, 5000);
