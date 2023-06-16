import torch
import time

def time_synchronized():
    torch.cuda.synchronize() if torch.cuda.is_available() else None
    return time.time()