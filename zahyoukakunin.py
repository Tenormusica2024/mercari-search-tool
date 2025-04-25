import pyautogui
import time

print("5秒後に座標取得を開始します...")
time.sleep(5)

try:
    while True:
        x, y = pyautogui.position()
        position_str = f"X: {x} Y: {y}"
        print(position_str, end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\n終了しました")