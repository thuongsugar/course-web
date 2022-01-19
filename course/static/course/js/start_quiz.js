var examWrap = document.querySelector('.box-wrap-exam')
var url = window.location.origin
var btnStartQuiz = document.querySelectorAll('.page__exam-course-item-btn')
var quizBox = document.querySelector('.page__content__exam-item')
var quizBoxParent = document.querySelector('.quiz')
const timerBox = document.querySelector('.time-quiz')
var isSendQuiz = false
var idCourse
var cheat = 0
quizBoxParent.setAttribute('style','display:none')
btnStartQuiz.forEach(button => {
    button.onclick = e => {
        idCourse = e.target.getAttribute('data-id')
        if (confirm("Bạn đã sẵn sàng rồi chứ ?")) {
            fullScreen()
            examWrap.setAttribute('style','display:none')
            quizBoxParent.setAttribute('style','display:block')
            getQuestion(idCourse);
        }
    }
})
function getQuestion(idCourse) {
    // quizBoxParent.innerHTML = ''
    var apiQuestion =url + `/quiz/${idCourse}`
    var data
    console.log(apiQuestion);
    fetch(apiQuestion)
        .then(data => {
            return data.json()
        })
        .then(dataResponse => {
            console.log(dataResponse);
            data = dataResponse.data
            data.forEach((q,index) => {
                for (const [question, answer] of Object.entries(q)) {
                    var ans='';
                    answer.forEach(a => {
                        ans += `<li>
                                    <input type="radio" value="${a}" class="ans" id="${question}-${a}" name="${question}">
                                    <label for="${question}-${a}">${a}</label>
                            </li>`
                    })
                    quizBox.innerHTML += `
                            <div class="gird_colum-2">
                                <div class="page__content-quiz">
                                    <div class="page__content-quiz-question">
                                        <div class="page__content-quiz-question-text">
                                            <h2>Câu hỏi ${index+1}</h2>
                                            <span>${question}</span>
                                        </div>
                                    </div>
                                    <div class="page__content-quiz-answer">
                                            <ul>
                                                ${ans}
                                            </ul>
                                    </div>
                                </div>
                            </div>
                   `
                }
            })
            activateTimer(dataResponse.time)
        })
}

const quizForm = document.getElementById('quiz_form')

function sendData() {
    console.log((cheat - 1) / 2);
    const csrf = document.getElementsByName('csrfmiddlewaretoken')
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    cheat = Math.round((cheat - 1) / 2)
    data['cheat'] =cheat
    elements.forEach(el=>{
        if (el.checked) {
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })
    console.log(data);
    fetch(url + `/quiz/${idCourse}/save`,
        {   
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                "X-CSRFToken": csrf[0].value
            },
            body: JSON.stringify(data)
        }
    )
        .then(data => { return data.json() })
        .then(data => {
            console.log(data);
            quizBoxParent.innerHTML = ''
            dataResult = data.result
            htmlResult = ''
            dataResult.forEach(r => {
                for ([q, a] of Object.entries(r)) {
                    console.log(a);
                    answerResult = ''
                    if (a.answer_correct == a.answered) {
                        answerResult = `<li style="background:green"}>
                                    ${a.answer_correct}
                            </li>`
                    } else {
                        if (a.answered === null) {
                            answerResult = `<li style="background:red">
                                    ${a.answered}(không chọn)
                            </li>
                            <li style="background:green">
                                ${a.answer_correct}
                            </li>`
                        } else {
                            answerResult = `<li style="background:red">
                                    ${a.answered}
                            </li>
                            <li style="background:green">
                                ${a.answer_correct}
                            </li>`
                        }
                        
                    }
                    
                    htmlResult += `
                    <div class="gird_colum-2">
                        <div class="page__content-quiz">
                            <div class="page__content-quiz-question">
                                <div class="page__content-quiz-question-text">
                                    <span>${q}</span>
                                </div>
                            </div>
                            <div class="page__content-quiz-answer">
                                    <ul>
                                        ${answerResult}
                                    </ul>
                            </div>
                        </div>
                    </div>
        `  
                }
                     
            })
            htmlResult = `<div class="score_quiz" style="font-size: 18px">
                                <b>${data.score} điểm</b>
                            </div>
                            <hr>
                            `
                + `<div class="page__content__exam-item">
                            ${htmlResult}
                            </div>`
            quizBoxParent.innerHTML = htmlResult
            
        })

}

quizForm.onsubmit = e => {
    e.preventDefault()
    document.getElementById('id01').style.display = 'block'
    var btnSave = document.querySelector('.savebtn')
    btnSave.onclick = e => {
        isSendQuiz = true
        cancelFullScreen()
        sendData();
        document.getElementById('id01').style.display='none'
    
        clearInterval()
        timerBox.style.display = 'none'
    }
}



const activateTimer = (time) => {
    if (time.toString().length < 2) {
        timerBox.innerHTML = `<b>0${time}:00</b>`
    } else {
        timerBox.innerHTML = `<b>${time}:00</b>`
    }

    let minutes = time - 1
    let seconds = 60
    let displaySeconds
    let displayMinutes

    const timer = setInterval(()=>{
        seconds --
        if (seconds < 0) {
            seconds = 59
            minutes --
        }
        if (minutes.toString().length < 2) {
            displayMinutes = '0'+minutes
        } else {
            displayMinutes = minutes
        }
        if(seconds.toString().length < 2) {
            displaySeconds = '0' + seconds
        } else {
            displaySeconds = seconds
        }
        if (isSendQuiz) {
            clearInterval(timer)
        }
        if (minutes === 0 && seconds === 0) {
            timerBox.innerHTML = "<b>00:00</b>"
            setTimeout(()=>{
                clearInterval(timer)
                alert('Hết thời gian')
                isSendQuiz = true
                sendData()
                cancelFullScreen()
                document.getElementById('id012').style.display = 'none'
                timerBox.style.display = 'none'

            }, 500)
        }

        timerBox.innerHTML = `<b>${displayMinutes}:${displaySeconds}</b>`
    }, 1000)
}

var docElm =  document.querySelector('.quiz')
function fullScreen() {
    // var docElm = document.querySelector('.quiz')
    if (quizBoxParent.requestFullscreen) {
        quizBoxParent.requestFullscreen();
    }
    else if (quizBoxParent.mozRequestFullScreen) {
        quizBoxParent.mozRequestFullScreen();
    }
    else if (quizBoxParent.webkitRequestFullScreen) {
        quizBoxParent.webkitRequestFullScreen();
    }
    else if (quizBoxParent.msRequestFullscreen) {
        quizBoxParent.msRequestFullscreen();
    }
}
function cancelFullScreen() {
    // var quizBoxParent = document.querySelector('.quiz')
    console.log("huy full");
    console.log(quizBoxParent);
    if (document.exitFullscreen) {
        document.exitFullscreen();
    }
    else if (document.mozCancelFullScreen) {
        document.mozCancelFullScreen();
    }
    else if (document.webkitCancelFullScreen) {
        document.webkitCancelFullScreen();
    }
    else if (document.msExitFullscreen) {
        document.msExitFullscreen();
    }
}

quizBoxParent.addEventListener("fullscreenchange", function (e) {
    if (isSendQuiz === false) {
        cheat++
        console.log("vao full screen");
        document.getElementById('id012').style.display = 'block'
        var btnBack = document.querySelector('.backbtn')
        btnBack.onclick = e => {
            fullScreen()
            document.getElementById('id012').style.display = 'none'
        }    
    } else {
        cancelFullScreen()
        document.getElementById('id012').style.display = 'none'
    }
}, false);
