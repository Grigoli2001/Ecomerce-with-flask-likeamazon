const yourAccount = document.getElementById("yourAccount");
const yourAccountMenu = document.getElementById("yourAccountMenu");
yourAccount.addEventListener("mouseover", () => {
  yourAccountMenu.style.display = "block";
});
yourAccountMenu.addEventListener("mouseover", () => {
  yourAccountMenu.style.display = "block";
});
yourAccount.addEventListener("mouseleave", () => {
  yourAccountMenu.style.display = "none";
  yourAccountMenu.addEventListener("mouseleave", () => {
    yourAccountMenu.style.display = "none";
  });
});
