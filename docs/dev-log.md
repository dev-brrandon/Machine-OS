# Machine Development Log

> Roadmap & Sub-Agenten Aufträge

---

## Übersicht

| Version | Fokus | Zeitrahmen | Status |
|---------|-------|------------|--------|
| v0.1 | Bootstrap - Supervised Learning | 2 Wochen | 🔄 In Planung |
| v0.2 | Unsupervised Clustering | 2 Wochen | ⏳ Wartet |
| v0.3 | Reinforcement Learning | 2 Wochen | ⏳ Wartet |
| v0.4 | Causal & Transfer Learning | 1 Monat | ⏳ Wartet |
| v0.5 | Meta-Learning & Code-Gen | 1 Monat | ⏳ Wartet |

---

## v0.1 - Bootstrap (Supervised Learning)

**Ziel:** Machine kann durch menschliches Labeln lernen

**Funktionalität:**
- Rohdaten-Input (Pixel, Audio)
- Einfache Vektor-Embeddings
- Speicherung: Vektor + Label
- Abfrage: "Was ist das?" → Ähnlichste Antwort aus Speicher

**Sub-Agenten Aufträge:**

### Researcher
- [ ] Recherchiere: Wie funktioniert k-NN (k-nearest neighbors) Algorithmus?
- [ ] Recherchiere: Einfache Methoden für Bild-zu-Vektor Konvertierung (ohne Deep Learning)
- [ ] Recherchiere: Audio-Feature-Extraktion (Grundlagen)

### Coder 1
- [ ] Implementiere `utils/math_ops.py`: Matrix-Multiplikation, Vektor-Operationen
- [ ] Implementiere `core/memory.py`: Speicher für Vektoren + Labels (SQLite oder JSON)
- [ ] Implementiere `core/pattern.py`: k-NN Algorithmus von Grund auf

### Coder 2
- [ ] Implementiere `sensors/camera.py`: Webcam-Rohdaten-Capture (nur Pixel, keine Erkennung!)
- [ ] Implementiere `sensors/microphone.py`: Audio-Rohdaten-Capture (nur Wellenformen)
- [ ] Implementiere `interface/teach.py`: CLI für menschliches Labeln

### Code-Prüfer
- [ ] Review: Alle mathematischen Operationen testen
- [ ] Review: Speicher-Effizienz prüfen
- [ ] Review: Sensor-Code auf Fehlerbehandlung prüfen

**Akzeptanzkriterien:**
- [ ] Machine kann zwischen 3 verschiedenen Objekten unterscheiden (nach Labeln)
- [ ] Machine fragt "Was ist das?" bei unbekannten Inputs
- [ ] Machine speichert neue Labels korrekt
- [ ] Machine erkennt bekannte Objekte mit >80% Genauigkeit

---

## v0.2 - Unsupervised Clustering

**Ziel:** Machine findet selbst Muster, ohne menschliche Labels

**Funktionalität:**
- Clustering-Algorithmus (k-means oder DBSCAN, selbst implementiert)
- Automatische Gruppierung ähnlicher Inputs
- Mensch kann Cluster nachträglich benennen

**Sub-Agenten Aufträge:**

### Researcher
- [ ] Recherchiere: k-means Algorithmus (Schritt-für-Schritt)
- [ ] Recherchiere: DBSCAN Algorithmus (Alternative zu k-means)
- [ ] Recherchiere: Wie wählt man optimale Cluster-Anzahl?

### Coder 1
- [ ] Implementiere `core/unsupervised.py`: k-means von Grund auf
- [ ] Implementiere Cluster-Visualisierung (Text-basiert oder einfache Bilder)
- [ ] Erweitere `core/memory.py`: Cluster-Speicherung

### Coder 2
- [ ] Implementiere `core/metrics.py`: Distanz-Metriken (Euklidisch, Cosine)
- [ ] Implementiere `interface/cluster_name.py`: Mensch benennt gefundene Cluster
- [ ] Teste Clustering mit verschiedenen Datensätzen

### Code-Prüfer
- [ ] Review: Clustering-Algorithmus auf Korrektheit
- [ ] Review: Distanz-Metriken verifizieren
- [ ] Performance-Test: Wie schnell bei vielen Daten?

**Akzeptanzkriterien:**
- [ ] Machine findet 3-5 Cluster in ungelabelten Daten
- [ ] Cluster sind sinnvoll (ähnliche Dinge zusammen)
- [ ] Mensch kann Cluster nachträglich benennen
- [ ] Neue Daten werden korrekt zugeordnet

---

## v0.3 - Reinforcement Learning

**Ziel:** Machine lernt aus Belohnung und Bestrafung

**Funktionalität:**
- Vorhersagen machen
- Feedback erhalten (gut/schlecht)
- Gewichte anpassen
- Trial-and-Error Lernen

**Sub-Agenten Aufträge:**

### Researcher
- [ ] Recherchiere: Q-Learning (Grundlagen)
- [ ] Recherchiere: Einfache Reward-Funktionen
- [ ] Recherchiere: Exploration vs Exploitation

