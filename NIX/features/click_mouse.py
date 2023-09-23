import pyautogui
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python click_mouse.py x_position y_position")
        return

    try:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    except ValueError:
        print("Invalid coordinates. Please provide integers for x_position and y_position.")
        return

    try:
        pyautogui.click(x, y)
        print(f"Clicked at ({x}, {y})")
    except pyautogui.FailSafeException:
        print("The click was canceled due to the mouse cursor reaching the corner of the screen.")

if __name__ == "__main__":
    main()
