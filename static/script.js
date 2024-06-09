// var today = document.getElementById('date')

var today = document.getElementById('datetime')
const now = new Date()

var date = now.getDate()
var month = now.getMonth()
var year = now.getFullYear()

let fulldate = date + "-" + month + "-" + year

today.innerHTML = fulldate
today.value = fulldate