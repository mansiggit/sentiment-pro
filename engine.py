from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        # This model is a beast—it handles 20+ languages including Hindi, French, Spanish
        model_path = "tabularisai/multilingual-sentiment-analysis"
        self.analyzer = pipeline("sentiment-analysis", model=model_path)

    def analyze(self, text):
        if not text or str(text).strip() == "":
            return None

        result = self.analyzer(text)[0]
        # This model returns labels like 'very negative', 'neutral', etc.
        return {
            "sentiment": result['label'].title(),
            "confidence": f"{round(result['score'] * 100, 2)}%"
        }