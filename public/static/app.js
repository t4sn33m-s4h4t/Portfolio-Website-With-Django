const theme = document.querySelector(".theme-btn")
const localStorageKey = "theme"

theme.addEventListener("click", () => {
  const currentTheme = document.body.classList.contains("light-mode")

  // Save the current theme in local storage
  localStorage.setItem(localStorageKey, currentTheme ? "dark" : "light")
  console.log(666)
  // Toggle the light and dark mode of the website
  document.body.classList.toggle("light-mode")
})

// Get the current theme from local storage
const currentTheme = localStorage.getItem(localStorageKey)
if (currentTheme === "light") {
  document.body.classList.add("light-mode")
} else {
  document.body.classList.remove("light-mode")
}
