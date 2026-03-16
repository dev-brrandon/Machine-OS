#!/usr/bin/env python3
"""
Machine Research Database Setup
Initialisiert Qdrant Collections für Forschungsdaten
"""

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

# Verbindung zu Qdrant (Port 32773)
client = QdrantClient(
    host="187.77.67.80", 
    port=32773,
    api_key="qJ4icfeaDcrK7p4sX91sIb4gh7H61GFU",
    https=False
)

print("🔧 Initialisiere Machine Research Database...")

# Collection 1: Code Examples
# Speichert Code-Beispiele als Vektoren + Metadaten
if not client.collection_exists("code_examples"):
    client.create_collection(
        collection_name="code_examples",
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )
    print("✅ Collection 'code_examples' erstellt")
else:
    print("ℹ️  Collection 'code_examples' existiert bereits")

# Collection 2: Research Findings
# Speichert Forschungsergebnisse
if not client.collection_exists("research_findings"):
    client.create_collection(
        collection_name="research_findings",
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )
    print("✅ Collection 'research_findings' erstellt")
else:
    print("ℹ️  Collection 'research_findings' existiert bereits")

# Collection 3: Test Results
# Speichert Test-Ergebnisse von Codern
if not client.collection_exists("test_results"):
    client.create_collection(
        collection_name="test_results",
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )
    print("✅ Collection 'test_results' erstellt")
else:
    print("ℹ️  Collection 'test_results' existiert bereits")

print("\n🎉 Machine Research Database bereit!")
print("   - code_examples: Für Code-Beispiele")
print("   - research_findings: Für Forschungsergebnisse")
print("   - test_results: Für Test-Ergebnisse")
