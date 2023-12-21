document.addEventListener("DOMContentLoaded", () => {
  let code_block = document.querySelector(".post__content pre");
  if (code_block) {
    code_block.classList.add("post__content--code", "code__content");
  }

  // SITE THEME CHANGE
  const mode__changer = document.querySelector(".change__mode");
  const sun__svg = document.querySelector(".sun__svg");
  const moon__svg = document.querySelector(".moon__svg");
  const site__mode = document.querySelector("html");
  let site_theme = null

  function siteModeChecker() {
    site_theme = JSON.parse(localStorage.getItem("el-blog"));
    if (!site_theme?.theme) {
      if (site__mode.getAttribute("data-theme") == "dark") {
        localStorage.setItem('el-blog', JSON.stringify({'theme' : 'dark'}));
        sun__svg.style.display = "block";
        moon__svg.style.display = "none";
      } else {
        moon__svg.style.display = "block";
        sun__svg.style.display = "none";
        localStorage.setItem('el-blog', JSON.stringify({'theme' : 'light'}));
      }
    } else {
      if(site_theme?.theme == 'dark'){
        sun__svg.style.display = "block";
        moon__svg.style.display = "none";
        site__mode.setAttribute("data-theme", "dark");
      } else {
        moon__svg.style.display = "block";
        sun__svg.style.display = "none";
        site__mode.setAttribute("data-theme", "light");
      }
    }
  }
  siteModeChecker();

  sun__svg.addEventListener("click", () => {
    site__mode.removeAttribute("data-theme", "dark");
    site__mode.setAttribute("data-theme", "light");
    localStorage.setItem('el-blog', JSON.stringify({'theme' : 'light'}));
    siteModeChecker();
  });

  moon__svg.addEventListener("click", () => {
    site__mode.removeAttribute("data-theme", "light");
    site__mode.setAttribute("data-theme", "dark");
    localStorage.setItem('el-blog', JSON.stringify({'theme' : 'dark'}));
    siteModeChecker();
  });
});
