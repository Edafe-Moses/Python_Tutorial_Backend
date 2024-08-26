let i = 0

const data = [
    {
        header: "Learn to Change the World",
        summary: "The School of Under Graduate & Post Graduate Studies at Anchor University is a beacon of academic excellence dedicated to fostering advanced learning, cutting-adge reserch, and holistic development among aspiring scholars and professionals.",
        buttons: ["Read More", "Apply Here"]
    },
    {
        header: "Imporving Lives through learning",
        summary: "The School of Post Graduate Studies at Anchor University is a beacon of academic excellence, dedicated to fostering advanced learning, cutting-adge research, and holistic development among aspiring scholars and professionals",
        buttons: ["Read More", "Apply Here"]
    },
    {
        header: "where scholarship & Innovation Meet",
        summary: "The School of Post Graduate Studies at Anchor University is a beacon of academic excellence, dedicated to fostering advanced learning, cutting-adge research, and holistic development among aspiring scholars and professionals",
        buttons: ["Read More", "Apply Here"]
    }
]
let a = "./"
let imgArr = ['./images/1.jpg','./images/2.jpg','./images/3.jpg']

const images = document.querySelectorAll('.carousel-image')
const round = document.querySelectorAll('.round')

const inc = document.getElementById("increment")
const dec = document.getElementById("decrement")

function change() {
    images[i].classList.remove('active')
    round[i].classList.remove('r-active')
    i = (i + 1) % imgArr.length
    images[i].classList.add('active')
    round[i].classList.add('r-active')
}

function carosel() { 
    inc.addEventListener('click', () => {
        change()
    })
    dec.addEventListener('click', () => {
        change(-1)
    })
    change()
}

setInterval(carosel, 5000)
window.onload(carosel())