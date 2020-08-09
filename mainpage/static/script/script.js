const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.links');
    const navLinks = document.querySelectorAll('.links li');
    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active');
        burger.classList.toggle('toggle');
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = '';
            }
            else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 5 + 0.1}s`;
            }
        });
    });

};
document.addEventListener('DOMContentLoaded', () => {
    navSlide();
    const content = document.querySelector('.content');
    if (content.style.animation) {
        content.style.animation = '';
    }
    else {
        content.style.animation = `appear 0.5s`;
    }
});
const capitalize = (str, lower = false) =>
    (lower ? str.toLowerCase() : str).replace(/(?:^|\s|["'([{])+\S/g, match => match.toUpperCase());
;
const query = () => {
    const input = document.getElementById('search');
    var link = capitalize(String(input.value))
    const el = document.getElementById(link);
    var y = el.offsetTop - el.scrollTop + el.clientTop - 60;
    if (screen.width<900)
    {
        y -= 30;
    }   
    window.scrollTo(0,y);
        
};

