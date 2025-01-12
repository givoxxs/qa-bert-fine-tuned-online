document.getElementById('ask-button').addEventListener('click', function (event) {
    event.preventDefault();  // Ngừng reload trang khi nhấn nút

    const context = document.getElementById('context').value;
    const question = document.getElementById('question').value;

    if (!context || !question) {
        alert("Cả context và câu hỏi đều phải được điền!");
        return;
    }

    fetch('/answer/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ context: context, question: question })
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                document.getElementById('answer').innerText = data.answer;
            }
        })
        .catch(error => console.error('Error:', error));
});

document.getElementById('reload-button').addEventListener('click', function () {
    document.getElementById('context').value = '';  // Làm sạch input context
    document.getElementById('question').value = '';  // Làm sạch input question
    document.getElementById('answer').innerText = '...';  // Reset câu trả lời
});
