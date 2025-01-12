python3 ../../../main_pretrain.py \
    --dataset stl10 \
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
    --scheduler warmup_cosine \
    --lr 0.6 \
    --min_lr 0.0006 \
    --warmup_start_lr 0.0 \
    --warmup_epochs 11 \
    --classifier_lr 0.1 \
    --weight_decay 1e-6 \
    --batch_size 256 \
    --num_workers 4 \
    --brightness 0.8 \
    --contrast 0.8 \
    --saturation 0.8 \
    --hue 0.2 \
    --gaussian_prob 0.0 0.0 \
    --crop_size 96 \
    --num_crops_per_aug 1 1 \
    --name deepclusterv2_res18 \
    --project STL10-200ep \
    --entity kaistaim \
    --wandb \
    --save_checkpoint \
    --method deepclusterv2 \
    --proj_hidden_dim 2048 \
    --proj_output_dim 128 \
    --num_prototypes 3000 3000 3000 \
    --knn_eval \
    --lam 0.1 \
    --tau_decor 0.1 \
    --our_loss False \
