const fileInput=document.getElementById("image")
window.addEventListener('paste',e => {
	fileInput.files=e.clipboardData.files;
})
