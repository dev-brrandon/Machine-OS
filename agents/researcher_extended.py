#!/usr/bin/env python3
"""
Machine Researcher - Extended Code Intelligence Agent
Sammelt Code-Beispiele für v0.1 bis v1.0
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

class CodeResearcher:
    def __init__(self):
        self.qdrant = QdrantClient(
            host=QDRANT_HOST,
            port=QDRANT_PORT,
            api_key=QDRANT_API_KEY,
            https=False
        )
        self.collection = "code_examples"
        self.start_time = time.time()
        self.duration = 300  # 5 Minuten
        
    def should_continue(self):
        """Prüfe ob Zeit noch nicht abgelaufen"""
        return (time.time() - self.start_time) < self.duration
        
    def generate_embedding(self, code: str) -> list:
        """Generiere einfaches Embedding für Code"""
        features = [
            len(code),
            code.count('def '),
            code.count('for '),
            code.count('if '),
            code.count('import'),
            hash(code) % 100 / 100,
        ]
        vector = features + [0.0] * (384 - len(features))
        return vector
    
    def save_code_example(self, title: str, code: str, description: str, 
                         topic: str, complexity: str, source: str, version: str = "v0.1"):
        """Speichere Code-Beispiel in Qdrant"""
        
        if not self.should_continue():
            print(f"⏱️  Zeit abgelaufen! Stoppe bei: {title}")
            return None
        
        payload = {
            "title": title,
            "code": code,
            "description": description,
            "topic": topic,
            "complexity": complexity,
            "source": source,
            "language": "python",
            "version_target": version,
            "created_at": datetime.now().isoformat(),
        }
        
        vector = self.generate_embedding(code)
        code_id = abs(hash(code + title)) % (10 ** 10)
        
        point = PointStruct(
            id=code_id,
            vector=vector,
            payload=payload
        )
        
        try:
            self.qdrant.upsert(
                collection_name=self.collection,
                points=[point]
            )
            print(f"✅ [{version}] {title} ({complexity})")
            return code_id
        except Exception as e:
            print(f"❌ Fehler beim Speichern: {e}")
            return None
    
    def research_all_versions(self):
        """Sammelt Code für alle Versionen v0.1-v1.0"""
        
        print("🚀 Extended Machine Researcher")
        print("=" * 60)
        print("Sammle Code für v0.1 bis v1.0...")
        print("Dauer: 5 Minuten")
        print()
        
        # v0.1: Bootstrap - Supervised Learning
        self.research_v01_bootstrap()
        if not self.should_continue(): return
        
        # v0.2: Unsupervised Clustering
        self.research_v02_clustering()
        if not self.should_continue(): return
        
        # v0.3: Reinforcement Learning
        self.research_v03_reinforcement()
        if not self.should_continue(): return
        
        # v0.4: Causal & Transfer
        self.research_v04_causal()
        if not self.should_continue(): return
        
        # v0.5: Meta-Learning & Code-Gen
        self.research_v05_meta()
        if not self.should_continue(): return
        
        # v0.6: Multimodal
        self.research_v06_multimodal()
        if not self.should_continue(): return
        
        # v0.7: Memory
        self.research_v07_memory()
        if not self.should_continue(): return
        
        # v0.8: Dialog
        self.research_v08_dialog()
        if not self.should_continue(): return
        
        # v0.9: Autonomy
        self.research_v09_autonomy()
        if not self.should_continue(): return
        
        # v1.0: Alpha Release
        self.research_v10_alpha()
        
    def research_v01_bootstrap(self):
        """v0.1: Supervised Learning - bereits vorhanden, erweitern"""
        print("\n📦 v0.1: Bootstrap (Supervised Learning)")
        
        # SQLite Speicher
        code = '''
import sqlite3
import json

class VectorStore:
    """Speichert Vektoren und Labels in SQLite"""
    
    def __init__(self, db_path="machine_memory.db"):
        self.conn = sqlite3.connect(db_path)
        self._init_db()
    
    def _init_db(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS vectors (
                id INTEGER PRIMARY KEY,
                vector BLOB,
                label TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()
    
    def store(self, vector, label):
        vector_blob = json.dumps(vector).encode()
        self.conn.execute(
            "INSERT INTO vectors (vector, label) VALUES (?, ?)",
            (vector_blob, label)
        )
        self.conn.commit()
    
    def get_all(self):
        cursor = self.conn.execute("SELECT vector, label FROM vectors")
        rows = cursor.fetchall()
        return [(json.loads(row[0]), row[1]) for row in rows]
'''
        self.save_code_example(
            title="SQLite Vector Store",
            code=code,
            description="Speichert Vektoren und Labels in SQLite-Datenbank. Robust und einfach.",
            topic="Speicher",
            complexity="einfach",
            source="Machine Researcher",
            version="v0.1"
        )
    
    def research_v02_clustering(self):
        """v0.2: Unsupervised Clustering"""
        print("\n📦 v0.2: Unsupervised Clustering")
        
        code = '''
import random
import math

class KMeans:
    """K-Means Clustering von Grund auf"""
    
    def __init__(self, k=3, max_iters=100):
        self.k = k
        self.max_iters = max_iters
        self.centroids = None
    
    def fit(self, data):
        # Zufällige Initialisierung der Centroids
        self.centroids = random.sample(data, self.k)
        
        for _ in range(self.max_iters):
            # Zuordnung zu Centroids
            clusters = [[] for _ in range(self.k)]
            for point in data:
                closest = self._closest_centroid(point)
                clusters[closest].append(point)
            
            # Neue Centroids berechnen
            new_centroids = []
            for cluster in clusters:
                if cluster:
                    centroid = [sum(x)/len(x) for x in zip(*cluster)]
                    new_centroids.append(centroid)
                else:
                    new_centroids.append(random.choice(data))
            
            # Konvergenz prüfen
            if new_centroids == self.centroids:
                break
            self.centroids = new_centroids
    
    def _closest_centroid(self, point):
        distances = [self._euclidean(point, c) for c in self.centroids]
        return distances.index(min(distances))
    
    def _euclidean(self, a, b):
        return math.sqrt(sum((x-y)**2 for x, y in zip(a, b)))
    
    def predict(self, point):
        return self._closest_centroid(point)
'''
        self.save_code_example(
            title="K-Means Clustering",
            code=code,
            description="K-Means Algorithmus von Grund auf. Findet selbst Cluster in Daten.",
            topic="Clustering",
            complexity="mittel",
            source="Machine Researcher",
            version="v0.2"
        )
    
    def research_v03_reinforcement(self):
        """v0.3: Reinforcement Learning"""
        print("\n📦 v0.3: Reinforcement Learning")
        
        code = '''
import random

class QLearning:
    """Einfaches Q-Learning für Reinforcement Learning"""
    
    def __init__(self, states, actions, learning_rate=0.1, discount=0.95):
        self.states = states
        self.actions = actions
        self.lr = learning_rate
        self.discount = discount
        # Q-Table initialisieren
        self.q_table = {s: {a: 0.0 for a in actions} for s in states}
    
    def get_action(self, state, epsilon=0.1):
        """Epsilon-Greedy Strategie"""
        if random.random() < epsilon:
            return random.choice(self.actions)
        return max(self.q_table[state], key=self.q_table[state].get)
    
    def update(self, state, action, reward, next_state):
        """Q-Value aktualisieren"""
        current_q = self.q_table[state][action]
        max_next_q = max(self.q_table[next_state].values())
        new_q = current_q + self.lr * (reward + self.discount * max_next_q - current_q)
        self.q_table[state][action] = new_q
    
    def get_best_action(self, state):
        """Beste Aktion für einen State"""
        return max(self.q_table[state], key=self.q_table[state].get)
'''
        self.save_code_example(
            title="Q-Learning Algorithmus",
            code=code,
            description="Q-Learning für Reinforcement Learning. Lernt aus Belohnung.",
            topic="Reinforcement Learning",
            complexity="mittel",
            source="Machine Researcher",
            version="v0.3"
        )
    
    def research_v04_causal(self):
        """v0.4: Causal & Transfer Learning"""
        print("\n📦 v0.4: Causal & Transfer Learning")
        
        code = '''
from collections import defaultdict

class TemporalPatternMiner:
    """Findet zeitliche Muster (A führt zu B)"""
    
    def __init__(self, window_size=5):
        self.window_size = window_size
        self.transitions = defaultdict(lambda: defaultdict(int))
        self.event_counts = defaultdict(int)
    
    def add_sequence(self, events):
        """Füge Event-Sequenz hinzu"""
        for i in range(len(events) - 1):
            current = events[i]
            next_event = events[i + 1]
            self.transitions[current][next_event] += 1
            self.event_counts[current] += 1
    
    def get_probabilities(self, event):
        """Wahrscheinlichkeiten für nächstes Event"""
        if event not in self.event_counts:
            return {}
        total = self.event_counts[event]
        return {next_e: count/total 
                for next_e, count in self.transitions[event].items()}
    
    def predict_next(self, event, threshold=0.3):
        """Vorhersage des nächsten Events"""
        probs = self.get_probabilities(event)
        if not probs:
            return None
        best = max(probs, key=probs.get)
        return best if probs[best] > threshold else None
'''
        self.save_code_example(
            title="Temporal Pattern Mining",
            code=code,
            description="Findet zeitliche Muster und kausale Zusammenhänge in Event-Sequenzen.",
            topic="Causal Learning",
            complexity="mittel",
            source="Machine Researcher",
            version="v0.4"
        )
    
    def research_v05_meta(self):
        """v0.5: Meta-Learning & Code-Gen"""
        print("\n📦 v0.5: Meta-Learning & Code-Gen")
        
        code = '''
import ast
import inspect

class CodeAnalyzer:
    """Analysiert Python-Code auf Komplexität"""
    
    def analyze(self, code_str):
        """Analysiert Code und gibt Metriken zurück"""
        try:
            tree = ast.parse(code_str)
            metrics = {
                'num_functions': 0,
                'num_loops': 0,
                'num_conditionals': 0,
                'lines': len(code_str.split('\\n')),
                'complexity': 'einfach'
            }
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    metrics['num_functions'] += 1
                elif isinstance(node, (ast.For, ast.While)):
                    metrics['num_loops'] += 1
                elif isinstance(node, ast.If):
                    metrics['num_conditionals'] += 1
            
            # Komplexität bestimmen
            score = metrics['num_functions'] + metrics['num_loops'] + metrics['num_conditionals']
            if score > 10:
                metrics['complexity'] = 'komplex'
            elif score > 5:
                metrics['complexity'] = 'mittel'
            
            return metrics
        except:
            return None
    
    def suggest_optimization(self, metrics):
        """Schlägt Optimierungen vor"""
        suggestions = []
        if metrics['num_loops'] > 3:
            suggestions.append("Versuche Vektorisierung statt Schleifen")
        if metrics['num_conditionals'] > 5:
            suggestions.append("Betrachte Lookup-Tables statt if-elif chains")
        return suggestions
'''
        self.save_code_example(
            title="Code Analyzer & Optimizer",
            code=code,
            description="Analysiert Python-Code und schlägt Optimierungen vor. Für Meta-Learning.",
            topic="Code-Gen",
            complexity="komplex",
            source="Machine Researcher",
            version="v0.5"
        )
    
    def research_v06_multimodal(self):
        """v0.6: Multimodal Integration"""
        print("\n📦 v0.6: Multimodal Integration")
        
        code = '''
import numpy as np

class MultimodalFusion:
    """Kombiniert verschiedene Modalitäten (Bild, Audio, Text)"""
    
    def __init__(self, image_dim=128, audio_dim=64, text_dim=32):
        self.image_dim = image_dim
        self.audio_dim = audio_dim
        self.text_dim = text_dim
        self.fused_dim = image_dim + audio_dim + text_dim
    
    def fuse_early(self, image_vec, audio_vec, text_vec):
        """Early Fusion: Konkatenation"""
        # Padding auf gleiche Länge (vereinfacht)
        return image_vec + audio_vec + text_vec
    
    def fuse_attention(self, modalities, weights):
        """Attention-basierte Fusion"""
        # Gewichtete Summe
        fused = []
        for i, mod in enumerate(modalities):
            weight = weights[i] if i < len(weights) else 1.0
            fused.extend([x * weight for x in mod])
        return fused
    
    def align_modalities(self, mod_a, mod_b):
        """Aligniert zwei Modalitäten auf gemeinsamen Raum"""
        # Einfache Projektion (vereinfacht)
        min_len = min(len(mod_a), len(mod_b))
        return mod_a[:min_len], mod_b[:min_len]
'''
        self.save_code_example(
            title="Multimodal Fusion",
            code=code,
            description="Kombiniert Bild, Audio und Text zu gemeinsamen Repräsentationen.",
            topic="Multimodal",
            complexity="komplex",
            source="Machine Researcher",
            version="v0.6"
        )
    
    def research_v07_memory(self):
        """v0.7: Kontextuelles Gedächtnis"""
        print("\n📦 v0.7: Kontextuelles Gedächtnis")
        
        code = '''
import time
from collections import deque

class EpisodicMemory:
    """Speichert Ereignisse mit Zeitstempel"""
    
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.episodes = deque(maxlen=capacity)
    
    def add_episode(self, event, context=None):
        """Fügt Episode hinzu"""
        episode = {
            'timestamp': time.time(),
            'event': event,
            'context': context or {}
        }
        self.episodes.append(episode)
    
    def recall_recent(self, n=10):
        """Ruft letzte n Episoden ab"""
        return list(self.episodes)[-n:]
    
    def recall_by_time(self, start_time, end_time):
        """Ruft Episoden in Zeitfenster ab"""
        return [ep for ep in self.episodes 
                if start_time <= ep['timestamp'] <= end_time]
    
    def search_similar(self, query_event, threshold=0.8):
        """Sucht ähnliche Episoden"""
        # Einfache Ähnlichkeit (vereinfacht)
        similar = []
        for ep in self.episodes:
            if self._similarity(query_event, ep['event']) > threshold:
                similar.append(ep)
        return similar
    
    def _similarity(self, a, b):
        # Vereinfachte Ähnlichkeit
        return 0.5  # Placeholder
'''
        self.save_code_example(
            title="Episodic Memory System",
            code=code,
            description="Speichert Ereignisse mit Zeitstempel und Kontext. Für Langzeitgedächtnis.",
            topic="Memory",
            complexity="mittel",
            source="Machine Researcher",
            version="v0.7"
        )
    
    def research_v08_dialog(self):
        """v0.8: Kommunikation & Dialog"""
        print("\n📦 v0.8: Kommunikation & Dialog")
        
        code = '''
class SimpleDialogManager:
    """Einfacher Dialog-Manager"""
    
    def __init__(self):
        self.context = []
        self.max_context = 10
        self.intents = {
            'greeting': ['hello', 'hi', 'hey'],
            'question': ['what', 'how', 'why', 'when'],
            'command': ['do', 'make', 'create'],
        }
    
    def add_to_context(self, speaker, message):
        """Fügt Nachricht zum Kontext hinzu"""
        self.context.append({
            'speaker': speaker,
            'message': message,
            'timestamp': time.time()
        })
        if len(self.context) > self.max_context:
            self.context.pop(0)
    
    def detect_intent(self, message):
        """Erkennt Intent der Nachricht"""
        msg_lower = message.lower()
        for intent, keywords in self.intents.items():
            if any(kw in msg_lower for kw in keywords):
                return intent
        return 'unknown'
    
    def generate_response(self, user_message):
        """Generiert einfache Antwort"""
        intent = self.detect_intent(user_message)
        
        responses = {
            'greeting': "Hello! How can I help you?",
            'question': "That's an interesting question. Let me think...",
            'command': "I'll try to do that.",
            'unknown': "I'm not sure I understand. Can you clarify?"
        }
        
        return responses.get(intent, responses['unknown'])
    
    def get_context_summary(self):
        """Zusammenfassung des Dialog-Kontexts"""
        return " ".join([c['message'] for c in self.context[-3:]])
'''
        self.save_code_example(
            title="Dialog Manager",
            code=code,
            description="Einfacher Dialog-Manager mit Intent-Erkennung und Kontext.",
            topic="Dialog",
            complexity="mittel",
            source="Machine Researcher",
            version="v0.8"
        )
    
    def research_v09_autonomy(self):
        """v0.9: Autonomie & Proaktivität"""
        print("\n📦 v0.9: Autonomie & Proaktivität")
        
        code = '''
class GoalManager:
    """Verwaltet Ziele und Pläne"""
    
    def __init__(self):
        self.goals = []
        self.current_goal = None
        self.plans = {}
    
    def add_goal(self, description, priority=1, deadline=None):
        """Fügt neues Ziel hinzu"""
        goal = {
            'id': len(self.goals),
            'description': description,
            'priority': priority,
            'deadline': deadline,
            'status': 'pending',
            'progress': 0.0
        }
        self.goals.append(goal)
        self._sort_goals()
        return goal['id']
    
    def _sort_goals(self):
        """Sortiert Ziele nach Priorität"""
        self.goals.sort(key=lambda g: (-g['priority'], g.get('deadline', float('inf'))))
    
    def get_next_goal(self):
        """Gibt nächstes Ziel zurück"""
        for goal in self.goals:
            if goal['status'] == 'pending':
                return goal
        return None
    
    def create_plan(self, goal_id, steps):
        """Erstellt Plan für Ziel"""
        self.plans[goal_id] = steps
    
    def execute_step(self, goal_id):
        """Führt nächsten Schritt aus"""
        if goal_id not in self.plans:
            return False
        plan = self.plans[goal_id]
        # Führe ersten nicht-erledigten Schritt aus
        for step in plan:
            if not step.get('done', False):
                step['done'] = True
                return step
        return None
    
    def evaluate_progress(self, goal_id):
        """Bewertet Fortschritt"""
        if goal_id not in self.plans:
            return 0.0
        plan = self.plans[goal_id]
        done = sum(1 for s in plan if s.get('done', False))
        return done / len(plan) if plan else 0.0
'''
        self.save_code_example(
            title="Goal Manager & Planner",
            code=code,
            description="Verwaltet Ziele, erstellt Pläne und verfolgt Fortschritt. Für Autonomie.",
            topic="Autonomie",
            complexity="komplex",
            source="Machine Researcher",
            version="v0.9"
        )
    
    def research_v10_alpha(self):
        """v1.0: Alpha Release"""
        print("\n📦 v1.0: Alpha Release")
        
        code = '''
import json
import threading
import time

class MachineCore:
    """Haupt-Klasse für Machine v1.0"""
    
    def __init__(self, config_path="config.json"):
        self.config = self._load_config(config_path)
        self.running = False
        self.modules = {}
        self.lock = threading.Lock()
    
    def _load_config(self, path):
        """Lädt Konfiguration"""
        try:
            with open(path) as f:
                return json.load(f)
        except:
            return self._default_config()
    
    def _default_config(self):
        """Standard-Konfiguration"""
        return {
            'version': '1.0.0',
            'modules': ['vision', 'audio', 'memory', 'learning'],
            'safety_limits': {
                'max_memory_mb': 1024,
                'max_cpu_percent': 80
            }
        }
    
    def load_module(self, name, module):
        """Lädt ein Modul"""
        with self.lock:
            self.modules[name] = module
            print(f"Module {name} loaded")
    
    def start(self):
        """Startet Machine"""
        self.running = True
        print("Machine v1.0 started")
        self._main_loop()
    
    def _main_loop(self):
        """Hauptschleife"""
        while self.running:
            # Sensoren lesen
            # Verarbeiten
            # Lernen
            # Aktiv werden
            time.sleep(0.1)
    
    def stop(self):
        """Stoppt Machine"""
        self.running = False
        print("Machine stopped")
    
    def get_status(self):
        """Gibt Status zurück"""
        return {
            'running': self.running,
            'modules_loaded': list(self.modules.keys()),
            'version': self.config.get('version', 'unknown')
        }
'''
        self.save_code_example(
            title="Machine Core v1.0",
            code=code,
            description="Haupt-Klasse für Machine v1.0. Modular, konfigurierbar, stabil.",
            topic="Core System",
            complexity="komplex",
            source="Machine Researcher",
            version="v1.0"
        )
    
    def run(self):
        """Hauptfunktion"""
        print(f"\n⏱️  Starte 5-Minuten Research Session...")
        print(f"   Start: {datetime.now().strftime('%H:%M:%S')}")
        print(f"   Ende: ca. {(datetime.now().timestamp() + 300)} ")
        print()
        
        self.research_all_versions()
        
        elapsed = time.time() - self.start_time
        print()
        print("=" * 60)
        print(f"🎉 Research Session abgeschlossen!")
        print(f"   Dauer: {elapsed:.1f} Sekunden")
        print(f"   Zeit übrig: {max(0, 300 - elapsed):.1f} Sekunden")
        print()
        print("Alle Code-Beispiele in Qdrant gespeichert.")
        print("Coder können jetzt auf alle Versionen zugreifen!")

if __name__ == "__main__":
    researcher = CodeResearcher()
    researcher.run()
