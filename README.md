# Ultrasound-Nerve-Segmentation

Dataset taken from https://www.kaggle.com/c/ultrasound-nerve-segmentation
Ultrasound nerve images of the neck region
The dataset is in data/ folder and has only 10 images in both test/ and train/ folders please download full dataset if needed and follow same directory structure

Run programs as (please refers to logs provided)
data.py - load data, create numpy binaries
train.py - generate weights.h5 and model.h5 (trained using data/train/ folder)
summary.py - see a summary of our trained model
predict.py - images from data/test/ outputs are predicted to preds/ folder
predict.py takes 2 or more numeric command line arguments to show images from test which are predicted in preds/ folder

Example
python3 predict.py 13 15 17
gives 6 images as output the 13th, 15th, 17th image(ultrasound input image) on the left
and 3 black and white images on the right, the white region denoting where the required nerve is present in the orginal image.
