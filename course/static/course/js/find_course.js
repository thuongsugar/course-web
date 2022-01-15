const findCourseEl = document.querySelector('.header__search-input')
const resultCourseBlock = document.querySelector('.header__search-result')
const resultCourseEl = document.querySelector('.result__content ul')

findCourseEl.addEventListener('input', (e) => {
    q = e.target.value.trim()
    if (q.length >= 2) {
        resultCourseBlock.setAttribute('style', 'display:block')
        pathDomain = document.location.origin
        path = document.location.origin + `/api/course/?q=${q}`
        console.log(path)
        
        fetch(path)
            .then(data => data.json())
            .then(data => {
                content = ''
                if (data.length == 0) {

                    return resultCourseEl.innerHTML = `<li>
                            <li>Không tìm thấy khóa học</li>
                        </li>`
                }
                data.forEach(course => {
                    content = content + `<li>
                                <a href="${document.location.origin}/course/${course.pk}">
                                    <img src="${pathDomain}/static/${course.fields.image}" alt="">
                                    <span>${course.fields.subject}</span>
                                </a>
                            </li>`
                    console.log(course);
                });
                resultCourseEl.innerHTML = content
            });
        


        
    } else {
        resultCourseBlock.setAttribute('style','display:none')
        
    }
});