from PIL import Image
import numpy as np

# Open the maze image and make greyscale, and get its dimensions
im = Image.open('/Volumes/A:/MIU CS/S22/Algorithm Analysis & Design 2 CSC315/Project/maze 19.png').convert('L')
w, h = im.size

# Ensure all black pixels are 0 and all white pixels are 1
binary = im.point(lambda p: p > 240 and 1)

# Resize to half its height and width so we can fit on Stack Overflow, get new dimensions
binary = binary.resize((w//3,h//3),Image.NEAREST)
w, h = binary.size

# Convert to Numpy array - because that's how images are best stored and processed in Python
nim = np.array(binary)

# Print that puppy out 
for r in range(h):
    for c in range(w):
        print(nim[r,c],end='')
    print()
