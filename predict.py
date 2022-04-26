import torch 
import torch.nn as nn 
from torchvision import transforms

from network import VGG16 
from DiseaseData import Diseasedata

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

data_transforms = transforms.Compose([
  transforms.Resize((224,224)),
  transforms.ToTensor(),
  transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

root_path = 'Dataset'
test_data = Diseasedata(root_path, phase='val')

model = VGG16(num_classes=3)

model.load_state_dict(torch.load('Models/VGG16_custom.pth'))
model.to(device)
model.eval()

index = 132
image, label = test_data.__getitem__(index)

image = data_transforms(image)
image = image.unsqueeze(0).to(device)

outputs = model(image)
_, preds = torch.max(outputs, 1)

status = ['Early blight', 'Late blight', 'healthy']

print(preds.item())
print(label)
print('Predicted: ', status[preds.item()])
print('Correct label: ', status[label])