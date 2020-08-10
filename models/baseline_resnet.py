import torch
import torch.nn.functional as F
import torchvision.models as models

class Resnet50_FC2(torch.nn.Module):
    def __init__(self, n_class=5, pretrained=True, use_fc_=True, name="ResNext"):
        super(Resnet50_FC2, self).__init__()
        self.name = name
        #self.basemodel = models.resnet50(pretrained=pretrained)
        self.basemodel = models.resnext101_32x8d(pretrained=pretrained, progress=True)
        self.linear1 = torch.nn.Linear(1000 , 512)
        self.linear2 = torch.nn.Linear(512, n_class)

        self.use_fc_ = use_fc_

    def forward(self, x, onehot=None):
        x = self.basemodel(x)
        if self.use_fc_:
            x = F.relu(self.linear1(x))
            out = F.softmax(self.linear2(x), dim=-1)
            pred = torch.argmax(out, dim=-1)

            return out, pred
        else:
            batch_size = x.shape[0]
            return x.reshape(batch_size,-1), None