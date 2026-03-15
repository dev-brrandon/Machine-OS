# Machine-OS

OS Development Project - Machine

## Projekt-Struktur

```
Machine-OS/
├── docs/               # Dokumentation
│   ├── architecture/   # Architektur-Dokumente
│   ├── proposals/      # Feature-Proposals
│   └── api/            # API-Dokumentation
├── src/                # Quellcode
│   ├── kernel/         # Kernel-Code
│   ├── drivers/        # Treiber
│   └── lib/            # Bibliotheken
├── tests/              # Tests
├── tools/              # Build-Tools & Scripts
└── README.md           # Diese Datei
```

## Team

**Chefs:**
- Brandon (@dev-brrandon)
- Klaw (@openclaw-agent)

**Sub-Agenten:**
- Researcher
- Coder 1 & 2
- Code-Prüfer

## Workflow

1. Chefs besprechen → Einigung
2. Befehle an Sub-Agenten
3. Sub-Agenten entwickeln → commit → push
4. Code-Prüfer reviewed
5. Merge in main

## Getting Started

```bash
# Clonen
git clone git@github.com:dev-brrandon/Machine-OS.git
cd Machine-OS

# Status checken
git status

# Neue Feature-Branch erstellen
git checkout -b feature/name

# Änderungen committen
git add .
git commit -m "Beschreibung"
git push origin feature/name
```

## Lizenz

MIT License
