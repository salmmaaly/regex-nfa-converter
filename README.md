# 📌 Regex to NFA Converter (Thompson’s Construction)

## 📖 Overview
This project converts a **Regular Expression (Regex)** into a **Non-deterministic Finite Automaton (NFA)** using **Thompson’s Construction Algorithm**.

It supports parsing a regex expression, building an NFA, displaying its transition table (including ε-transitions), and visually rendering the automaton using Graphviz.

---

## 👥 Team Members
- Salma Zakaria — 231001369  
- Tasneem Elsharkawy — 231001398  
- Amr Ahmed — 231000719  
- Rodina Ahmed — 231002758  

---

## ✨ Features
- Supports regex operations:
  - Concatenation
  - Union (`|`)
  - Kleene Star (`*`)
  - Plus (`+`)
  - Optional (`?`)
- Tokenization and recursive descent parsing
- Thompson’s Construction Algorithm for NFA generation
- Transition table with ε-transitions
- Graph visualization using Graphviz
- Automatic PNG output of the NFA

---

## ⚙️ Requirements

### Install Python dependencies
```bash
pip install graphviz