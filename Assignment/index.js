const divElement = document.getElementById("flow");
const value = [1, 2, 3];
let index = 0;

const updateElement = () => {
    divElement.innerHTML = `<div class="trans">
        <div style="border:1px solid black; width:20px; height:20px;"></div>
        <img src="./images/heroImage/${value[index]}.jpg" alt=""/>
    </div>`;
    
    index++;
    if (index >= value.length) {
        index = 0;
    }
};

setInterval(updateElement, 500);