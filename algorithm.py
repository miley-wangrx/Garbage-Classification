# -*- coding: utf-8 -*-
"""test01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1suKs-Ts2dvYwD81ux-azgR9b64kRSlN8
"""

import torch
import torchvision.models as models
import torch.nn as nn
from PIL import Image
from pathlib import Path
from torchvision.datasets import ImageFolder
import torchvision.transforms as transforms
from ResNet import ResNet


# from google.colab import drive
# drive.mount('/content/drive')
#data_dir = "drive/MyDrive/Colab Notebooks/garbagecollection/Garbage classification"

# model_path = "drive/MyDrive/Colab Notebooks/garbagecollection/Garbage classification/model01.pt"

# image_path = "/content/images.jpeg"

# data_path = "drive/MyDrive/Colab Notebooks/garbagecollection/Garbage classification"

# class ResNet(nn.Module):
#     def __init__(self):
#         super().__init__()
#         # Use a pretrained model
#         self.network = models.resnet50(pretrained=True)
#         # Replace last layer
#         num_ftrs = self.network.fc.in_features
#         self.network.fc = nn.Linear(num_ftrs, 6)
    
#     def forward(self, xb):
#         return torch.sigmoid(self.network(xb))



def get_default_device_and_load(model_path):
    model = ResNet()
    #model.load_state_dict(torch.load('model_weights.pth'))
    # if torch.cuda.is_available():
    #     model.load_state_dict(torch.load('model_weights.pth'))
    # else:
    #     model.load_state_dict(torch.load('model_weights.pth'), map_location=torch.device('cpu'))
    device = torch.device('cpu')
    model.load_state_dict(torch.load('model_weights1.pth',map_location='cpu'))
    model.eval()
    #model = torch.load('model01.pt',map_location='cpu')
    return model

def process_data(data_path):
    data_dir = data_path
    transformations = transforms.Compose([transforms.Resize((256, 256)), transforms.ToTensor()])
    dataset = ImageFolder(data_dir, transform = transformations)
    return dataset

def predict_image(img, model, dataset):
    
    def get_default_device():
      if torch.cuda.is_available():
          return torch.device('cuda')
      else:
          return torch.device('cpu')
    def to_device(data, device):
      if isinstance(data, (list,tuple)):
        return [to_device(x, device) for x in data]
      return data.to(device, non_blocking=True)
    device = get_default_device()

    # Convert to a batch of 1
    xb = to_device(img.unsqueeze(0), device)
    # Get predictions from model
    yb = model(xb)
    
    # Pick index with highest probability
    prob, preds  = torch.max(yb, dim=1)
    print(prob, preds)
    # Retrieve the class label
    #print(dataset.classes[preds[0].item()])
    return dataset.classes[preds[0].item()]

def make_prediction(model,dataset, image_path:str):
    image = Image.open(Path(image_path))
    transformations = transforms.Compose([transforms.Resize((256, 256)), transforms.ToTensor()])
    example_image = transformations(image)
    return predict_image(example_image, model, dataset)


def run(image_path, model_path, data_path):
    dataset = process_data(data_path)
    model = get_default_device_and_load(model_path)
    result =  make_prediction(model, dataset, image_path)
    return result