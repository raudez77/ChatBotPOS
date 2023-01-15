import os 
import pathlib


ROOT = pathlib.Path(__file__).resolve().parent
TOKENIZER_DIR = os.path.join(ROOT, "Tokenizer")
EMBEDDINGS_DIR = os.path.join(ROOT,"Embeddings")
