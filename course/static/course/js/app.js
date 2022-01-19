const $ = document.querySelector.bind(document);
const $$ = document.querySelectorAll.bind(document);
// header focus on inputelement and click information
const headerInputElement = $('.header__search-wrap input')
const rootElement = $('.app__wrap')
const inforImg = $('.header__information-img');
const boxUser = $('.header__information-user-box')



headerInputElement.addEventListener('click', function(e) {
    e.stopPropagation()
})

// Click infor
if (inforImg) {
    inforImg.addEventListener('click', function() {
        boxUser.classList.toggle('isopen')
    })   
}
if (boxUser != null) {
    boxUser.addEventListener('click', function(e) {
        e.stopPropagation()
    })

}


// Add js

const boxAdd = $('.page__sidebar-add-box')


boxAdd.addEventListener('click', function(e) {
    e.stopPropagation()
})

// Sidebar active

// Slider render

const sliderList = $('.page__content-slider-list')

// const data = fetch('http://localhost:8000/api/category/')
//     .then(data => { return data.json() })
//     .then(data=>{console.log(data);})
            
const sliderContent = [
    {
        heading: 'Đừng xấu hổ khi không biết',
        description: 'Để đạt được kết quả tốt trong mọi việc ta cần xác định mục tiêu rõ ràng cho việc đó.',
        background: 'linear-gradient(to right, rgb(118, 18, 255), rgb(5, 178, 255));',
    },
    {
        heading: 'Chỉ xấu hổ khi không học.',
        description: 'Đừng để mình là gánh nặng cho gia đình cho xã hội.',
        background: 'linear-gradient(to right, rgb(254, 33, 94), rgb(255, 148, 2));',
    },
    {
        heading: 'Học, học nữa, học mãi.',
        description: 'Cố gắng trở thành người có ích cho xã hội, hãy là một mẫu người mà mọi người mơ ước',
        background: 'linear-gradient(to right, rgb(0, 126, 254), rgb(6, 195, 254));',
    }
]

const htmlsSlider = sliderContent.map(function(content, index) {
    return `
        <div class="page__content-slider-item" style="background: ${content.background};" data-index="${index}">
            <div class="page__content-slider-item-content">
                <h2 class="page__content-slider-item-heading">${content.heading}</h2>
                <p class="page__content-slider-item-description">${content.description}</p>
            </div>
            
        </div>
    `
})

sliderList.innerHTML = htmlsSlider.join('')


// Slider handle


let sliderItemElement = $$('.page__content-slider-item')
let index = 0;
let slideId;

const firstClone = sliderItemElement[0].cloneNode(true);
const lastClone = sliderItemElement[sliderItemElement.length - 1].cloneNode(true);

firstClone.id = 'slider__first-clone'
lastClone.id = 'slider__last-clone'

sliderList.append(firstClone)
sliderList.append(lastClone)


const sliderWidth = 100;
const slicks = $$('.page__content-slider-slickdot li')

// Slider slickdot

const slickHandle = function () {
    for(let i = 0; i < slicks.length; i++ ) {
        if(i === index) {
            slicks[i].classList.add('slideractive')
        } else if (index === 3 || index === 0) {
            slicks[0].classList.add('slideractive')
            slicks[slicks.length - 1].classList.remove('slideractive')
        } else {
            slicks[i].classList.remove('slideractive')
        }
    }
}

const startSlider = () => {
    slideId = setInterval(() => {
        index++;
        if (index >= 3) {
            index = 0
        }
        console.log(index);
        sliderList.style.transform = `translateX(${-sliderWidth * index}%)`
        sliderList.style.transition = '1s'
        slickHandle()
    },6000)
    
}

startSlider()
