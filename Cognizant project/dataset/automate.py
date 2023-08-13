import cv2
import numpy as np
import os
import csv
import random

def overlay_images(background, overlays):
    result = np.copy(background)

    for overlay_path, x, y in overlays:
        overlay = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)
        if overlay is None:
            print(f"Error: Could not load overlay image '{overlay_path}'")
            continue

        h, w, _ = overlay.shape
        overlay = cv2.resize(overlay, (w, h))

        x_top_left = x - w // 2
        y_top_left = y - h // 2

        overlay_alpha = overlay[:, :, 3] / 255.0  # Use alpha channel as blending factor
        
        # Resize overlay_alpha to match overlay_roi dimensions
        overlay_alpha = cv2.resize(overlay_alpha, (w, h))

        # Create regions of interest (ROI) for overlay and result images
        overlay_roi = overlay[:, :, :3]
        result_roi = result[y_top_left:y_top_left+h, x_top_left:x_top_left+w]

        result_roi = overlay_alpha[:, :, np.newaxis] * overlay_roi + (1 - overlay_alpha[:, :, np.newaxis]) * result_roi

        result[y_top_left:y_top_left+h, x_top_left:x_top_left+w] = result_roi.astype(np.uint8)

    return result

#----------------------------------------------------------------------------------------------------------------

def overlay_images1(background, overlays):
    result1 = np.copy(background)

    for overlay_path, x, y in overlays:
        overlay1 = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)
        if overlay1 is None:
            print(f"Error: Could not load overlay image '{overlay_path}'")
            continue

        h1, w1, _ = overlay1.shape
        overlay1 = cv2.resize(overlay1, (w1, h1))

        x_top_left1 = x - w1 // 2
        y_top_left1 = y - h1 // 2

        overlay_alpha1 = overlay1[:, :, 3] / 255.0  # Use alpha channel as blending factor

        # Resize overlay_alpha to match overlay_roi dimensions
        overlay_alpha1 = cv2.resize(overlay_alpha1, (w1, h1))

        # Create regions of interest (ROI) for overlay and result images
        overlay_roi1 = overlay1[:, :, :3]
        result_roi1 = result1[y_top_left1:y_top_left1+h1, x_top_left1:x_top_left1+w1]

        result_roi1 = overlay_alpha1[:, :, np.newaxis] * overlay_roi1 + (1 - overlay_alpha1[:, :, np.newaxis]) * result_roi1
        
        result1[y_top_left1:y_top_left1+h1, x_top_left1:x_top_left1+w1] = result_roi1.astype(np.uint8)

    return result1

#----------------------------------------------------------------------------------------------------------------------

def overlay_images2(background, overlays):
    result2 = np.copy(background)

    for overlay_path, x, y in overlays:
        overlay2 = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)
        if overlay2 is None:
            print(f"Error: Could not load overlay image '{overlay_path}'")
            continue

        h2, w2, _ = overlay2.shape
        overlay2 = cv2.resize(overlay2, (w2, h2))

        x_top_left2 = x - w2 // 2
        y_top_left2 = y - h2 // 2

        overlay_alpha2 = overlay2[:, :, 3] / 255.0  # Use alpha channel as blending factor

        # Resize overlay_alpha to match overlay_roi dimensions
        overlay_alpha2 = cv2.resize(overlay_alpha2, (w2, h2))

        # Create regions of interest (ROI) for overlay and result images
        overlay_roi2 = overlay2[:, :, :3]
        result_roi2 = result2[y_top_left2:y_top_left2+h2, x_top_left2:x_top_left2+w2]

        result_roi2 = overlay_alpha2[:, :, np.newaxis] * overlay_roi2 + (1 - overlay_alpha2[:, :, np.newaxis]) * result_roi2
        
        result2[y_top_left2:y_top_left2+h2, x_top_left2:x_top_left2+w2] = result_roi2.astype(np.uint8)

    return result2

#-------------------------------------------------------------------------------------------------------------

