import os
from transformers import pipeline


class SentimentAnalyzer:
    def __init__(self):
        # Model name is env-driven so it can be swapped without code changes
        # and so any future gated/private model follows the same pattern.
        model_path = os.environ.get(
            "SENTIMENT_MODEL_PATH",
            "tabularisai/multilingual-sentiment-analysis",
        )

        # Optional HF token for private/gated models or higher rate limits.
        hf_token = os.environ.get("HUGGINGFACE_HUB_TOKEN") or None

        self.analyzer = pipeline(
            "sentiment-analysis",
            model=model_path,
            token=hf_token,
        )

    def analyze(self, text):
        if not text or str(text).strip() == "":
            return None

        result = self.analyzer(text)[0]
        return {
            "sentiment": result["label"].title(),
            "confidence": f"{round(result['score'] * 100, 2)}%",
        }
