# optimizer
optim_wrapper = dict(
    optimizer=dict(
        type='SGD', lr=0.8, momentum=0.9, weight_decay=0.0001, nesterov=True))

# learning policy
param_scheduler = [
    # warm up learning rate scheduler
    dict(
        type='LinearLR',
        start_factor=0.25,
        by_epoch=True,
        begin=0,
        # about 2500 iterations for ImageNet-1k
        end=5,
        # update by iter
        convert_to_iter_based=True),
    # main learning rate scheduler
    dict(
        type='CosineAnnealingLR',
        T_max=95,
        by_epoch=True,
        begin=5,
        end=100,
    )
]

# train, val, test setting
train_cfg = dict(by_epoch=True, max_epochs=100)
val_cfg = dict(interval=1)  # validate every epoch
test_cfg = dict()
