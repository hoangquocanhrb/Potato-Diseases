import torch
from PIL import Image
import torch.nn as nn
from torch.utils.data import Dataset
import os 

class Diseasedata(Dataset):
  def __init__(self, root, transforms=None, phase='train'):
    self.root = root 
    self.phase = phase
    self.transforms = transforms 
    self.labels = list(sorted(os.listdir(os.path.join(root, phase))))
    print(self.labels)
    self.list_imgs = []
    for label in self.labels:
      imgs = list(os.listdir(os.path.join(root, phase, label)))
      for img in imgs:
        self.list_imgs.append([img, label])

  def __getitem__(self, index):
    img_path = os.path.join(self.root, self.phase, self.list_imgs[index][1], self.list_imgs[index][0])
    img = Image.open(img_path)
    label = self.list_imgs[index][1]
    
    if self.transforms is not None:
      img = self.transforms[self.phase](img)
    
    return img, self.labels.index(label)

  def __len__(self):
    return len(self.list_imgs)

# root = 'Dataset/'
# a = Diseasedata(root)
# b = a.__getitem__(5000)
# print(b)