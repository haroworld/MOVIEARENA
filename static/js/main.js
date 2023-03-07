btn = document.getElementById('menu-btn');
mobile_nav = document.getElementById('mobile-nav');


btn.addEventListener('click', onClick);



function onClick(e){
    btn.classList.toggle('open')
    mobile_nav.classList.toggle('flex')
    mobile_nav.classList.toggle('hidden')
};

dropbtn = document.getElementById('drop-btn');
dropnav = document.getElementById('drop-nav');
btnup = document.getElementById('btn-up');


dropbtn.addEventListener('click', clickDrop);
btnup.addEventListener('click', clickUP);


function clickDrop(e){
    dropnav.classList.toggle('hidden');
    btnup.classList.toggle('hidden');
    dropbtn.classList.toggle('hidden');
}

function clickUP(e){
    dropnav.classList.toggle('hidden');
    btnup.classList.toggle('hidden');
    dropbtn.classList.toggle('hidden');
}


