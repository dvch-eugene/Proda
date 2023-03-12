function enter() {
    document.getElementById('save-note').click()
  }

document.querySelector('textarea').addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      e.preventDefault()
      enter()
      return
    }
  })