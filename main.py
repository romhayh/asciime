import cv2
import numpy as np
from numba import njit
from keyboard import is_pressed
from time import sleep

STRING = '$@B%8&WM#''*''oahkbdpqwmZ0QOLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. '
INTENSITIES = np.array([c for c in reversed([c for c in STRING])])
def clear():
    import os 
    os.system('cls' if os.name == 'nt' else 'clear')    
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

@njit
def intensityToAscii(intensity):
    N = len(INTENSITIES)
    return INTENSITIES[np.int0((N / 255) * intensity)]
    
def toAscii(img: np.ndarray):
    for x in img:
        for i in x:
            c = intensityToAscii(i)
            print(c, end='::' if c != ' ' else '  ')
        print('\n', end='') 

def prepareImage(img: np.ndarray):
    
    RATIO = img.shape[1] / img.shape[0]
    WIDTH = 380
    HEIGHT = int(WIDTH * RATIO)
    SIZE = (WIDTH, HEIGHT)
    
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.resize(img1, SIZE)
    

def fromVideo():
    cap = cv2.VideoCapture(0)
    _, img = cap.read()
    RATIO = img.shape[1] / img.shape[0]
    WIDTH = 100
    HEIGHT = int(WIDTH * RATIO)
    SIZE = (WIDTH, HEIGHT)
    
    while True:
        
        _, img = cap.read()
        
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        img = cv2.resize(img, SIZE)
        
        toAscii(img)
        
        
        if is_pressed('q'):
            break
        else:
            sleep(0.1)
            clear()
        
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    clear()
    img = cv2.imread(r'D:\vscode workspace\asciiMe\NOAM.jpeg')
    img = prepareImage(img)
    toAscii(img)
    
    