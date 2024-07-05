const txt_activity = document.getElementById('activity');
const txt_status = document.getElementById('status');
const btn_back = document.getElementById('back');
const btn_save = document.getElementById('save');

btn_save.addEventListener('click', () => {
    pywebview.api.save_activity(txt_activity.value, txt_status.value);
})

btn_back.addEventListener('click', () => {
    pywebview.api.open_home();
});