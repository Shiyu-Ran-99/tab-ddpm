from scripts.resample_privacy import privacy_metrics
from collections import defaultdict
import json
import numpy as np
from tqdm import tqdm
import argparse
import toml

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, help='choose the dataset')
args = parser.parse_args()

# datasets = ['abalone','adult','buddy','california','cardio','churn2','diabetes','fb-comments','gesture','higgs-small','house','insurance','king','miniboone','wilt']
# datasets = ['abalone','diabetes']
# models = ['ddpm_cb_best','ctabgan-plus','tvae','smote']
models = ['ddpm_cb_best']
# pbar = tqdm(datasets)
mbar = tqdm(models)
f = toml.load('exp/churn2/ddpm_cb_best/config.toml', _dict=dict)

res = {}
for model in mbar:
    real_path = 'data/'+args.dataset
    fake_path = 'exp/'+args.dataset+'/'+model
    dists = privacy_metrics(real_path=real_path,fake_path=fake_path, data_percent=15)
    privacy_val = np.median(dists)
    res['dataset'] = args.dataset
    res['model'] = model
    res['embedding_type'] = f['model_params']['embedding_type']
    res['dcr_value'] = privacy_val
    mbar.set_description(f"{model} is completed")

# with open(f"dcr_dp/{args.dataset}_dcr.json","w") as f:
#     json.dump(res,f)
#     print("Computing DCR values are done.")
file = open("dcr_dp_embed.txt", "a")
file.write(f"{res}")
file.write("\n")
file.close()