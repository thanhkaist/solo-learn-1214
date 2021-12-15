python3 ../../../main_pretrain.py \
    --dataset cifar100 \
    --backbone resnet18 \
    --data_dir ~/workspace/trung_database/datasets/ \
    --max_epochs 200 \
    --gpus 0 \
    --accelerator gpu \
    --precision 16 \
    --optimizer sgd \
    --lars \
    --grad_clip_lars \
    --eta_lars 0.02 \
    --exclude_bias_n_norm \
    --scheduler warmup_cosine \
    --lr 0.4 \
    --classifier_lr 0.1 \
    --weight_decay 1e-5 \
    --batch_size 256 \
    --num_workers 4 \
    --brightness 0.4 \
    --contrast 0.4 \
    --saturation 0.2 \
    --hue 0.1 \
    --gaussian_prob 0.0 0.0 \
    --solarization_prob 0.0 0.2 \
    --crop_size 32 \
    --num_crops_per_aug 1 1 \
    --name nnclr_res18 \
    --project CIFAR100-200ep \
    --entity kaistaim \
    --wandb \
    --save_checkpoint \
    --method nnclr \
    --temperature 0.2 \
    --proj_hidden_dim 2048 \
    --pred_hidden_dim 4096 \
    --proj_output_dim 256 \
    --queue_size 65536 \
    --knn_eval \
    --lam 0.1 \
    --tau_decor 0.1 \
    --our_loss False \