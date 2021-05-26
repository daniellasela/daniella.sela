
let image_tracker = 'orange';
 function change(){

 let image = document.getElementById('circle');
 if(image_tracker=='orange'){
    image.src='rbImg4.jpeg';
    image_tracker='blue';
 }
 else{
    image.src='rbImg2.jpeg';
    image_tracker='orange';
 }
 }
 let timer = setInterval('change();',3000);

function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}


 function stop(){
 clearInterval(timer);
 }