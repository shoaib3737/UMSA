# Urdu Multi-Modal Sentiment Analysis (UMSA)

[![IEEE Publication](https://img.shields.io/badge/Published%20in-IEEE%20Access-blue)](https://doi.org/10.1109/ACCESS.2025.3552475)

**UMSA** is a robust and extensible framework for **multi-modal sentiment analysis and emotion detection**, focused specifically on **Urdu-language product review videos**. It combines **textual, audio, and visual modalities** using a fusion-based approach and ensemble modeling. This repository contains the implementation code, dataset details, model weights, and evaluation results described in our thesis and journal publication.

---

## 📄 Journal Publication

> **S. S. Malik et al.**, *"Multi-Modal Emotion Detection and Sentiment Analysis,"* in IEEE Access, vol. 13, pp. 59790-59810, 2025.  
> [📖 Read Full Paper](https://doi.org/10.1109/ACCESS.2025.3552475)

---

## 📊 Overview

In the digital era, online review videos play a vital role in shaping public opinion and consumer decisions. **UMSA** addresses the challenge of extracting sentiment from such content, especially for low-resource languages like Urdu.

UMSA offers:
- A multi-modal Urdu dataset (USD)
- End-to-end extraction and annotation of text, audio, and visual modalities
- Early fusion and late ensembling techniques
- Support for transfer learning
- Benchmarking on text-only and multi-modal datasets

---

## 🧠 Key Features

- **Dataset (USD):**  
  Urdu Sentiment Dataset consisting of annotated videos with synchronized modalities

- **Multi-Modality Handling:**  
  - `Text` extracted from transcribed speech  
  - `Audio` preprocessed for emotional signals  
  - `Visual Frames` captured and annotated from videos

- **Model Fusion + Ensembling:**  
  Each modality is modeled individually and then combined via ensemble strategies for final prediction.

- **Use Case Evaluation:**  
  Real-world product reviews evaluated to test generalization.

---

## 🧪 Performance Summary

UMSA achieves **>80% classification accuracy** on the USD dataset using multi-modal integration. Validation on external datasets (`USCv1`, `UrduTweets`) showed expected drop in performance due to modality mismatch.

## Dataset , Models and Code

The detail of Datasets, Models and Code is available on :
https://www.kaggle.com/datasets/shoaib837/urdu-sentiments-dataset-usd

---

## 📁 Repository Structure

