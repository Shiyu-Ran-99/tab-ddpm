#! /bin/bash
#ddpm_cb_best
python scripts/pipeline.py --config exp/abalone/ddpm_cb_best/config.toml --train --sample --eval
python scripts/pipeline.py --config exp/buddy/ddpm_cb_best/config.toml --train --sample --eval
python scripts/pipeline.py --config exp/california/ddpm_cb_best/config.toml --train --sample --eval
python scripts/pipeline.py --config exp/diabetes/ddpm_cb_best/config.toml --train --sample --eval
python scripts/pipeline.py --config exp/insurance/ddpm_cb_best/config.toml --train --sample --eval
python scripts/pipeline.py --config exp/wilt/ddpm_cb_best/config.toml --train --sample --eval

python cal_metrics.py --dataset abalone --model ddpm_cb_best
python cal_metrics.py --dataset buddy --model ddpm_cb_best
python cal_metrics.py --dataset california --model ddpm_cb_best
python cal_metrics.py --dataset diabetes --model ddpm_cb_best
python cal_metrics.py --dataset insurance --model ddpm_cb_best
python cal_metrics.py --dataset wilt --model ddpm_cb_best