### Coder 1
- [ ] Implementiere `core/reinforcement.py`: Q-Learning Algorithmus
- [ ] Implementiere `core/predict.py`: Vorhersage-Engine
- [ ] Implementiere Reward-System (positive/negative Verstärkung)

### Coder 2
- [ ] Implementiere `interface/feedback.py`: Mensch gibt Feedback
- [ ] Implementiere Lern-Rate-Anpassung
- [ ] Erstelle Test-Szenarien für Reinforcement

### Code-Prüfer
- [ ] Review: Q-Learning Implementierung
- [ ] Review: Reward-Berechnung
- [ ] Test: Konvergiert das Lernen?

**Akzeptanzkriterien:**
- [ ] Machine lernt eine einfache Aufgabe durch Trial-and-Error
- [ ] Machine verbessert sich über Zeit
- [ ] Machine balanciert Exploration und Exploitation

---

## v0.4 - Causal & Transfer Learning

**Ziel:** Machine versteht Ursache-Wirkung und überträgt Wissen

**Funktionalität:**
- Zeitliche Muster erkennen (A führt zu B)
- Wissen auf neue Domänen übertragen
- Abstrakte Konzepte bilden

**Sub-Agenten Aufträge:**

### Researcher
- [ ] Recherchiere: Zeitliche Korrelation vs Kausalität
- [ ] Recherchiere: Transfer Learning Methoden (einfache Ansätze)
- [ ] Recherchiere: Abstraktion in neuronalen Netzen

### Coder 1
- [ ] Implementiere `core/causal.py`: Zeitliche Muster-Erkennung
- [ ] Implementiere `core/transfer.py`: Wissenstransfer zwischen Domänen
- [ ] Implementiere Abstraktions-Layer

### Coder 2
- [ ] Implementiere Zeitfenster für Muster (sliding window)
- [ ] Implementiere Ähnlichkeits-Mapping zwischen Domänen
- [ ] Teste Transfer auf verschiedene Datentypen

### Code-Prüfer
- [ ] Review: Kausalitäts-Erkennung
- [ ] Review: Transfer-Mechanismus
- [ ] Test: Funktioniert Transfer wirklich?

**Akzeptanzkriterien:**
- [ ] Machine erkennt: "Nach X kommt oft Y"
- [ ] Machine überträgt gelerntes auf neue Situationen
- [ ] Machine bildet abstrakte Konzepte

---

## v0.5 - Meta-Learning & Code-Gen

**Ziel:** Machine verbessert sich selbst durch Code-Generierung

**Funktionalität:**
- Analysiert eigene Performance
- Generiert Code für bessere Algorithmen
- Selbst-Modifikation

**Sub-Agenten Aufträge:**

### Researcher
- [ ] Recherchiere: Meta-Learning (Learning to learn)
- [ ] Recherchiere: Code-Generierung durch KI (Grundlagen)
- [ ] Recherchiere: Self-modifying code (Sicherheitsaspekte)

### Coder 1
- [ ] Implementiere `meta/analyze.py`: Performance-Analyse
- [ ] Implementiere `meta/code_gen.py`: Code-Generierungs-Engine
- [ ] Implementiere Sandbox für sichere Code-Ausführung

### Coder 2
- [ ] Implementiere `meta/optimize.py`: Algorithmus-Optimierung
- [ ] Implementiere Versions-Kontrolle für selbst-generierten Code
- [ ] Erstelle Test-Framework für generierten Code

### Code-Prüfer
- [ ] Review: Code-Generierung (Sicherheit!)
- [ ] Review: Sandbox-Implementierung
- [ ] Review: Versions-Kontrolle

**Akzeptanzkriterien:**
- [ ] Machine erkennt eigene Schwächen
- [ ] Machine generiert verbesserten Code
- [ ] Generierter Code ist sicher und funktioniert
- [ ] Machine wird über Zeit effizienter

---

## Allgemeine Regeln

### Für alle Sub-Agenten

1. **Keine externen KI-Bibliotheken** (nur NumPy für Arrays)
2. **Alles dokumentieren** (Kommentare, Docstrings)
3. **Tests schreiben** (vor dem Commit)
4. **Chefs informieren** bei Unklarheiten
5. **Git workflow:**
   - Branch erstellen: `git checkout -b feature/v0.X-name`
   - Committen: `git commit -m "Beschreibung"`
   - Pushen: `git push origin feature/v0.X-name`
   - Code-Prüfer reviewt
   - Merge in main

### Prioritäten

1. **Funktionalität** vor Perfektion
2. **Verständlichkeit** vor Cleverness
3. **Testbarkeit** vor Features
4. **Sicherheit** vor allem (besonders bei v0.5)

---

## Aktueller Stand

**Version:** v0.1 - Bootstrap  
**Status:** In Planung  
**Nächster Schritt:** Sub-Agenten spawnen und Aufträge verteilen  

**Chefs:** Brandon & Klaw 🦾

---

*Letzte Aktualisierung: 2026-03-16*
