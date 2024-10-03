# Role-play Engineering Strategies for Text-to-Audio Generation

## Description

Modern large language models (LLMs)’ role-play abilities via role prompting have proven to be capable of enhancing the performance of LLMs’ in complex humanlike interactions and behaviors across fields. Recently, text-to-audio (TTA) generation methods are able to construct intended audio through natural language de- scriptions. TTA models are mostly trained on audio datasets paired with manually or automatically generated plain descriptions. This study explores whether changing perspectives of descriptions would impact the performance of TTA models. Hereby, we introduce a zero-shot role-play prompting methodology to create prompts from the perspective of specific roles. This method is tested on Tango model. Both objective and subjective evaluation reveal that role prompting could significantly enhance the audio quality and text-audio alignment of recent TTA methods.

## Traning and Inference
### Prerequisites

This proposed method is tested on [Tango](https://github.com/declare-lab/tango), thus we follow the training and inference procedures provided by Tango.

Install `requirements.txt`.

```bash
git clone https://github.com/declare-lab/tango/
cd tango
pip install -r requirements.txt
```

You might also need to install `msclap==1.3.3` for computing text-audio alignment score in this experiment:

```bash
pip install msclap
```

### Datasets

Like Tango, we use the dataset AudioCaps[AudioCaps repository](https://github.com/cdjkim/audiocaps) for downloading the data.

### How to train?
We use the `accelerate` package from Hugging Face for multi-gpu training. Run `accelerate config` from terminal and set up your run configuration by the answering the questions asked.

You can now train **TANGO** on the AudioCaps dataset using:

```bash
accelerate launch train.py \
--text_encoder_name="google/flan-t5-large" \
--scheduler_name="stabilityai/stable-diffusion-2-1" \
--unet_model_config="configs/diffusion_model_config.json" \
--freeze_text_encoder --augment --snr_gamma 5 \
```

The argument `--augment` uses augmented data for training as reported in our paper. We recommend training for at-least 40 epochs, which is the default in `train.py`.

To start training from our released checkpoint use the `--hf_model` argument.

```bash
accelerate launch train.py \
--hf_model "declare-lab/tango" \
--unet_model_config="configs/diffusion_model_config.json" \
--freeze_text_encoder --augment --snr_gamma 5 \
```

Check `train.py` and `train.sh` for the full list of arguments and how to use them.

### How to make inferences?

### From your trained checkpoints

Checkpoints from training will be saved in the `saved/*/` directory.

To perform audio generation and objective evaluation in AudioCaps test set from your trained checkpoint:

```bash
CUDA_VISIBLE_DEVICES=0 python inference.py \
--original_args="saved/*/summary.jsonl" \
--model="saved/*/best/pytorch_model_2.bin" \
```

Check `inference.py` and `inference.sh` for the full list of arguments and how to use them.

### From released Tango checkpoints in Hugging Face Hub

To perform audio generation and objective evaluation in AudioCaps test set from Tango huggingface checkpoints:

```bash
python inference_hf.py --checkpoint="declare-lab/tango"
```

## Prompts generation

To generate paraphrased prompts, we provide code for implementing FLAN-T5-XL for prompts paraphasing, run Prompt_generate_Flan_T5_XL.ipynb.

## Prompts evaluation

To evaluate the paraphrased prompts, run Prompts_evaluation.ipynb.


