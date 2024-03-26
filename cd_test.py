import pyautogui
import cv2

def get_cursor_color():
    # Get the current position of the cursor
    x, y = pyautogui.position()
    # Get the color of the pixel at the cursor position
    pixel_color = pyautogui.screenshot().getpixel((x, y))
    return pixel_color

def main():
    print("Move your cursor and click to detect color (press 'q' to quit).")
    while True:
        if cv2.waitKey(1000) & 0xFF == ord('q'):  # Press 'q' to quit
            break
        else:
            color = get_cursor_color()
            print("Pixel color at cursor position:", color)

if __name__ == "__main__":
    main()