def main():
    annotations = {}
    annotations1 = {}
    annotations2 = {}
    with open('annotations.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            annotations[row[0]] = (int(row[1]), int(row[2]))
    with open('annotations1.csv', 'r') as csv_file1:
        csv_reader1 = csv.reader(csv_file1)
        for row in csv_reader1:
            annotations1[row[0]] = (int(row[1]), int(row[2]))
    with open('annotations2.csv', 'r') as csv_file2:
        csv_reader2 = csv.reader(csv_file2)
        for row in csv_reader2:
            annotations2[row[0]] = (int(row[1]), int(row[2]))

    images=os.listdir()
    bgimages=[]
    for i in images:
        if i.startswith('bg'):
           bgimages.append(i)
    

    # Access elements randomly using random indices
    for _ in range(1):
        background_path = random.choice(bgimages)
        background_path1 = random.choice(bgimages)
        background_path2 = random.choice(bgimages)
        
    background = cv2.imread(background_path)
    background1 = cv2.imread(background_path1)
    background2 = cv2.imread(background_path2)
    if background is None:
        print(f"Error: Could not load background image '{background_path}'")
        exit()

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
    overlays = []
    overlays1= []
    overlays2= []
    overlay_count=5

    for _ in range(1):
        for _ in range(len(plants)):
            overlay_plant1 = random.choice(plants)
            overlay_plant2 = random.choice(plants)
            overlay_plant3 = random.choice(plants)
        for _ in range(len(wd)):
            overlay_wd1 = random.choice(wd)
            overlay_wd2 = random.choice(wd)
            overlay_wd3 = random.choice(wd)
        for _ in range(len(lamps)):
            overlay_lamps1 = random.choice(lamps)
            overlay_lamps2 = random.choice(lamps)
            overlay_lamps3 = random.choice(lamps)
        for _ in range(len(sofas)):
            overlay_sofa1 = random.choice(sofas)
            overlay_sofa2 = random.choice(sofas)
            overlay_sofa3 = random.choice(sofas)
        for _ in range(len(tables)):
            overlay_tab1 = random.choice(tables)
            overlay_tab2 = random.choice(tables)
            overlay_tab3 = random.choice(tables)
        
        x, y = annotations[overlay_plant1]
        overlays.append((overlay_plant1, x, y))
        x, y = annotations[overlay_lamps1]
        overlays.append((overlay_lamps1, x, y))
        x, y = annotations[overlay_wd1]
        overlays.append((overlay_wd1, x, y))
        x, y = annotations[overlay_sofa1]
        overlays.append((overlay_sofa1, x, y))
        x, y = annotations[overlay_tab1]
        overlays.append((overlay_tab1, x, y))
        

        x1, y1= annotations1[overlay_plant2]
        overlays1.append((overlay_plant2, x1, y1))
        x1, y1= annotations1[overlay_lamps2]
        overlays1.append((overlay_lamps2, x1, y1))
        x1, y1= annotations1[overlay_wd2]
        overlays1.append((overlay_wd2, x1, y1))
        x1, y1= annotations1[overlay_sofa2]
        overlays1.append((overlay_sofa2, x1, y1))
        x1, y1= annotations1[overlay_tab2]
        overlays1.append((overlay_tab2, x1, y1))
        
        
        x2, y2= annotations2[overlay_plant3]
        overlays2.append((overlay_plant3, x2, y2))
        x2, y2= annotations2[overlay_lamps3]
        overlays2.append((overlay_lamps3, x2, y2))
        x2, y2= annotations2[overlay_wd3]
        overlays2.append((overlay_wd3, x2, y2))
        x2, y2= annotations2[overlay_sofa3]
        overlays2.append((overlay_sofa3, x2, y2))
        x2, y2= annotations2[overlay_tab3]
        overlays2.append((overlay_tab3, x2, y2))
        

    result_image = overlay_images(background, overlays)
    result_image1 = overlay_images1(background1, overlays1)
    result_image2 = overlay_images2(background2, overlays2)
    cv2.imshow('Result', result_image)
    cv2.imshow('Result1', result_image1)
    cv2.imshow('Result2', result_image2)
    cv2.imwrite('output1.png',result_image)
    cv2.imwrite('output2.png',result_image1)
    cv2.imwrite('output3.png',result_image2)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
        


if __name__ == '__main__':
    main()
