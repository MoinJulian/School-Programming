const nav = document.querySelector("nav");
const links = document.createElement("div");
const home = document.createElement("a");
const what_is_golf_games = document.createElement("a");
const a = document.querySelectorAll("a");

//nav styles
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
what_is_golf_games.style.marginLeft = "10px";

// Links styles

links.style.display = "flex";
links.style.alignItems = "center";
links.style.justifyContent = "center";
links.style.width = "25vw";

links.appendChild(home);
links.appendChild(what_is_golf_games);
nav.appendChild(links);
