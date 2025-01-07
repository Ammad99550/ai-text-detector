from transformers import pipeline

class TextDetectionModel:
    def __init__(self, model_name='roberta-base-openai-detector'):
        """
        Initializes the model using a pre-trained Hugging Face transformer model.
        You can replace 'roberta-base-openai-detector' with any other model suitable for content detection.
        """
        self.model = pipeline('text-classification', model=model_name)

    def detect(self, text):
        """
        Detects whether the given text is AI-generated.
        
        :param text: Input text to analyze
        :return: Result of the model's prediction (e.g., 'AI-generated' or 'Human-generated')
        """
        result = self.model(text)
        # Assuming the model returns a label such as "AI-generated" or "Human-generated"
        label = result[0]['label']
        return label
