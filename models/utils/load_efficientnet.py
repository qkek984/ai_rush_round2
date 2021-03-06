from models.efficientnet import EfficientNet
import torch.nn as nn

def EfficientNet_B2(pretrained=True, num_class= 5, advprop=False, onehot=1, onehot2=0):
    if pretrained:
        model = EfficientNet.from_pretrained('efficientnet-b2', num_classes=num_class, onehot=onehot, onehot2=onehot2)
        for name, param in model.named_parameters():
            if 'fc' not in name :# and 'blocks.24' not in name and 'blocks.25' not in name
                param.requires_grad = False
    else:
        model = EfficientNet.from_name('efficientnet-b2', onehot=onehot, onehot2=onehot2)

    model.name = "EfficientNet_B2"
    print("EfficientNet B2 Loaded!")

    return model

def EfficientNet_B5(pretrained=True, num_class= 5, advprop=False, onehot=1, onehot2=0):
    if pretrained:
        model = EfficientNet.from_pretrained('efficientnet-b5', num_classes=num_class, onehot=onehot, onehot2=onehot2)
        for name, param in model.named_parameters():
            if 'fc' not in name :# and 'blocks.24' not in name and 'blocks.25' not in name
                param.requires_grad = False
    else:
        model = EfficientNet.from_name('efficientnet-b5', onehot=onehot, onehot2=onehot2)

    model.name = "EfficientNet_B5"    
    print("EfficientNet B5 Loaded!")

    return model

def EfficientNet_B6(pretrained=True, num_class=5, advprop=False, onehot=1, onehot2=0):
    if pretrained:
        model = EfficientNet.from_pretrained('efficientnet-b6', num_classes=num_class, onehot=onehot, onehot2=onehot2)
        for name, param in model.named_parameters():
            if 'fc' not in name :# and 'blocks.24' not in name and 'blocks.25' not in name
                param.requires_grad = False
    else:
        model = EfficientNet.from_name('efficientnet-b6', onehot=onehot, onehot2=onehot2)
    
    model.name = "EfficientNet_B6"
    print("EfficientNet B6 Loaded!")

    return model

def EfficientNet_B8(pretrained=True, num_class=5, onehot=1, onehot2=0):
    if pretrained:
        model = EfficientNet.from_pretrained('efficientnet-b8', num_classes=num_class, onehot=onehot, onehot2=onehot2)
        for name, param in model.named_parameters():
            if 'fc' not in name:
                param.requires_grad = False
    else:
        model = EfficientNet.from_name('efficientnet-b8', onehot=onehot, onehot2=onehot2)
    model.name = "EfficientNet_B8"    
    print("EfficientNet B7 Loaded!")

    return model