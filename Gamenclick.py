import pyautogui
import time

# クリック前の待機時間（秒）
WAIT_TIME = 3

# クリックしたい座標
TARGET_X = 300
TARGET_Y = 225

# プログラム開始のお知らせ
print(f"{WAIT_TIME}秒後に座標 X: {TARGET_X}, Y: {TARGET_Y} をクリックします...")
time.sleep(WAIT_TIME)

# 指定座標をクリック
try:
    # 現在のマウス位置を保存
    current_x, current_y = pyautogui.position()
    print(f"現在のマウス位置: X: {current_x}, Y: {current_y}")
    
    # 指定座標へ移動してクリック
    pyautogui.click(x=TARGET_X, y=TARGET_Y)
    
    print(f"座標 X: {TARGET_X}, Y: {TARGET_Y} をクリックしました")
    
    # クリック後、少し待機してから元の位置に戻る（オプション）
    # time.sleep(0.5)
    # pyautogui.moveTo(current_x, current_y)
    # print("元のマウス位置に戻りました")
    
except Exception as e:
    print(f"エラーが発生しました: {e}")