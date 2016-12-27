# script to vectorize text and implement other transformation functions
from sklearn.feature_extraction.text import TfidfVectorizer


class Transformer:

    def __init__(self):
        self.vectorizer = TfidfVectorizer('english', min_df=3, analyzer='word')
        self.vector_features = []

    def vectorize_text(self, text):
        vectorized_text = self.vectorizer.fit_transform(text)
        self.vector_features = self.vectorizer.get_feature_names()
        return vectorized_text

    def get_features(self):
        return self.vector_features