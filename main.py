import argparse
import cv2
from inference import Network
import numpy as np
import math
import time
from datetime import datetime
from matplotlib import pyplot as plt

#The directory for xml and bin file 
INPUT_STREAM = "./intel/emotions-recognition-retail-0003/FP32/emotions-recognition-retail-0003.xml"

#location to store the graph
save_graph="./data/"

#An array containing the feelings measured
feelings = ["neutral", "happy", "sad", "surprise", "anger"]
#A counter to conclude the emotions after a session
feelingsScore=[0,0,0,0,0]

def infer_on_video():
    '''
    Function Use:
    Main Function that does everything.
    Load and infers on the model.
    Makes a graph and saves it.
    '''
    plugin = Network()
    # Load the model  
    plugin.load_model(INPUT_STREAM,"CPU")
    input_shape = plugin.get_input_shape()
    # Get and open video capture
    cap = cv2.VideoCapture(0)
    frameRate=cap.get(5)
    # Set it ot webcam
    cap.open(0)
    
    # Grab the shape of the input
    width = int(cap.get(3))
    height = int(cap.get(4))
    count=1
    start=time.time()
    # Process frames until the video ends, or process is exited
    while cap.isOpened():
        try:
            # Read the next frame
            flag, frame = cap.read()
            if not flag:
                break
            key_pressed = cv2.waitKey(20)

            #Pre-process the frame
            pre_proccessed_frame = cv2.resize(
                frame, (input_shape[3], input_shape[2]))
            pre_proccessed_frame = pre_proccessed_frame.transpose((2, 0, 1))
            pre_proccessed_frame = pre_proccessed_frame.reshape(1,*pre_proccessed_frame.shape)
            #Perform inference on the frame
            plugin.async_inference(pre_proccessed_frame)
            #Get the output of inference
            if plugin.wait() == 0:
                res = plugin.extract_output()
            #Update the frame to include detected bounding boxes
            feelingsScore[np.argmax(res[0])]+=1
            # Break if escape key pressed
            print(feelingsScore)
            if key_pressed == 27:
                break
        except KeyboardInterrupt:
                break
    #To obtain the total time duration
    end=time.time()
    dateTimeObj = datetime.now()
    
    # Time stamp of current session
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")
    # Colors for the graph
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red']
    title=timestampStr+'\n'+"Time Duration:"+"{0:.2f}".format((end-start)/(60*60))+"hr"
    # Plot with various details
    plt.title(title, fontdict=None, loc='center', pad=None)
    plt.pie(feelingsScore, labels=feelings, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
    plt.legend(feelings,loc="best")
    plt.axis('equal')
    # Saving the graph to data directory with timestamp as name in png format
    plt.savefig(save_graph+dateTimeObj.strftime("%d-%b-%Y-%H-%M")+".png")
    plt.show()
    # Destroys the current opened windows
    cap.release()
    cv2.destroyAllWindows()
    
def main():
    infer_on_video()


if __name__ == "__main__":
    main()
