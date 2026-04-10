# 📌 Regex to NFA Converter (Thompson’s Construction Algorithm)

## 👥 Team Members
- Salma Zakaria — 231001369  
- Tasneem Elsharkawy — 231001398  
- Amr Ahmed — 231000719  
- Rodina Ahmed — 231002758  

---

## 📖 Project Description

This project converts a **Regular Expression (Regex)** into a **Non-deterministic Finite Automaton (NFA)** using **Thompson’s Construction Algorithm**.

It takes a regex as input, parses it using a recursive descent parser, and builds an equivalent NFA using ε-transitions. The system then displays the result as both a transition table and a graphical visualization using Graphviz.

---

## 📥 Input Format

A regular expression string is entered by the user.

Example:
a(b|c)*a

Supported operators:
- Concatenation: ab  
- Union: a|b  
- Kleene Star: a*  
- Plus: a+  
- Optional: a?  
- Grouping: ( )

---

## 📤 Output Format

### 1. Transition Table (Console Output)
State | Input | Next
----------------------
->q0  | a     | q1  
q1    | ε     | q2  
q1    | ε     | q3  
q2    | b     | q4  
q3    | c     | q5  
q4    | ε     | q6  
q5    | ε     | q6  
Final: ['q6']

---

### 2. Graph Output

The program generates a file:

nfa_graph.png

Example structure:
(q0) --a--> (q1)  
(q1) --ε--> (q2)  
(q2) --b--> (q4)  
(q1) --ε--> (q3)  
(q3) --c--> (q5)  
(q4) --ε--> (q6) [FINAL]  
(q5) --ε--> (q6)

---

## ⚙️ Tools & Technologies

- Python 3
- graphviz (Python library)
- Graphviz system package

Install:
pip install graphviz

Windows: https://graphviz.org/download/  
Linux: sudo apt install graphviz  
Mac: brew install graphviz  

---

## 🧠 Inside Mechanism

1. Tokenization of regex input  
2. Recursive descent parsing:
   - expr → |
   - concat → concatenation
   - factor → *, +, ?
   - atom → character / ( )
3. Thompson’s Construction builds NFA fragments
4. BFS assigns state IDs
5. Graphviz renders final NFA

---

## 🚀 How to Run

python main.py "a(b|c)*a"

OR

python main.py
regex: a(b|c)*a

---

## 📌 Example Input
a(b|c)*a

---

## 📤 Example Output
Transition table printed in console and image generated:


nfa_graph.png

---

## 📁 Project Structure

Regex-to-NFA/
│
├── main.py
├── README.md
└── nfa_graph.png

---

