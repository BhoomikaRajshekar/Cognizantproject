#Program to save mouse clicks as locations for overlaying in csv format using for loop

import cv2
import csv
import os

# Global variables to store mouse click coordinates and overlay path
click_data = []

current =os.getcwd()
#print(current)

images=os.listdir()
bgimages=[]
for i in images:
    if i.startswith('bg'):
        bgimages.append(i)
#print(bgimages)
sofas=[]
for i in images:
    if i.startswith('sofa'):
        sofas.append(i)
#print(sofas)
lamps=[]
for i in images:
    if i.startswith('lamp'):
        lamps.append(i)
#print(lamps)
wd=[]
for i in images:
    if i.startswith('wd'):
        wd.append(i)
#print(wd)
plants=[]
for i in images:
    if i.startswith('plant'):
        plants.append(i)
#print(plants)
tables=[]
for i in images:
    if i.startswith('table'):
        tables.append(i)
#print(tables)





# Mouse click callback function
def mouse_click(event, x, y, flags, param):
    global click_data
    if event == cv2.EVENT_LBUTTONDOWN:
        click_data.append((x, y, overlay_path))
        print(f"Clicked at ({x}, {y}) with overlay path: {overlay_path}")

# Load overlay image paths
overlay_paths = [lamps[0],lamps[1],lamps[2],lamps[3],lamps[4],lamps[5], sofas[0],sofas[1],sofas[2],sofas[3],sofas[4], wd[0],wd[1],wd[2],wd[3],wd[4],wd[5], tables[0],tables[1],tables[2],tables[3], plants[0],plants[1],plants[2],plants[3]]

# Create a window to display the background image
cv2.namedWindow("Background Image")
for overlay_path in overlay_paths:
    # Load background image
    background_path = bgimages[0]  # Replace with the path to your background image
    
    background = cv2.imread(background_path)

    # Create a copy of the background image for display
    background_display = background.copy()

    cv2.setMouseCallback("Background Image", mouse_click)

    print(f"Click on the background image to select locations for overlay: {overlay_path}. Press 'Esc' to continue to the next overlay.")

    while True:
        cv2.imshow("Background Image", background_display)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # Press 'Esc' to continue to the next overlay
            break

# Save click data (coordinates and overlay path) to a CSV file
csv_filename = "annotations2.csv"
with open(csv_filename, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for x, y, path in click_data:
        csv_writer.writerow([path, x, y])

cv2.destroyAllWindows()
