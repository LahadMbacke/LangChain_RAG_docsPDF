# LangChain_RAG_docsPDF
![Ask_Book_Questions_Workflow](https://github.com/user-attachments/assets/4063088d-396e-4491-b68c-a73c4c8c401d)
-https://bennycheung.github.io/ask-a-book-questions-with-langchain-openai

Projet utilisant LangChain pour poser des questions à partir de documents PDF en utilisant un système de récupération-augmented generation (RAG).

## Description

Ce projet utilise LangChain pour créer une interface de questions-réponses à partir de documents PDF. Le processus comprend l'extraction de texte des fichiers PDF, la création d'une base de connaissances et l'utilisation d'un modèle de langage pour répondre aux questions posées sur le contenu des PDF.

## Prérequis

- Python 3.x
- Compte OpenAI avec une clé API valide

## Installation

Clonez le dépôt et installez les dépendances :

```bash
cd LangChain_RAG_docsPDF
pip install -r requirements.txt
```

## Fonctionnalités
Extraction de texte à partir de fichiers PDF.
Création d'une base de connaissances à partir du texte extrait.
Utilisation d'un modèle de langage pour répondre aux questions.
Interface utilisateur Streamlit pour interagir avec le système.

## Utilisation
1- Lancez l'application Streamlit :
```bash
streamlit run main.py
 ```

2- Téléchargez un fichier PDF via l'interface utilisateur.
3- Posez des questions et recevez des réponses basées sur le contenu du PDF.

## Fonctionnement
Le texte est extrait des fichiers PDF et divisé en morceaux.
Les morceaux de texte sont transformés en embeddings à l'aide de OpenAIEmbeddings.
Un modèle de langage OpenAI génère des réponses aux questions posées par l'utilisateur.
L'interface Streamlit facilite l'interaction avec le système.




