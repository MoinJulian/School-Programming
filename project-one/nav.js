const nav = document.querySelector("nav");
const links = document.createElement("div");
const home = document.createElement("a");
const what_is_golf_games = document.createElement("a");
const a = document.querySelectorAll("a");

//nav styles
nav.style.width = "50vw";
nav.style.height = "30px";
nav.style.borderBottom = "1px solid grey";

// home link styles

home.href = "./index.html";
home.textContent = "Home";
home.style.color = "black";

// What is Golf Styles

what_is_golf_games.href = "./what-is-golf-games.html";
what_is_golf_games.textContent = "What is Golf Games?";
what_is_golf_games.style.color = "black";

// Links styles

links.style.display = "flex";
links.style.alignItems = "center";
links.style.justifyContent = "space-between";
links.style.width = "25vw";
links.style.marginLeft = "10px";

links.appendChild(what_is_golf_games);
links.appendChild(home);
nav.appendChild(links);
