from summarizer import TransformerSummarizer

def log(text: str, header: str):
    print("\n")
    print(header)
    print(text)

def gpt2_summarize(body: str) -> str:
    compression_ratio = len(body)/66
    GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2")
    full = ''.join(GPT2_model(body,max_length=compression_ratio))
    return full

