#!/usr/bin/env python3
"""
Machine Researcher - Deep Search Mode
Sammelt umfassend Code-Beispiele für alle Versionen bis 19:30
"""

import os
import sys
import json
import hashlib
import time
from datetime import datetime
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

# Konfiguration
QDRANT_HOST = "187.77.67.80"
QDRANT_PORT = 32773
QDRANT_API_KEY = "qJ4icfeaDcrK7p4sX91sIb4gh7H61GFU"

class DeepResearcher:
    def __init__(self):
        self.qdrant = QdrantClient(
            host=QDRANT_HOST,
            port=QDRANT_PORT,
            api_key=QDRANT_API_KEY,
            https=False
        )
        self.collection = "code_examples"
        self.start_time = time.time()
        self.end_time = self.start_time + (28 * 60)  # 28 Minuten bis 19:30
        self.count = 0
        
    def should_continue(self):
        return time.time() < self.end_time
        
    def time_remaining(self):
        return int(self.end_time - time.time())
        
    def generate_embedding(self, code: str) -> list:
        features = [
            len(code),
            code.count('def '),
            code.count('for '),
            code.count('if '),
            code.count('import'),
            code.count('class '),
            hash(code) % 100 / 100,
        ]
        vector = features + [0.0] * (384 - len(features))
        return vector
    
    def save_code(self, title, code, description, topic, complexity, version):
        if not self.should_continue():
            return False
            
        payload = {
            "title": title,
            "code": code,
            "description": description,
            "topic": topic,
            "complexity": complexity,
            "source": "Deep Research",
            "language": "python",
            "version_target": version,
            "created_at": datetime.now().isoformat(),
        }
        
        vector = self.generate_embedding(code)
        code_id = abs(hash(code + title + str(time.time()))) % (10 ** 10)
        
        point = PointStruct(id=code_id, vector=vector, payload=payload)
        
        try:
            self.qdrant.upsert(collection_name=self.collection, points=[point])
            self.count += 1
            print(f"[{self.time_remaining()}s] ✅ {title} ({version})")
            return True
        except Exception as e:
            print(f"❌ Fehler: {e}")
            return False
    
    def research_all(self):
        print("🔬 Deep Research Mode")
        print("=" * 60)
        print(f"Start: {datetime.now().strftime('%H:%M:%S')}")
        print(f"Ende: 19:30:00 (28 Minuten)")
        print("Sammle umfassend Code für alle Versionen...")
        print()
        
        # V0.1: Grundlagen (mehr Beispiele)
        self.research_v01_extended()
        
        # V0.2-V0.5: Lernalgorithmen
        self.research_learning_algorithms()
        
        # V0.6-V0.8: Fortgeschrittene Themen
        self.research_advanced()
        
        # V0.9-V1.0: System & Integration
        self.research_system_integration()
        
        # Utilities & Tools
        self.research_utilities()
        
        print()
        print("=" * 60)
        print(f"🎉 Deep Research abgeschlossen!")
        print(f"Gesammelt: {self.count} Code-Beispiele")
        print(f"Endzeit: {datetime.now().strftime('%H:%M:%S')}")
    
    def research_v01_extended(self):
        """Erweiterte Grundlagen für v0.1"""
        print("\n📦 v0.1: Erweiterte Grundlagen")
        
        examples = [
            ("Euklidische Distanz", '''
def euclidean_distance(v1, v2):
    """Berechnet euklidische Distanz zwischen zwei Vektoren"""
    import math
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))

def manhattan_distance(v1, v2):
    """Manhattan-Distanz (L1-Norm)"""
    return sum(abs(a - b) for a, b in zip(v1, v2))

def cosine_similarity(v1, v2):
    """Cosine Similarity für Vektoren"""
    import math
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(x * x for x in v1))
    norm2 = math.sqrt(sum(x * x for x in v2))
    return dot / (norm1 * norm2) if norm1 and norm2 else 0.0
''', "Distanz-Metriken für k-NN und Clustering", "Mathematik", "einfach", "v0.1"),
            
            ("Bild-Preprocessing", '''
from PIL import Image
import numpy as np

def resize_image(image_path, size=(64, 64)):
    """Bild auf einheitliche Größe bringen"""
    img = Image.open(image_path)
    img = img.convert('RGB')
    img = img.resize(size)
    return img

def normalize_pixels(image_array):
    """Pixel-Werte normalisieren (0-255 -> 0-1)"""
    return image_array / 255.0

def grayscale(image_path):
    """Bild in Graustufen umwandeln"""
    img = Image.open(image_path).convert('L')
    return np.array(img)
''', "Bildvorverarbeitung für Machine Vision", "Bildverarbeitung", "einfach", "v0.1"),
            
            ("Audio-Preprocessing", '''
import wave
import struct
import numpy as np

def load_audio(filepath, sample_rate=16000):
    """Lädt Audio-Datei und gibt Samples zurück"""
    with wave.open(filepath, 'rb') as wav:
        n_channels = wav.getnchannels()
        n_samples = wav.getnframes()
        audio_data = wav.readframes(n_samples)
        
        # Konvertiere zu numpy array
        fmt = f"{n_samples * n_channels}h"
        samples = struct.unpack(fmt, audio_data)
        
        # Stereo zu Mono konvertieren falls nötig
        if n_channels == 2:
            samples = [(samples[i] + samples[i+1]) / 2 
                      for i in range(0, len(samples), 2)]
        
        return np.array(samples)

def normalize_audio(samples):
    """Normalisiert Audio auf -1 bis 1"""
    return samples / np.max(np.abs(samples))
''', "Audiovorverarbeitung für Machine Hearing", "Audioverarbeitung", "mittel", "v0.1"),
        ]
        
        for title, code, desc, topic, complexity, version in examples:
            if not self.should_continue():
                return
            self.save_code(title, code, desc, topic, complexity, version)
    
    def research_learning_algorithms(self):
        """Lernalgorithmen für v0.2-v0.5"""
        print("\n📦 v0.2-v0.5: Lernalgorithmen")
        
        examples = [
            ("DBSCAN Clustering", '''
import math
from collections import deque

class DBSCAN:
    """DBSCAN Clustering Algorithmus"""
    
    def __init__(self, eps=0.5, min_points=5):
        self.eps = eps
        self.min_points = min_points
        self.labels = None
    
    def fit(self, data):
        n = len(data)
        self.labels = [-1] * n  # -1 = noise
        cluster_id = 0
        
        for i in range(n):
            if self.labels[i] != -1:
                continue
            
            neighbors = self._get_neighbors(data, i)
            
            if len(neighbors) < self.min_points:
                self.labels[i] = -1  # Noise
            else:
                self._expand_cluster(data, i, neighbors, cluster_id)
                cluster_id += 1
    
    def _get_neighbors(self, data, idx):
        neighbors = []
        for i, point in enumerate(data):
            if self._distance(data[idx], point) <= self.eps:
                neighbors.append(i)
        return neighbors
    
    def _expand_cluster(self, data, idx, neighbors, cluster_id):
        self.labels[idx] = cluster_id
        i = 0
        while i < len(neighbors):
            neighbor = neighbors[i]
            if self.labels[neighbor] == -1:
                self.labels[neighbor] = cluster_id
            if self.labels[neighbor] == -1:
                new_neighbors = self._get_neighbors(data, neighbor)
                if len(new_neighbors) >= self.min_points:
                    neighbors.extend(new_neighbors)
            i += 1
    
    def _distance(self, a, b):
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))
''', "DBSCAN für beliebige Cluster-Formen", "Clustering", "komplex", "v0.2"),
            
            ("SARSA Reinforcement", '''
import random

class SARSALearning:
    """SARSA: On-Policy Reinforcement Learning"""
    
    def __init__(self, states, actions, alpha=0.1, gamma=0.95, epsilon=0.1):
        self.states = states
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {s: {a: 0.0 for a in actions} for s in states}
    
    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        return max(self.q_table[state], key=self.q_table[state].get)
    
    def learn(self, state, action, reward, next_state, next_action):
        """SARSA Update"""
        current_q = self.q_table[state][action]
        next_q = self.q_table[next_state][next_action]
        new_q = current_q + self.alpha * (reward + self.gamma * next_q - current_q)
        self.q_table[state][action] = new_q
''', "SARSA: Alternative zu Q-Learning", "Reinforcement Learning", "mittel", "v0.3"),
            
            ("Markov Chain", '''
from collections import defaultdict

class MarkovChain:
    """Einfache Markov Chain für Sequenz-Modellierung"""
    
    def __init__(self, order=1):
        self.order = order
        self.transitions = defaultdict(lambda: defaultdict(int))
        self.totals = defaultdict(int)
    
    def train(self, sequence):
        """Trainiert die Markov Chain"""
        for i in range(len(sequence) - self.order):
            state = tuple(sequence[i:i + self.order])
            next_state = sequence[i + self.order]
            self.transitions[state][next_state] += 1
            self.totals[state] += 1
    
    def predict_next(self, state):
        """Vorhersage des nächsten Zustands"""
        if state not in self.transitions:
            return None
        
        # Wahrscheinlichkeiten berechnen
        probs = {k: v / self.totals[state] 
                for k, v in self.transitions[state].items()}
        
        # Wahrscheinlichste wählen
        return max(probs, key=probs.get)
    
    def generate_sequence(self, start, length=10):
        """Generiert Sequenz aus Startzustand"""
        sequence = list(start)
        for _ in range(length):
            state = tuple(sequence[-self.order:])
            next_state = self.predict_next(state)
            if next_state is None:
                break
            sequence.append(next_state)
        return sequence
''', "Markov Chains für Sequenz-Vorhersage", "Causal Learning", "mittel", "v0.4"),
        ]
        
        for title, code, desc, topic, complexity, version in examples:
            if not self.should_continue():
                return
            self.save_code(title, code, desc, topic, complexity, version)
    
    def research_advanced(self):
        """Fortgeschrittene Themen"""
        print("\n📦 v0.6-v0.8: Fortgeschrittene Themen")
        
        examples = [
            ("Attention Mechanismus", '''
import math

class SimpleAttention:
    """Vereinfachter Attention-Mechanismus"""
    
    def __init__(self, dim):
        self.dim = dim
        self.query_weights = [0.1] * dim
        self.key_weights = [0.1] * dim
        self.value_weights = [0.1] * dim
    
    def attention(self, query, keys, values):
        """Berechnet Attention-Scores"""
        scores = []
        for key in keys:
            # Dot-Product Attention
            score = sum(q * k for q, k in zip(query, key))
            scores.append(score)
        
        # Softmax
        exp_scores = [math.exp(s) for s in scores]
        sum_exp = sum(exp_scores)
        weights = [e / sum_exp for e in exp_scores]
        
        # Gewichtete Summe der Values
        output = [0.0] * len(values[0])
        for i, value in enumerate(values):
            for j, v in enumerate(value):
                output[j] += weights[i] * v
        
        return output, weights
''', "Attention für Multimodal-Fusion", "Multimodal", "komplex", "v0.6"),
            
            ("LSTM Cell", '''
import math

class SimpleLSTM:
    """Vereinfachte LSTM-Zelle"""
    
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.hidden = [0.0] * hidden_size
        self.cell = [0.0] * hidden_size
    
    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))
    
    def tanh(self, x):
        return math.tanh(x)
    
    def step(self, x):
        """Ein Zeitschritt"""
        # Vereinfachte Berechnung
        forget = [self.sigmoid(x[i] + self.hidden[i]) 
                  for i in range(self.hidden_size)]
        input_gate = [self.sigmoid(x[i] + self.hidden[i]) 
                      for i in range(self.hidden_size)]
        
        # Cell State aktualisieren
        self.cell = [self.cell[i] * forget[i] + input_gate[i] * self.tanh(x[i])
                     for i in range(self.hidden_size)]
        
        # Hidden State
        output = [self.sigmoid(x[i] + self.hidden[i]) 
                  for i in range(self.hidden_size)]
        self.hidden = [output[i] * self.tanh(self.cell[i]) 
                       for i in range(self.hidden_size)]
        
        return self.hidden
''', "LSTM für sequentielle Daten", "Memory", "komplex", "v0.7"),
            
            ("Tokenizer", '''
import re

class SimpleTokenizer:
    """Einfacher Text-Tokenizer"""
    
    def __init__(self):
        self.vocab = {}
        self.next_id = 0
    
    def tokenize(self, text):
        """Text in Tokens aufteilen"""
        # Kleinbuchstaben, Sonderzeichen entfernen
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        tokens = text.split()
        return tokens
    
    def encode(self, text):
        """Text zu Token-IDs"""
        tokens = self.tokenize(text)
        ids = []
        for token in tokens:
            if token not in self.vocab:
                self.vocab[token] = self.next_id
                self.next_id += 1
            ids.append(self.vocab[token])
        return ids
    
    def decode(self, ids):
        """Token-IDs zu Text"""
        reverse_vocab = {v: k for k, v in self.vocab.items()}
        tokens = [reverse_vocab.get(i, '<unk>') for i in ids]
        return ' '.join(tokens)
    
    def get_vocab_size(self):
        return len(self.vocab)
''', "Text-Tokenisierung für NLP", "Dialog", "mittel", "v0.8"),
        ]
        
        for title, code, desc, topic, complexity, version in examples:
            if not self.should_continue():
                return
            self.save_code(title, code, desc, topic, complexity, version)
    
    def research_system_integration(self):
        """System & Integration"""
        print("\n📦 v0.9-v1.0: System & Integration")
        
        examples = [
            ("Task Scheduler", '''
import threading
import time
from queue import PriorityQueue

class TaskScheduler:
    """Prioritätsbasierter Task-Scheduler"""
    
    def __init__(self):
        self.tasks = PriorityQueue()
        self.running = False
        self.thread = None
    
    def add_task(self, priority, func, args=()):
        """Fügt Task hinzu (niedrigere Zahl = höhere Priorität)"""
        self.tasks.put((priority, time.time(), func, args))
    
    def start(self):
        """Startet den Scheduler"""
        self.running = True
        self.thread = threading.Thread(target=self._run)
        self.thread.start()
    
    def _run(self):
        while self.running:
            if not self.tasks.empty():
                priority, timestamp, func, args = self.tasks.get()
                try:
                    func(*args)
                except Exception as e:
                    print(f"Task error: {e}")
            time.sleep(0.01)
    
    def stop(self):
        """Stoppt den Scheduler"""
        self.running = False
        if self.thread:
            self.thread.join()
''', "Task-Scheduler für autonome Abläufe", "Autonomie", "mittel", "v0.9"),
            
            ("Config Manager", '''
import json
import os

class ConfigManager:
    """Verwaltet Konfigurationen"""
    
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.config = self._load()
    
    def _load(self):
        """Lädt Konfiguration aus Datei"""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return self._default_config()
    
    def _default_config(self):
        """Standard-Konfiguration"""
        return {
            "version": "1.0.0",
            "debug": False,
            "modules": {},
            "limits": {
                "memory_mb": 1024,
                "cpu_percent": 80
            }
        }
    
    def get(self, key, default=None):
        """Holt Wert aus Konfiguration"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value
    
    def set(self, key, value):
        """Setzt Wert in Konfiguration"""
        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value
        self._save()
    
    def _save(self):
        """Speichert Konfiguration"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
''', "Konfigurations-Management", "Core System", "mittel", "v1.0"),
        ]
        
        for title, code, desc, topic, complexity, version in examples:
            if not self.should_continue():
                return
            self.save_code(title, code, desc, topic, complexity, version)
    
    def research_utilities(self):
        """Utilities & Tools"""
        print("\n📦 Utilities & Tools")
        
        examples = [
            ("Logger", '''
import logging
from datetime import datetime

class MachineLogger:
    """Zentraler Logger für Machine"""
    
    def __init__(self, name="machine", level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # Console Handler
        ch = logging.StreamHandler()
        ch.setLevel(level)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
    
    def info(self, msg):
        self.logger.info(msg)
    
    def debug(self, msg):
        self.logger.debug(msg)
    
    def warning(self, msg):
        self.logger.warning(msg)
    
    def error(self, msg):
        self.logger.error(msg)
    
    def log_decision(self, decision, context):
        """Loggt Entscheidungen mit Kontext"""
        self.info(f"Decision: {decision} | Context: {context}")
''', "Logging-System für Debugging", "Utilities", "einfach", "v0.1"),
            
            ("Profiler", '''
import time
from functools import wraps

class SimpleProfiler:
    """Einfacher Performance-Profiler"""
    
    def __init__(self):
        self.timings = {}
    
    def profile(self, func):
        """Decorator für Funktions-Timing"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            
            name = func.__name__
            if name not in self.timings:
                self.timings[name] = []
            self.timings[name].append(elapsed)
            
            return result
        return wrapper
    
    def report(self):
        """Zeigt Performance-Report"""
        print("Performance Report:")
        print("-" * 40)
        for name, times in self.timings.items():
            avg = sum(times) / len(times)
            print(f"{name}: {avg:.4f}s (avg, {len(times)} calls)")
''', "Performance-Profiling", "Utilities", "einfach", "v0.5"),
            
            ("Data Validator", '''
class DataValidator:
    """Validiert Datenstrukturen"""
    
    @staticmethod
    def is_valid_vector(vec, expected_dim=None):
        """Prüft ob Vektor gültig ist"""
        if not isinstance(vec, (list, tuple)):
            return False
        if len(vec) == 0:
            return False
        if expected_dim and len(vec) != expected_dim:
            return False
        try:
            [float(x) for x in vec]
            return True
        except:
            return False
    
    @staticmethod
    def is_valid_label(label):
        """Prüft ob Label gültig ist"""
        return isinstance(label, (str, int, float))
    
    @staticmethod
    def validate_dataset(X, y):
        """Validiert Trainingsdaten"""
        if len(X) != len(y):
            return False, "X und y haben unterschiedliche Längen"
        if len(X) == 0:
            return False, "Leerer Datensatz"
        return True, "OK"
''', "Daten-Validierung", "Utilities", "einfach", "v0.1"),
        ]
        
        for title, code, desc, topic, complexity, version in examples:
            if not self.should_continue():
                return
            self.save_code(title, code, desc, topic, complexity, version)

if __name__ == "__main__":
    researcher = DeepResearcher()
    researcher.research_all()
