from core.training import train_convnext

"""
Explanation of the config:
    - finetune.use_fraction: How much of the dataset to use for finetuning
        (applied before splitting into train, val, test)
    - finetune.epochs: Number of epochs to train for during finetuning
    - finetune.lr: Learning rate for finetuning
    - finetune.train_size: Fraction of the finetune dataset to use for training.
        The rest is split equally into a validation and test set.
    - finetune.batch_size: Batch size for finetuning.

    - pretrain.use_fraction: How much of the dataset to use for pretraining
    - pretrain.task: Which task to use for pretraining. Can be one of:
        - "rotated": Use the rotated images for pretraining
        - "grayscale": Use the grayscale images for pretraining
        - "rotated_grayscale": Use the rotated grayscale images for pretraining
        - None: Don't pretrain, just finetune
    - pretrain.epochs: Number of epochs to train for during pretraining
    - pretrain.lr: Learning rate for pretraining
    - pretrain.batch_size: Batch size for pretraining
"""
train_config = {
    "run_label": "MyExperimentName",
    "finetune": {
        "use_fraction": 1,
        "epochs": 15,
        "lr": 0.0001,
        "train_size": 1 / 3,
        "batch_size": 16,
    },
    "pretrain": {
        # Note from Marcel: An epoch on the full dataset takes roughly 1h on my RTX 2070s
        # and a batchsize of 16 takes up 7GB of memory on my GPU (every additional sample adds ~200MB of memory usage)
        # In general, the pretraining is much more demanding than the finetuning (due to the larger dataset size)
        "use_fraction": 1,
        "task": "rotated",
        "epochs": 5,
        "lr": 0.0001,
        "batch_size": 16,
    },
}

model = train_convnext(train_config=train_config)