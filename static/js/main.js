/* Script for search form and page links */
let searchForm = document.getElementById('searchForm');
let pageLinks = document.getElementsByClassName('page-link');
let incSearch = document.getElementById('incSearch');

if (incSearch) {
    for (let i = 0; pageLinks.length > i; i++) {
        pageLinks[i].addEventListener('click', function (e) {
            e.preventDefault();
            let page = this.dataset.page;
            searchForm.innerHTML += `<input value="${page}" name="page" hidden>`;
            searchForm.submit();
        });
    }
}