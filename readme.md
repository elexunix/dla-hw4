# Well, simply run `train.py` for training, and `test.py` for test

The complete report may be found in the `report` folder. Hope you will enjoy

The generated audios are there as well (couldn't be reliably embedded into the pdf)

The logs of the training can be found in this root folder (file `logs`)

The wandb charts etc of the main run is here: https://wandb.ai/elexunix/nv_project/runs/lq4mkm62?workspace=user-elexunix
others are here: https://wandb.ai/elexunix/nv_project

Finally, the checkpoint is accessible via elexunix.com/shared/dla-hw4/model-best.pth and is expected to be with that name (model-best.pth) inside default-test-folder. Also, the test dataset is also located inside default-test-folder
For you to ensure that checkpoint is available at the time of committing this, here is its sha512:
`$ sha512sum default-test-folder/model-best.pth `
`824dd56dc18696503fc0b88dbf290bb92196cbe601ccafbb6494c51fa4b31d89a81078e8e38535a355a41f60c0b5045f56706721043cffc2ee4dacc274c7dcbc  default-test-folder/model-best.pth`
