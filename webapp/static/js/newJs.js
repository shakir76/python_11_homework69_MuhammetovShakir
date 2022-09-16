function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


async function buttonOnClick(event) {
    event.preventDefault();
    let target = event.target
    let url = target.dataset.new
    const csrftoken = getCookie('csrftoken');
    let a = document.getElementById('A').value
    let b = document.getElementById('B').value
    let data = {
        "A": a,
        "B": b
    }
    let response = await fetch(url, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {'X-CSRFToken': csrftoken}
    })
    let new_response = await response.json()
    let divAnswer = document.getElementById('answer')
    let h1 = document.getElementById('h1')
    if (response.status === 200 ){
        divAnswer.style.background = 'green'
        h1.innerText = new_response.answer
    }
    else {
          divAnswer.style.background = 'red'
         h1.innerText = new_response.error
    }


}


function getAnswer() {
    let buttons = document.getElementsByClassName('btn')
    for (button of buttons) {
        button.addEventListener('click', buttonOnClick)
    }
}

window.addEventListener('load', getAnswer)