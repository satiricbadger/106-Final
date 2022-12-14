var element = document.getElementsByClassName('post-tags');

for (var i = 0; i < element.length; i++) {

    if (element[i].textContent == 'anime') {

        element[i].innerHTML = '<span class="anime-tag">#anime</span>'

    } else if (element[i].textContent == 'games') {

        element[i].innerHTML = '<span class="game-tag">#games</span>'

    } else if (element[i].textContent == 'both') {

        element[i].innerHTML = '<span class="game-tag">#games</span> <span class="anime-tag">#anime</span>'

    }
}
