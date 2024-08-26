const card = document.getElementById("summary")

const datas = [
    {
        id: 1,
        image: "",
        name: "orders",
        about: "Enter Order: 346",
        button: "view orders"
    },
    {
        id: 2,
        image: "",
        name: "store inventory",
        about: "total items: 24",
        button: "view now"
    },
    {
        id: 3,
        image: "",
        name: "sales manager",
        about: "total sales: 346",
        button: "view sales log"
    },
    {
        id: 4,
        image: "",
        name: "staff management",
        about: "total staffs: 47",
        button: "manage staff"
    },
]

let value = []

datas.map((data) => {
    value.push(
        `<div class="s-card">
            <img src="${data.image}" alt="${data.id}" />
            <h3>${data.name}</h3>
            <p>${data.about}</p>
            <a href="">${data.button}</a>
        </div>`
    )
})

card.innerHTML = value
