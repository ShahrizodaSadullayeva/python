


function windowScreen(){


const texts = document.querySelectorAll('.animation-text');

for(let i = 0; i < texts.length; i++){
    const text = texts[i];
    const strText = text.textContent;
    const splitText = strText.split('');
    text.textContent = "";

    for(let i = 0; i < splitText.length; i++){
        text.innerHTML += "<span>" + splitText[i] + "</span>";
    }

    let char = 0;
    let timer = setInterval(onTick, 50);

    function onTick(){
        const span = text.querySelectorAll('span')[char];
        span.classList.add('fadee');
        char++;

        if(char === splitText.length){
            complete();
            return;
        }
    }

    function complete(){
        clearInterval(timer);
        timer = null;
    }
}

const elements = document.querySelectorAll(".select-div-animation");
for(let i = 0; i < elements.length; i++){
    const element = elements[i];
    element.classList.add("fadee2");
}

}

window.requestAnimationFrame(windowScreen);