import pyautogui, time

# Aguardar antes de iniciar
print("Inicia em 5 segundos...")
time.sleep(5)

# Número de repetições por mensagem
X = 5 

# Abrir o arquivo txt
with open('repetir.txt', encoding='utf8') as texto:
    for frase in texto:
        for _ in range(X):
            pyautogui.typewrite(frase)
            pyautogui.press('enter')
            time.sleep(0.2)  # Adiciona um intervalo entre as mensagens (opcional)

print("Mensagens enviadas com sucesso!")
