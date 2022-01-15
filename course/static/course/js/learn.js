



const widthDocument = document.querySelector('html')
// const tabsDescription = document.querySelectorAll('.description-tab')
// const panesDescription = document.querySelectorAll('.description-pane')

const paneCourse = document.querySelector('.page__js-course-app-list-respon');;
const paneContent = document.querySelector('.page__js-course-app-video-description-wrap-content')
const tabCourse = document.querySelector('.page__js-course-app-video-header-item-content');
const tabAbout = document.querySelector('.page__js-course-app-video-header-item-about')

// Hidden courses list
const appDescriptionList = document.querySelector('.page__js-course-app-video-description')
const courseBtnList = document.querySelector('.page__js-course-app-list-hidden-btn');
const courseBoxList = document.querySelector('.page__js-course-app-list');
const courseVideoApp = document.querySelector('.page__js-course-app-video');
const activeBtnCourses = document.querySelector('.page__js-course-app-video-display-btn');
const courseVideoContent = document.querySelector('.page__js-course-app-video-content');
courseBtnList.onclick = function() {
    console.log(courseBtnList)
    courseBoxList.style.width = '0px';
    courseVideoApp.style.width = '100%';
    activeBtnCourses.style.opacity = '1';
    activeBtnCourses.style.display = 'flex';
    courseVideoContent.style.height = '100%';
    appDescriptionList.style.padding = '0 200px';
    // alert()
}


activeBtnCourses.onclick = () => {
    courseBoxList.style.width = '320px';
    courseVideoApp.style.width = 'calc(100% - 320px)';
    activeBtnCourses.style.display = 'none';
    courseVideoContent.style.height = '100%';
    appDescriptionList.style.padding = '0 80px';
}

const btnOpenStyle = getComputedStyle(activeBtnCourses)

const boxCourseListStyle = getComputedStyle(courseBoxList)
courseVideoContent.onmouseover = function() {
    if(boxCourseListStyle.width != '320px') {
        activeBtnCourses.style.opacity = '1';
        timeOut = setTimeout(function() {
            activeBtnCourses.style.opacity = '0'
        },5000)
    }
}

activeBtnCourses.onmouseover = function() {
    if(boxCourseListStyle.width != '320px') {
        activeBtnCourses.style.opacity = '1'
    }
}


// Courses List
const lessionsList = document.querySelector('.page__js-course-app-list-wrap')
const lessionsList2 = document.querySelector('.page__js-course-app-list-wrap-respon')
const lessionItemTest = document.querySelector('.page__js-course-app-list-item-wrap')
const linkVideoCourses = document.querySelector('.page__js-course-app-video-content-wrap')
const testscroll = document.querySelector('.page__js-course-app-video')



// Responsive

const windowWidth = window.innerWidth

window.addEventListener('resize', function(e) {
    const heightPercent = ((e.target.innerWidth)/windowWidth * 100) - 20
    if(e.target.innerWidth > 739 && e.target.innerWidth <= 1023) {
        paneCourse.classList.add('isopen-description');
        paneContent.classList.remove('isopen-description')
        tabCourse.classList.add('isclick');
        tabAbout.classList.remove('isclick')
        linkVideoCourses.style.height = `${heightPercent}%`
    } else {
        paneCourse.classList.remove('isopen-description');
        paneContent.classList.add('isopen-description')
        tabCourse.classList.remove('isclick')
        tabAbout.classList.add('isclick')
    }
})




