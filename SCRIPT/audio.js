 // Code JavaScript pour le lecteur audio en direct
 var audioPlayer = new Audio('URL_DU_FLUX_EN_DIRECT');
 audioPlayer.controls = true;
 document.getElementById('live-stream').appendChild(audioPlayer);
