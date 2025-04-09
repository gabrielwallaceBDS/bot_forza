import time
import threading
import pyautogui
import pygetwindow as gw
import tkinter as tk
from tkinter import ttk

try:
    from pynput import keyboard
except ImportError:
    keyboard = None

running = False
status_label = None
log_text = None

def delay(segundos=1.0):
    time.sleep(segundos)

def log(mensagem):
    if log_text:
        log_text.insert(tk.END, f"{mensagem}\n")
        log_text.see(tk.END)

def ativar_janela_jogo():
    janela = gw.getWindowsWithTitle('Título da Janela do Jogo')
    if janela:
        try:
            janela[0].activate()
        except:
            janela[0].minimize()
            janela[0].maximize()
        time.sleep(0.5)  # Pequeno atraso para garantir que a janela esteja ativa
    else:
        log("Janela do jogo não encontrada.")

def executar_bot():
    global running
    tentativa = 1
    while running:
        log(f"🔁 Tentativa {tentativa}")

        ativar_janela_jogo()

        pyautogui.press('enter')
        log("Pressionando Enter (iniciar busca)")
        delay()

        pyautogui.press('enter')
        log("Pressionando Enter (confirmar busca)")
        delay()

        try:
            inicio = time.time()
            encontrado = False
            while time.time() - inicio < 5:
                if pyautogui.locateOnScreen('nenhum_leilao.png', confidence=0.8):
                    encontrado = True
                    break
            if encontrado:
                log("Nenhum leilão para exibir.")
                pyautogui.press('esc')
                log("Pressionando Esc (voltar)")
                delay()
                pyautogui.press('enter')
                log("Pressionando Enter (nova pesquisa)")
                delay()
                pyautogui.press('enter')
                log("Pressionando Enter (confirmar nova pesquisa)")
                delay()
                tentativa += 1
                continue
        except:
            log("🟢 Carro disponível - prosseguindo para compra")

        log("🚗 Carro encontrado! Iniciando compra...")

        pyautogui.press('y')
        log("Pressionando Y (abrir menu)")
        delay()

        pyautogui.press('down')
        log("Pressionando ↓ (selecionar 'Comprar agora')")
        delay()

        pyautogui.press('enter')
        log("Pressionando Enter (selecionar)")
        delay()

        pyautogui.press('enter')
        log("Pressionando Enter (confirmar compra)")
        delay()

        time.sleep(4)  # Aguarda 4 segundos antes de fechar a mensagem de sucesso
        pyautogui.press('enter')
        log("Pressionando Enter (fechar mensagem de sucesso)")
        delay()

        pyautogui.press('esc')
        log("Pressionando Esc (sair)")
        delay()

        pyautogui.press('esc')
        log("Pressionando Esc (voltar para pesquisa)")
        delay()

        pyautogui.press('enter')
        log("Pressionando Enter (nova pesquisa)")
        delay()

        pyautogui.press('enter')
        log("Pressionando Enter (confirmar nova pesquisa)")
        delay()

        tentativa += 1

def iniciar():
    global running
    if not running:
        running = True
        if status_label:
            status_label.config(text="Iniciando em 3 segundos...")
        time.sleep(3)
        threading.Thread(target=executar_bot, daemon=True).start()
        if status_label:
            status_label.config(text="Status: Rodando")

def parar():
    global running
    running = False
    if status_label:
        status_label.config(text="Status: Parado")
    log("⛔ Bot parado.")

def alternar_com_tecla():
    if running:
        parar()
    else:
        iniciar()

def on_key_press(key):
    try:
        if hasattr(key, 'char') and key.char and key.char.lower() == 'p':
            alternar_com_tecla()
    except:
        pass

def start_key_listener():
    if keyboard is not None:
        try:
            listener = keyboard.Listener(on_press=on_key_press)
            listener.daemon = True
            listener.start()
        except:
            pass

def criar_interface():
    global status_label, log_text
    root = tk.Tk()
    root.title("Bot Leilão FH5")
    root.geometry("400x300")

    ttk.Button(root, text="Iniciar Bot", command=iniciar).pack(pady=10)
    ttk.Button(root, text="Parar Bot", command=parar).pack(pady=5)
    status_label = ttk.Label(root, text="Status: Parado")
    status_label.pack(pady=5)

    ttk.Label(root, text="Atalho: Tecla 'P' para Iniciar/Parar").pack()

    log_frame = ttk.LabelFrame(root, text="Logs")
    log_frame.pack(padx=10, pady=10, fill="both", expand=True)

    log_text = tk.Text(log_frame, height=10, wrap="word", state="normal")
    log_text.pack(expand=True, fill="both")

    start_key_listener()
    root.mainloop()

criar_interface()
