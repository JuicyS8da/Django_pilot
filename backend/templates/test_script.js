const questions = [
    {
        text: "Какой самолет имеет наибольшую дальность полета?",
        options: ["Boeing 747", "Airbus A380", "Lockheed SR-71", "Concorde"]
    },
    {
        text: "Какой максимальный потолок у пассажирского самолета?",
        options: ["10 000 м", "12 000 м", "13 700 м", "15 000 м"]
    },
    {
        text: "Какой самолет первым преодолел звуковой барьер?",
        options: ["Messerschmitt Me 262", "Bell X-1", "F-86 Sabre", "MiG-15"]
    },
    {
        text: "Что означает аббревиатура ATC?",
        options: ["Air Traffic Control", "Airplane Technical Check", "Aviation Terminal Code", "Aircraft Turbine Control"]
    },
    {
        text: "Какой авиационный прибор используется для измерения высоты?",
        options: ["Альтиметр", "Акселерометр", "Барометр", "Гироскоп"]
    },
    {
        text: "Какой двигатель чаще всего используется в современных пассажирских самолетах?",
        options: ["Реактивный", "Поршневой", "Турбовинтовой", "Электрический"]
    },
    {
        text: "Что означает термин 'stall' в авиации?",
        options: ["Потеря подъемной силы", "Отказ двигателя", "Поломка шасси", "Выход самолета за пределы взлетно-посадочной полосы"]
    },
    {
        text: "Как называется прибор, который записывает параметры полета?",
        options: ["Черный ящик", "Автопилот", "Флайт-контроллер", "Навигационный дисплей"]
    },
    {
        text: "Как называется стандартный язык радиопереговоров в авиации?",
        options: ["Английский", "Французский", "Испанский", "Немецкий"]
    },
    {
        text: "Что делает система ILS в аэропортах?",
        options: ["Помогает самолетам совершать точную посадку", "Обеспечивает контроль за багажом", "Распознает метеоусловия", "Подсчитывает количество самолетов в воздухе"]
    }
];

let currentQuestionIndex = 0;
let answers = new Array(questions.length).fill(null);

function loadQuestion() {
    const question = questions[currentQuestionIndex];
    document.getElementById("question-text").innerText = `Вопрос ${currentQuestionIndex + 1}: ${question.text}`;

    const optionsContainer = document.querySelector(".options");
    optionsContainer.innerHTML = "";
    question.options.forEach((option, index) => {
        const label = document.createElement("label");
        label.innerHTML = `<input type="radio" name="answer" value="${index}"> ${option}`;
        optionsContainer.appendChild(label);
    });

    updateQuestionList();
    updateButtons();
}

function nextQuestion() {
    const selectedOption = document.querySelector("input[name='answer']:checked");
    if (selectedOption) {
        answers[currentQuestionIndex] = selectedOption.value;
    }

    if (currentQuestionIndex < questions.length - 1) {
        currentQuestionIndex++;
        loadQuestion();
    }
}

function finishTest() {
    alert("Тест завершен! Ваши ответы сохранены.");
    // Тут можно добавить логику сохранения ответов в базу данных или перенаправления
}

function updateButtons() {
    const nextButton = document.getElementById("next-btn");
    const finishButton = document.getElementById("finish-btn");

    if (currentQuestionIndex === questions.length - 1) {
        nextButton.style.display = "none";
        finishButton.style.display = "block";
    } else {
        nextButton.style.display = "block";
        finishButton.style.display = "none";
    }
}

function updateQuestionList() {
    const questionList = document.getElementById("question-list");
    questionList.innerHTML = "";

    questions.forEach((_, index) => {
        const questionItem = document.createElement("div");
        questionItem.classList.add("question-item");
        if (answers[index] !== null) {
            questionItem.classList.add("answered");
        }
        questionItem.innerText = index + 1;
        questionItem.onclick = () => {
            currentQuestionIndex = index;
            loadQuestion();
        };
        questionList.appendChild(questionItem);
    });
}

document.addEventListener("DOMContentLoaded", loadQuestion);

document.getElementById("theme-button").addEventListener("click", function() {
    document.body.classList.toggle("dark-mode");
    this.textContent = document.body.classList.contains("dark-mode") ? "Темная" : "Светлая";
});

document.getElementById("language-select").addEventListener("change", function() {
    alert("Язык изменен на: " + this.value);
});

