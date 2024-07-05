const btn_register = document.getElementById('btn-register');

btn_register.addEventListener('click', () => {
    pywebview.api.new_register();
});