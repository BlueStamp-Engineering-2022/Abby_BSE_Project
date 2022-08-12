# Object Detection with Raspberry Pi
This project uses TensorFlow Lite to train a machine model that can identify moles and melanoma. With just a Raspberry Pi computer and camera module, a world of software can be employed to differentiate between cancerous and benign skin lesions. Read more about the process below.

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| Abby S | Schreiber High School | Software | Incoming Senior

<p align="center">
  <img width="352" height="352" src="https://lh3.googleusercontent.com/pw/AM-JKLV-YDfqQdp219YqTJSM2JK4ZVRv5XeBLT6ztFlJGZsdD1wkNc9OEk_qlOJHJQm_62XWkc12TH0OV2HHJdgFt36PPx9skuuckdvvVcZ83H36X_O_szLM_lKmxis8GBpkpi5IRF8vM_H9EKprgIbJb5M4=s1376-no?authuser=0">
</p>

# Third Milestone
My third milestone focused on improving the accuracy of my custom melanoma detection model. I annotated a new dataset of about 3,300 images from Kaggle using the LabelImg app. Then, I converted the image files and annotations into formats compatible with Google Colab. I followed a similar process of training the dataset in Google Colab and saving the trained model as a tflite file. This time, because of the expanded dataset, the accuracy of my model during validation and testing was much higher than that achieved by my original Milestone 2 model. When I exported my new model to my Raspberry Pi downloads and ran it in the terminal with detect.py, it was able to identify my skin mole as "benign_mole."

[![Second Milestone](https://i3.ytimg.com/vi/763d7XsoXwE/maxresdefault.jpg)](https://www.youtube.com/watch?v=763d7XsoXwE "Second Milestone")
<pre>




</pre>

# Second Milestone
My second milestone revolved around training my own custom TensorFlow Lite model. Its goal was to differentiate between benign moles and melanoma in new images such as those from my live-feed Raspberry Pi camera. I used an app from GitHub called LabelImg to annotate images of skin cancer and moles from the internet, and these annotations got saved as XML files along side the JPG image files. I uploaded them to Google Colab, separated them into training and validation sets, and used Google Colab's guidelines to train in 25 epochs and 4 batches. Once the model had been trained and evaluated, I exported it to the Downloads folder on my Raspberry Pi as a tflite file. I ran the detect.py code in the terminal (after specifying that I wanted it to use my custom newly-trained model), and the object detection app opened. This time, it could only identify images from the live-feed as "melanoma" or "benign_mole." Although its accuracy was lower than desired, my custom model ran without errors.

[![Second Milestone](https://i3.ytimg.com/vi/763d7XsoXwE/maxresdefault.jpg)](https://www.youtube.com/watch?v=763d7XsoXwE "Second Milestone")
<pre>




</pre>

# First Milestone
My first milestone started with setting up the Raspberry Pi, ribbon camera, and Dcorn desktop. An SD card was also inserted into the Pi, which provided the computer with storage and memory. Then, I wrote code in Raspberry Pi's Python editor to take a photo with the ribbon camera. After that, I used a pre-trained TensorFlow Lite model of images of common objects. This used live-feed video (from the Raspberry Pi camera) and OpenCV to process what the camera captured. In the Raspberry Pi terminal, I ran the detect.py code, which opened the object detection app. It was able to correctly identify objects such as "person," "keyboard," "phone," and more.

[![First Milestone](https://i3.ytimg.com/vi/PaVFm4ICkAI/maxresdefault.jpg)](https://www.youtube.com/watch?v=PaVFm4ICkAI "First Milestone")
<pre>




</pre>

# Starter Project
My starter project is called Simon Says and serves as a mini version of the memory game Simon. This project allowed me to practice basic soldering skills. I had some issues with melting plastic with the iron, but fortunately, this did not impact the device's ability to run. Since my main project is software-based, I probably won't be doing much soldering later on. Even so, it was fun and useful to learn the process.

[![Starter Project](https://i3.ytimg.com/vi/LiKZF35gun0/maxresdefault.jpg)](https://www.youtube.com/watch?v=LiKZF35gun0 "Starter Project")
