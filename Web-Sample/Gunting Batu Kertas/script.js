const button = document.querySelectorAll('.pilihan-player button');

const pilKomputer = document.querySelector('.komputer-memilih p');
const pilPlayer = document.querySelector('.kamu-memilih p');
const keterangan = document.querySelector('.hasil p');

const btnMainLagi = document.querySelector('button.main-lagi');


mulaiGame()
button.forEach(function(pilihanPlayer){
	pilihanPlayer.addEventListener('click', function(){
		const player = pilihanPlayer.className;
		const komputer = pilihanKomputer();
		const hasil = fight(player,komputer);

		let fightLoading = keterangan.innerHTML = 'fight!' ;
		grey();

		setTimeout(function(){
			togglePilihan();
		}, 100)
		const delay = setInterval(function(){
			keterangan.innerHTML = fightLoading += ' .' ;
		}, 400)
		setTimeout(function(){
			clearInterval(delay);
			tampilkanKeterangan(komputer,player,'kamu '+hasil+' !')
			grey();
		}, 1600)
		setTimeout(function(){
			mainLagi();
		}, 1800)
	})
})
btnMainLagi.addEventListener('click', function(){
	mulaiGame();
});

// ---FUNCTION---
function mulaiGame(){
	tampilkanKeterangan('--','--','--')
	mainLagi()
	setTimeout(function(){
		keterangan.innerHTML = 'mulai!' ;
		togglePilihan()
	}, 300)
}
function pilihanKomputer() {
	const angkaRandom = Math.random();
	if (angkaRandom <= 1/3) return 'batu';
	if (angkaRandom > 1/3 && angkaRandom <= 2/3) return 'gunting';
	return 'kertas';
}
// rules
function fight(p,k) {
	if (p == k) return 'seri';
	if (p == 'batu') return (k == 'gunting') ? 'menang':'kalah';
	if (p == 'gunting') return (k == 'kertas') ? 'menang':'kalah';
	return (k == 'batu') ? 'menang':'kalah';
}
function tampilkanKeterangan(pKomputer,pPlayer,pKeterangan) {
	pilKomputer.innerHTML = pKomputer;
	pilPlayer.innerHTML = pPlayer;
	keterangan.innerHTML = pKeterangan ;
}
// toggle function
function togglePilihan() {
	const divPilihan = document.querySelector('.pilihan-player');
	divPilihan.classList.toggle('hidden');
}
function mainLagi() {
	btnMainLagi.classList.toggle('hidden');
}
function grey() {
	keterangan.classList.toggle('text-grey');
}