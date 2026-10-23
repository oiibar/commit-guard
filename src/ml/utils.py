import os, random, numpy as np, torch

def set_seed(seed: int):
 random.seed(seed); np.random.seed(seed); torch.manual_seed(seed)
 torch.cuda.manual_seed_all(seed)
 os.environ["PYTHONHASHSEED"] = str(seed)
 torch.backends.cudnn.deterministic = True
 torch.backends.cudnn.benchmark = False

# Some GPU ops stay slightly non-deterministic; that is why you run several seeds anyway.
# seeds: [54, 67, 20, 89, 44]
# semgrep: {version: "x.y.z", rules_commit: "<git sha>", timeout_s: 30}
# data: {cvefixes: "v1.0.8", dataset_version: "v1"}
# split: {type: "project", ratios: [0.70, 0.15, 0.15], seed: 20}
# model: {name: "microsoft/codebert-base", max_len: 512, lr: 2.0e-5, epochs: 4, batch_size: 16} 