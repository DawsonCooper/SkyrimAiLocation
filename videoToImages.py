import cv2
import sys

# output folder should be conversoin 
def main():
    # get sys args [video path, output folder, category] 
    [path, output_folder, category] = [sys.argv[1], sys.argv[2], sys.argv[3]]
    print(sys.argv)

    print(f"Path: {path} output_folder: {output_folder} category: {category}")
    separate_video_to_images(path, output_folder, category)
    
    

def separate_video_to_images(video_path, output_folder, category):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Get the frames per second (fps) of the video
    fps = video.get(cv2.CAP_PROP_FPS)

    # Initialize a counter for the image filenames
    image_counter = 0

    # Read the first frame
    success, frame = video.read()

    # Loop through the video frames
    while success:
        # mod operator to get this if condition to run every 30 iterations(frames)
        if image_counter % 30 == 0:
            image_filename = f"{output_folder}/{category}_{image_counter/30}.jpg"
            cv2.imwrite(image_filename, frame)

        # After or after we skipped this frame we read the next frame
        success, frame = video.read()

        # Increment the image counter
        image_counter += 1

    # Release the video file
    video.release()

    

    


if __name__ == "__main__":
    main()
# Example usage
# video_path = "path/to/video.mp4"
# output_folder = "path/to/output/folder"
# separate_video_to_images(video_path, output_folder)