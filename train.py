import argparse

import torch
import torch.nn as nn 
from torch.utils.data import DataLoader
from torchvision import transforms

from DiseaseData import Diseasedata
from network import VGG16
import time
import math 

def args_input():
  parser = argparse.ArgumentParser(description='Set up parameters')
  parser.add_argument('--batch_size', type=int, nargs='?', default=64 ,help='batch size')
  parser.add_argument('--num_epochs', type=int, nargs='?', default=100, help='number of epochs')
  parser.add_argument('--from_scratch', type=bool, nargs='?', default=True, help='Train from scratch ?')
  return parser

def lambda_epoch(epoch):
  parser = args_input().parser_args()
  max_epoch = parser.num_epochs
  return math.pow(1-epoch/max_epoch, 0.9)

def train_model(model, dataloader, criterion, scheduler, optimizer, num_epochs):
  device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
  print('Device: ', device)

  model.to(device)
  
  num_train_imgs = len(dataloader['train'].dataset)
  num_val_imgs = len(dataloader['val'].dataset)
  batch_size = dataloader['train'].batch_size

  print('Num train imgs: ', num_train_imgs)
  print('Num val imgs: ', num_val_imgs)

  iteration = 1
  best_acc = 0

  for epoch in range(num_epochs):
    t_epoch_start = time.time()
    t_iter_start = time.time()
    epoch_train_loss = 0.0
    epoch_val_loss = 0.0

    print('Epoch {} / {}'.format(epoch+1, num_epochs))
    for phase in ['train', 'val']:
      if phase == 'train':
        model.train()
        optimizer.zero_grad()
        print('Train Phase...')
      else:
        model.eval()
        print('Val Phase...')

      running_correct = 0

      count = 0
      for images, labels in dataloader[phase]:
        if images.size()[0] == 1:
          print('Image size [0] = 1 !!!')
          continue

        images = images.to(device)
        labels = labels.to(device)

        if phase=='train' and count == 0:
          optimizer.step()
          optimizer.zero_grad()

        with torch.set_grad_enabled(phase == 'train'):
          outputs = model(images)
          _, preds = torch.max(outputs, 1)

          loss = criterion(outputs, labels)

          if phase == 'train':
            loss.backward()

            if (iteration % 10 == 0):
              t_iter_end = time.time()
              duration = t_iter_end - t_iter_start
              # print('Iteration {} || Loss: {:.6f}  || 10iter: {:.6f} sec'.format(iteration, loss.item()/batch_size, duration))

              t_iter_start = time.time()

            epoch_train_loss += loss.item()
            iteration += 1

          else:
            epoch_val_loss += loss.item()

        running_correct += torch.sum(preds == labels.data)

      if phase == 'train':
        scheduler.step()
      
      epoch_acc = running_correct.double() / len(dataloader[phase].dataset)
      print('{} acc = {}'.format(phase, epoch_acc))

      if phase == 'val' and epoch_acc > best_acc:
        best_acc = epoch_acc
        torch.save(model.state_dict(), 'Models/VGG16_custom.pth')
        print('Saved model')

    t_epoch_end = time.time()
    duration = t_epoch_end - t_epoch_start
    print('Epoch {} || Epoch_train_loss: {:.6f} || Epoch_val_loss: {:.6f}'.format(epoch+1, epoch_train_loss/num_train_imgs, epoch_val_loss/num_val_imgs))        
    print('Duration {:.6f} sec'.format(duration))
    t_epoch_start = time.time()

if __name__ == '__main__':
  parser = args_input().parser_args()

  root_path = 'Dataset'
  data_transforms = {
    'train': transforms.Compose([
      transforms.Resize((224,224)),
      transforms.ToTensor(),
      transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
      transforms.Resize((224,224)),
      transforms.ToTensor(), 
      transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
  }
  train_dataset = Diseasedata(root_path, transforms=data_transforms, phase='train')
  val_dataset = Diseasedata(root_path, transforms=data_transforms, phase='val')

  model = VGG16(num_classes=3)

  if not parser.from_scratch:
    model.load_state_dict(torch.load('Models/VGG16_custom.pth'))

  criterion = nn.CrossEntropyLoss()

  optimizer = torch.optim.Adam(model.parameters(), lr=0.001, weight_decay=0.00001)

  scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda=lambda_epoch, last_epoch=-1)

  batch_size = parser.batch_size

  train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
  val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

  dataloader = {
    'train': train_loader,
    'val': val_loader
  }

  num_epochs = parser.num_epochs
  train_model(model, dataloader, criterion, scheduler, optimizer, num_epochs=num_epochs)