import cv2
import numpy as np
import os
import csv

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

    os.chdir('selected')
    #print(os.getcwd())
    images=os.listdir()
    #print(images)
    bgimages=[]
    for i in images:
        if i.startswith('bg'):
           bgimages.append(i)

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


    background_path = bgimages[0]
    background = cv2.imread(background_path)
    if background is None:
        print(f"Error: Could not load background image '{background_path}'")
        exit()

    overlay_count = 3
    overlays = []
    overlays1= []
    overlays2= []

    overlay_plant=plants[0]
    overlay_wd=wd[0]
    overlay_lamps=lamps[0]
    overlay_sofa=sofas[0]
    overlay_table=tables[0]

    if overlay_plant not in annotations:
        print(f"No coordinates found for overlay image '{overlay_path}' in annotations.csv")
        exit()
    if overlay_wd not in annotations1:
        print(f"No coordinates found for overlay image '{overlay_path}' in annotations1.csv")
        exit()
    if overlay_lamps not in annotations2:
        print(f"No coordinates found for overlay image '{overlay_path}' in annotations2.csv")
        exit()
    if overlay_sofa not in annotations2:
        print(f"No coordinates found for overlay image '{overlay_path}' in annotations2.csv")
        exit()
    if overlay_table not in annotations2:
        print(f"No coordinates found for overlay image '{overlay_path}' in annotations2.csv")
        exit()

    x, y = annotations[overlay_plant]
    overlays.append((overlay_plant, x, y))
    x, y = annotations[overlay_lamps]
    overlays.append((overlay_lamps, x, y))
    x, y = annotations[overlay_wd]
    overlays.append((overlay_wd, x, y))
    x, y = annotations[overlay_sofa]
    overlays.append((overlay_sofa, x, y))
    x, y = annotations[overlay_table]
    overlays.append((overlay_table, x, y))
        
    x1, y1= annotations1[overlay_plant]
    overlays1.append((overlay_plant, x1, y1))
    x1, y1= annotations1[overlay_lamps]
    overlays1.append((overlay_lamps, x1, y1))
    x1, y1= annotations1[overlay_wd]
    overlays1.append((overlay_wd, x1, y1))
    x1, y1= annotations1[overlay_sofa]
    overlays1.append((overlay_sofa, x1, y1))
    x1, y1= annotations1[overlay_table]
    overlays1.append((overlay_table, x1, y1))

        
    x2, y2= annotations2[overlay_plant]
    overlays2.append((overlay_plant, x2, y2))
    x2, y2= annotations2[overlay_lamps]
    overlays2.append((overlay_lamps, x2, y2))
    x2, y2= annotations2[overlay_wd]
    overlays2.append((overlay_wd, x2, y2))
    x2, y2= annotations2[overlay_sofa]
    overlays2.append((overlay_sofa, x2, y2))
    x2, y2= annotations2[overlay_table]
    overlays2.append((overlay_table, x2, y2))

    result_image = overlay_images(background, overlays)
    result_image1 = overlay_images1(background, overlays1)
    result_image2 = overlay_images2(background, overlays2)
    output_path = 'useroutput'

    # Save image1
    cv2.imwrite(os.path.join(output_path, 'image1.jpg'), result_image)

    # Save image2
    cv2.imwrite(os.path.join(output_path, 'image2.jpg'), result_image1)

    # Save image3
    cv2.imwrite(os.path.join(output_path, 'image3.jpg'), result_image2)

    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #save_option = input("Do you want to save this result (y/n)? ")
    #if save_option.lower() == 'y':
        #save_path = input("Enter the path to save the result image: ")
        #cv2.imwrite(save_path, result_image)
        #print("Result image saved.")


if __name__ == '__main__':
    main()
