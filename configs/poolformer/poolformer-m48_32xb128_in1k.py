_base_ = [
    '../_base_/models/poolformer/poolformer_m48.py',
    '../_base_/datasets/imagenet_bs128_poolformer_medium_224.py',
    '../_base_/schedules/imagenet_bs1024_adamw_swin.py',
    '../_base_/default_runtime.py',
]

# schedule settings
optim_wrapper = dict(
    optimizer=dict(lr=4e-3),
    clip_grad=dict(max_norm=5.0),
)
