function toggleForm(taskId) {
    var taskBody = document.getElementById('task_' + taskId);
    if (taskBody) {
        taskBody.classList.toggle('show_form');
    } else {
        console.error('Element with id task_' + taskId + ' not found.');
    }
}
