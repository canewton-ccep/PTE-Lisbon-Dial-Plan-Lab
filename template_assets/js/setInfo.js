info = JSON.parse(atob(window.location.search.slice(1)))
Object.keys(info).forEach(key=> {sessionStorage.setItem(key, info[key])})
window.location.search = ""