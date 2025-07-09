// Scroll fluide
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// FAQ accordéon
const faqQuestions = document.querySelectorAll('.faq-question');

faqQuestions.forEach(button => {
    button.addEventListener('click', () => {
        button.classList.toggle('active');
        const answer = button.nextElementSibling;
        if (answer.style.maxHeight) {
            answer.style.maxHeight = null;
        } else {
            answer.style.maxHeight = answer.scrollHeight + "px";
        }
    });
});
