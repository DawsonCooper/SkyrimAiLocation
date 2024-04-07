import cv2
import sys
import os 

def main():
    
    path = "./photos"
    for subFolder in os.listdir(path):
            print(subFolder)

            #subfolder would be a list of the subfolder paths [0,1,2,3...]
            subFolderPath = os.path.join(path, subFolder)
            if os.path.isdir(subFolderPath):
                counter = 0
                for imageFiles in os.listdir(subFolderPath):
                    counter += 1

                    filePath = os.path.join(subFolderPath, imageFiles)
                    os.rename(filePath, os.path.join(subFolderPath, f"77104{counter}.jpg"))

                
if __name__ == "__main__":
    main()