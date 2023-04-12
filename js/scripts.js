window.addEventListener('load', function() {
    let selectCards = document.querySelectorAll('.information-select__card');
    let content = document.querySelectorAll('.information');
    let headerBtns = document.querySelectorAll('.header__navigation-btn')
    let mainSections = document.querySelectorAll('.main-section')
    
    selectCards.forEach(item => item.addEventListener('click', e => {
        let selectCardsTarget = e.target.getAttribute('data-card');
        selectCards.forEach(el => el.classList.remove('is-active'));
        content.forEach(el => el.classList.remove('is-active'));
        item.classList.add('is-active');
        document.getElementById(selectCardsTarget).classList.add('is-active');
    }));

    headerBtns.forEach(item => item.addEventListener('click', e => {

        // Prevent default behaviour - reload
        e.preventDefault()

        let targetId = 'main-' + e.target.getAttribute('for')
        
        mainSections.forEach(item => {

            item.classList.remove('is-active')

            if (item.id == targetId) {
                item.classList.add('is-active')
            }
        })

        headerBtns.forEach(item => item.classList.remove('is-active'))
        e.target.classList.add('is-active')
    }))

    document.querySelectorAll('.information-rules__title').forEach((el) => {
        el.addEventListener('click', () => {
            const parent = el.parentNode;
            if (parent.classList.contains('information-rules__main_active')) {
                parent.classList.remove('information-rules__main_active');
            } else {
                document.querySelectorAll('.information-rules__main').forEach((child) => child.classList.remove('information-rules__main_active'))
                parent.classList.add('information-rules__main_active');
            }
            // parent.classList.toggle('information-rules__main_active');
            
        })
    });
});