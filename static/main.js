const container = document.querySelector('.container');
const loginBtn = document.querySelector('.toggle-panel.toggle-right .btn');
const registerBtn = document.querySelector('.toggle-panel.toggle-left .btn');

loginBtn.addEventListener('click', (e) => {
    e.preventDefault();
    container.classList.remove('active');
});

registerBtn.addEventListener('click', (e) => {
    e.preventDefault();
    container.classList.add('active');
});