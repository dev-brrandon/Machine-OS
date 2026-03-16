#!/usr/bin/env python3
"""
Machine Researcher - Code Intelligence Agent v0.1

Mission: Baue eine Code-Wissensdatenbank für die Coder
- Sammelt Code-Beispiele von GitHub, Stack Overflow, Docs
- Speichert lauffähige Python-Implementierungen
- Strukturiert nach: Algorithmus, Komplexität, Performance
"""

import os
import sys
import json
import hashlib
from datetime import datetime
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

# Konfiguration
GEMINI_API_KEY = "AIzaSyDlaPdE0zErxeu4MZW_nrpq73C46Jkumko"
QDRANT_HOST = "187.77.67.80"
QDRANT_PORT = 32773
QDRANT_API_KEY = "qJ4icfeaDcrK7p4sX91sIb4gh7H61GFU"

class CodeResearcher:
    def __init__(self):
        self.qdrant = QdrantClient(
            host=QDRANT_HOST,
            port=QDRANT_PORT,
            api_key=QDRANT_API_KEY,
            https=False
        )
        self.collection = "code_examples"
        
    def generate_embedding(self, code: str) -> list:
        """Generiere einfaches Embedding für Code (für Qdrant)"""
        # Einfacher Ansatz: Code-Features als Vektor
        # In Produktion: Richtiges Code-Embedding (CodeBERT, etc.)
        features = [
            len(code),  # Länge
            code.count('def '),  # Anzahl Funktionen
            code.count('for '),   # Anzahl Schleifen
            code.count('if '),    # Anzahl Bedingungen
            code.count('import'), # Anzahl Imports
            hash(code) % 100 / 100,  # Hash als Feature
        ]
        # Auf 384 Dimensionen erweitern (für Qdrant)
        vector = features + [0.0] * (384 - len(features))
        return vector
    
    def save_code_example(self, title: str, code: str, description: str, 
                         topic: str, complexity: str, source: str):
        """Speichere Code-Beispiel in Qdrant"""
        
        payload = {
            "title": title,
            "code": code,
            "description": description,
            "topic": topic,
            "complexity": complexity,
            "source": source,
            "language": "python",
            "created_at": datetime.now().isoformat(),
            "version": "v0.1"
        }
        
        # Generiere Embedding aus dem Code
        vector = self.generate_embedding(code)
        
        # Eindeutige ID aus dem Code-Hash
        code_id = abs(hash(code)) % (10 ** 10)
        
        point = PointStruct(
            id=code_id,
            vector=vector,
            payload=payload
        )
        
        self.qdrant.upsert(
            collection_name=self.collection,
            points=[point]
        )
        
        print(f"✅ Gespeichert: {title} ({complexity})")
        return code_id
    
    def research_knn_implementations(self):
        """Sammelt verschiedene k-NN Implementierungen"""
        print("🔍 Sammle k-NN Implementierungen...")
        
        # Beispiel 1: Einfacher k-NN
        code_simple = '''
def knn_simple(X_train, y_train, x_test, k=3):
    """
    Einfacher k-NN Algorithmus
    X_train: Liste von Trainingsvektoren
    y_train: Liste von Labels
    x_test: Zu klassifizierender Vektor
    k: Anzahl der Nachbarn
    """
    import math
    
    # Berechne Distanzen zu allen Trainingspunkten
    distances = []
    for i, x in enumerate(X_train):
        # Euklidische Distanz
        dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(x, x_test)))
        distances.append((dist, y_train[i]))
    
    # Sortiere nach Distanz
    distances.sort(key=lambda x: x[0])
    
    # Wähle k nächste Nachbarn
    neighbors = distances[:k]
    
    # Mehrheitsentscheid
    from collections import Counter
    votes = [label for _, label in neighbors]
    return Counter(votes).most_common(1)[0][0]
'''
        
        self.save_code_example(
            title="k-NN Einfach (Euklidisch)",
            code=code_simple,
            description="Grundlegende k-NN Implementierung mit euklidischer Distanz. Gut für den Einstieg.",
            topic="k-NN Algorithmus",
            complexity="einfach",
            source="Machine Researcher v0.1"
        )
        
        # Beispiel 2: k-NN mit Cosine Similarity
        code_cosine = '''
def cosine_similarity(v1, v2):
    """Cosine Similarity zwischen zwei Vektoren"""
    import math
    dot_product = sum(a * b for a, b in zip(v1, v2))
    magnitude1 = math.sqrt(sum(x * x for x in v1))
    magnitude2 = math.sqrt(sum(x * x for x in v2))
    return dot_product / (magnitude1 * magnitude2)

def knn_cosine(X_train, y_train, x_test, k=3):
    """k-NN mit Cosine Similarity (besser für hohe Dimensionen)"""
    similarities = []
    for i, x in enumerate(X_train):
        sim = cosine_similarity(x, x_test)
        similarities.append((sim, y_train[i]))
    
    # Sortiere nach Similarity (absteigend)
    similarities.sort(key=lambda x: x[0], reverse=True)
    
    # Wähle k ähnlichste
    neighbors = similarities[:k]
    
    from collections import Counter
    votes = [label for _, label in neighbors]
    return Counter(votes).most_common(1)[0][0]
'''
        
        self.save_code_example(
            title="k-NN mit Cosine Similarity",
            code=code_cosine,
            description="k-NN mit Cosine Similarity statt Euklidischer Distanz. Besser für Text- und Bild-Embeddings.",
            topic="k-NN Algorithmus",
            complexity="mittel",
            source="Machine Researcher v0.1"
        )
    
    def research_vector_operations(self):
        """Sammelt Matrix- und Vektor-Operationen"""
        print("🔍 Sammle Vektor-Operationen...")
        
        code_matrix = '''
class SimpleMatrix:
    """Einfache Matrix-Operationen ohne NumPy"""
    
    @staticmethod
    def multiply(A, B):
        """Matrix-Multiplikation A × B"""
        rows_A = len(A)
        cols_A = len(A[0])
        cols_B = len(B[0])
        
        result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
        
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += A[i][k] * B[k][j]
        return result
    
    @staticmethod
    def transpose(matrix):
        """Transponiere Matrix"""
        return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    
    @staticmethod
    def dot_product(v1, v2):
        """Skalarprodukt zweier Vektoren"""
        return sum(a * b for a, b in zip(v1, v2))
    
    @staticmethod
    def euclidean_distance(v1, v2):
        """Euklidische Distanz"""
        import math
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))
'''
        
        self.save_code_example(
            title="Matrix-Operationen (Pure Python)",
            code=code_matrix,
            description="Grundlegende Matrix-Operationen ohne externe Bibliotheken. Für das Verständnis der Mathematik hinter ML.",
            topic="Mathematische Operationen",
            complexity="mittel",
            source="Machine Researcher v0.1"
        )
    
    def research_image_to_vector(self):
        """Sammelt Bild-zu-Vektor Konvertierungen"""
        print("🔍 Sammle Bild-zu-Vektor Methoden...")
        
        code_flatten = '''
def image_to_vector_flatten(image_path):
    """
    Konvertiere Bild zu Vektor durch Flattening
    Einfachster Ansatz: Pixel als 1D-Array
    """
    from PIL import Image
    
    # Lade Bild
    img = Image.open(image_path)
    
    # Konvertiere zu RGB
    img = img.convert('RGB')
    
    # Resize für Konsistenz (z.B. 64x64)
    img = img.resize((64, 64))
    
    # Flatten zu 1D-Array
    pixels = list(img.getdata())
    
    # Normalisiere (0-255 → 0-1)
    vector = [p / 255.0 for pixel in pixels for p in pixel]
    
    return vector

def image_to_vector_histogram(image_path):
    """
    Konvertiere Bild zu Vektor durch Farb-Histogramm
    Kompakter als Flattening
    """
    from PIL import Image
    
    img = Image.open(image_path).convert('RGB')
    
    # Erstelle Histogramm für jede Farbe (R, G, B)
    histogram = img.histogram()  # 768 Werte (256 * 3)
    
    # Normalisiere
    total_pixels = img.size[0] * img.size[1]
    vector = [h / total_pixels for h in histogram]
    
    return vector
'''
        
        self.save_code_example(
            title="Bild-zu-Vektor Konvertierung",
            code=code_flatten,
            description="Zwei Methoden: Flattening (einfach) und Histogram (kompakt). Kein Deep Learning nötig.",
            topic="Bildverarbeitung",
            complexity="einfach",
            source="Machine Researcher v0.1"
        )
    
    def research_audio_to_vector(self):
        """Sammelt Audio-zu-Vektor Methoden"""
        print("🔍 Sammle Audio-zu-Vektor Methoden...")
        
        code_audio = '''
import wave
import struct
import math

def audio_to_vector_raw(audio_path, sample_rate=16000):
    """
    Extrahiere Roh-Audio-Wellenform als Vektor
    Einfachster Ansatz
    """
    with wave.open(audio_path, 'rb') as wav:
        # Lese alle Frames
        n_frames = wav.getnframes()
        audio_data = wav.readframes(n_frames)
        
        # Konvertiere zu Float-Array
        fmt = f"{n_frames}h"  # 16-bit signed
        samples = struct.unpack(fmt, audio_data)
        
        # Normalisiere (-1 bis 1)
        vector = [s / 32768.0 for s in samples]
        
        # Downsampling für Konsistenz (z.B. auf 1000 Samples)
        if len(vector) > 1000:
            step = len(vector) // 1000
            vector = vector[::step][:1000]
        
        return vector

def audio_to_vector_fft(audio_path):
    """
    Extrahiere Frequenz-Spektrum durch FFT
    Besser für Audio-Erkennung
    """
    import numpy as np
    
    with wave.open(audio_path, 'rb') as wav:
        n_frames = wav.getnframes()
        audio_data = wav.readframes(n_frames)
        samples = struct.unpack(f"{n_frames}h", audio_data)
    
    # FFT (Fourier Transform)
    fft_result = np.fft.fft(samples)
    
    # Amplitude-Spektrum (nur erste Hälfte)
    amplitudes = np.abs(fft_result[:len(fft_result)//2])
    
    # Logarithmische Skalierung für bessere Features
    log_amplitudes = np.log(amplitudes + 1)
    
    return log_amplitudes.tolist()
'''
        
        self.save_code_example(
            title="Audio-zu-Vektor Konvertierung",
            code=code_audio,
            description="Roh-Wellenform und FFT-basierte Features. Für Sprach- und Audio-Erkennung.",
            topic="Audioverarbeitung",
            complexity="mittel",
            source="Machine Researcher v0.1"
        )
    
    def run(self):
        """Führe alle Recherchen durch"""
        print("🚀 Machine Researcher - Code Intelligence v0.1")
        print("=" * 60)
        print("Baue Code-Wissensdatenbank für Coder...")
        print()
        
        # Alle Recherchen durchführen
        self.research_knn_implementations()
        self.research_vector_operations()
        self.research_image_to_vector()
        self.research_audio_to_vector()
        
        print()
        print("=" * 60)
        print("🎉 Code-Wissensdatenbank fertig!")
        print()
        print("Gesammelt:")
        print("  - k-NN Implementierungen (einfach + cosine)")
        print("  - Matrix-Operationen (pure Python)")
        print("  - Bild-zu-Vektor Methoden")
        print("  - Audio-zu-Vektor Methoden")
        print()
        print("Alle Code-Beispiele in Qdrant:")
        print(f"  Host: {QDRANT_HOST}:{QDRANT_PORT}")
        print(f"  Collection: {self.collection}")
        print()
        print("Coder können jetzt darauf zugreifen und lernen!")

if __name__ == "__main__":
    researcher = CodeResearcher()
    researcher.run()
