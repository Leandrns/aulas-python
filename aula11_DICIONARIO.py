emojis = {
    ':)': '😊',
    ':(': '🙁',
    ':D': '😀',
    ':P': '😋',
    ':x': '😗',
    ':|': '😐',
    '<3': '🤍'
}

resp = input('Digite uma frase com emojis de caracteres do teclado: ')
for key in emojis.keys():
    resp = resp.replace(key, emojis[key])
print(resp)
