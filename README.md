# 📦 Code Nexus — Polymorphic Data Processing (Python)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![OOP](https://img.shields.io/badge/OOP-Object%20Oriented-success)
![Polymorphism](https://img.shields.io/badge/Concept-Polymorphism-orange)
![Status](https://img.shields.io/badge/Status-Learning%20Project-lightgrey)

A progressive Python project that demonstrates **polymorphism in practice** using  
**Abstract Base Classes**, **method overriding**, **duck typing**, and **pipeline architecture**.

The system evolves step by step:
from single-item processors,  
to batch data streams,  
and finally to a **recoverable, chained data processing pipeline** inspired by real-world backend systems.

---

## 🧠 Core Idea
> **Same interface, different behavior — without conditionals.**

---

## 🏗️ Visual Architecture Overview

### 🔹 ex0 — Polymorphic Processors (single item)

**DataProcessor (ABC)**  
├── `process(data)`  
├── `validate(data)`  
└── `format_output(result)`

**Specialized processors**
- `NumericProcessor`
- `TextProcessor`
- `LogProcessor`

✔ Same method call  
✔ Different internal behavior  
✔ No `if`, no type checks  

---

### 🔹 ex1 — Polymorphic Streams (batch processing)

**DataStream (ABC)**  
├── `process_batch()`  
├── `filter_data()`  
└── `get_stats()`

**Specialized streams**
- `SensorStream`
- `TransactionStream`
- `EventStream`

**StreamProcessor**
- Manages multiple streams polymorphically
- Depends on the interface, not the implementation

✔ Batch processing  
✔ Filtering & statistics  
✔ Interface-driven design  

---

### 🔹 ex2 — Nexus Pipeline Integration (enterprise level)

**ProcessingStage (Protocol / duck typing)**  
- Any class with `process()` can act as a stage

**Stages**
- `InputStage`
- `TransformStage`
- `OutputStage`
- `BackupTransformStage` (used on failure)

**ProcessingPipeline (ABC)**
- Manages stages
- Orchestrates data flow
- Tracks statistics

**Adapters (override `process()`)**
- `JSONAdapter`
- `CSVAdapter`
- `StreamAdapter`

**NexusManager**
- Orchestrates multiple pipelines
- Handles chaining, recovery, and monitoring

✔ Pipeline chaining (A → B → C)  
✔ Real error handling & recovery  
✔ Duck typing for flexible stages  

---

## 📁 Project Structure

```text
.
├── ex0/  # Single-item processors (foundations)
├── ex1/  # Batch streams & polymorphic stream manager
├── ex2/  # Enterprise pipeline integration & recovery
└── README.md
▶️ How to Run
python3 ex0/stream_processor.py
python3 ex1/data_stream.py
python3 ex2/nexus_pipeline.py
Each script runs independently and demonstrates the concepts of its exercise.

🧩 Concepts Demonstrated
Abstract Base Classes (ABC)

Abstract Methods (@abstractmethod)

Inheritance & Method Overriding

Subtype Polymorphism

Duck Typing (Protocol)

Batch Processing

Error Handling & Recovery

Separation of Concerns

Interface-based Design

✨ Why This Project Matters
New processors, streams, or pipelines can be added without modifying existing code

The architecture scales naturally from simple logic to complex systems

Demonstrates clean, extensible design aligned with real-world backend and data engineering practices

Focuses on clarity, maintainability, and explainability, not clever tricks

🎯 One-Line Summary (Defense-Ready)
A scalable polymorphic data processing system built in Python using abstract base classes, method overriding, duck typing, and pipeline orchestration.



