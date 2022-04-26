import torch
import torch.nn as nn 
from torchvision import models
import torch.nn.functional as F 

class VGG16(nn.Module):
  def __init__(self, num_classes):
    super(VGG16, self).__init__()
    self.pretrained_model = models.vgg16(pretrained=True).requires_grad_(False)
    self.pretrained_model.classifier[6] = nn.Linear(4096, num_classes)
    self.pretrained_model.classifier.requires_grad = True

  def forward(self, x):
    x = self.pretrained_model(x)
    x = F.softmax(x, dim=1)
    return x

# net = VGG16(3)
# print(net)
# a = torch.rand(1,3,224,224)
# b = net(a)
# print(b)