# SpamTxT
Spam via txt file


//////////////////////////////// SE QUISER PODE USAR:
FRASE = FRASE.STRIP() - para remover espaços ou quebras de linha.
//////////////////////////////// 

Code Example:
with open('repetir.txt', encoding='utf8') as texto:
    for frase in texto:
        FRASE = frase.strip()
          for _ in range(X):
              pyautogui.typewrite(frase)
              pyautogui.press('enter')
              time.sleep(0.2)  # Adiciona um intervalo entre as mensagens (opcional)
