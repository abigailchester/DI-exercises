var body = document.getElementsByTagName("body")[0]

var planet = document.createElement("div")

planet.setAttribute("class", "planet")

planet.style.backgroundColor="indigo"

var moon = document.createElement("div")

moon.setAttribute("class", "moon")

moon.style.backgroundColor="silver"

body.appendChild(planet)
body.appendChild(moon)

console.log(planet)