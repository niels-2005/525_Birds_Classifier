# CV_525_Birds_Classifier

Welcome to the **CV_525_Birds_Classifier** repository! This project is designed to classify 525 different bird species using deep learning techniques and a comprehensive dataset of bird images. The aim is to leverage TensorFlow and EfficientNetB7 for efficient and accurate image classification.

## Project Overview

**CV_525_Birds_Classifier** utilizes TensorFlow's powerful image processing capabilities and the EfficientNetB7 architecture to create a robust model capable of distinguishing among hundreds of bird species from images.

## Features

- **EfficientNetB7 Backbone**: Uses EfficientNetB7, known for its efficiency and effectiveness in image classification tasks, as the primary feature extractor.
- **Image Dataset Creation**: Processes images using TensorFlow's utilities to create training, validation, and test datasets.
- **Mixed Precision Training**: Implements TensorFlow's mixed precision training to accelerate the training process without losing the model's performance.
- **Visualization of Sample Images**: Includes scripts for displaying random samples of bird images from the dataset to verify data integrity and preprocessing steps.

## Dataset

The dataset contains images distributed across 525 categories representing different bird species. Images are preprocessed to ensure they are correctly formatted and normalized for training the deep learning model.

## Model Architecture

The model builds upon the EfficientNetB7 architecture, customized with the following layers for this specific task:
- **Global Average Pooling**: Reduces feature dimensions before classification.
- **Batch Normalization**: Normalizes the activations from the previous layer to improve learning dynamics.
- **Dropout**: Mitigates overfitting during training by randomly dropping units from the neural network.
- **Dense Output Layer**: A fully connected layer that outputs the class probabilities for each bird species.

## Training and Evaluation

- **Compilation**: The model is compiled with categorical crossentropy loss and Adam optimizer, focusing on accuracy as the primary metric.
- **Callbacks**: Includes early stopping to prevent overtraining and learning rate reduction on plateau to adjust the learning rate based on validation performance.
- **Visualization**: Training progress is visualized by plotting training and validation loss and accuracy, providing insights into the model's learning behavior.

## Conclusion

**CV_525_Birds_Classifier** demonstrates the application of advanced neural networks in fine-grained image classification. This project highlights the capabilities of modern CNN architectures like EfficientNetB7 in handling complex image data and achieving high accuracy in multi-class classification tasks.
