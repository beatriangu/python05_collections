📦 Code Nexus — Polymorphic Data Processing (Python)








This repository is part of a personal Python learning journey focused on clarity, mental models, and explainable code.

Code Nexus is a progressive Python project that demonstrates polymorphism in practice using:

Abstract Base Classes (ABC)

Method overriding

Duck typing (Protocol)

Pipeline-oriented architecture

The system evolves step by step:
from single-item processors,
to batch data streams,
and finally to recoverable, chained data processing pipelines, inspired by real-world backend and data engineering systems.

🧠 Core Idea

Same interface, different behavior — without conditionals.

This module shows how polymorphism:

removes if / elif / isinstance,

decouples systems,

and enables scalable, extensible architectures.

🏗️ Architecture Overview
🔹 ex0 — Polymorphic Processors (single item)

Abstract contract

DataProcessor (ABC)
 ├── process(data)
 ├── validate(data)
 └── format_output(result)


Concrete implementations

NumericProcessor

TextProcessor

LogProcessor

✔ Same method call
✔ Different internal behavior
✔ No type checks, no conditionals

📌 Focus: subtype polymorphism and strong contracts.

🔹 ex1 — Polymorphic Streams (batch processing)

Abstract stream interface

DataStream (ABC)
 ├── process_batch()
 ├── filter_data()
 └── get_stats()


Specialized streams

SensorStream

TransactionStream

EventStream

StreamProcessor

Operates polymorphically over multiple streams

Depends only on the interface, not the implementation

✔ Batch processing
✔ Filtering and aggregation
✔ Interface-driven design

📌 Focus: applying polymorphism to collections and batch workflows.

🔹 ex2 — Nexus Pipeline Integration (enterprise level)

Duck typing via Protocol

Any class exposing process() can act as a pipeline stage.

Stages

InputStage

TransformStage

OutputStage

BackupTransformStage (used on failure)

ProcessingPipeline (ABC)

Orchestrates stages

Manages data flow

Tracks execution statistics

Adapters (override process())

JSONAdapter

CSVAdapter

StreamAdapter

NexusManager

Orchestrates multiple pipelines

Handles chaining, monitoring, and recovery

✔ Pipeline chaining (A → B → C)
✔ Real error handling and fallback strategies
✔ Flexible stage composition through duck typing

📌 Focus: architecture, extensibility, and resilience.

📁 Project Structure
.
├── ex0/  # Single-item processors (foundations)
├── ex1/  # Batch streams & polymorphic stream manager
├── ex2/  # Pipeline orchestration, adapters & recovery
├── MAP.md
└── README.md

▶️ How to Run

From the repository root:

python3 ex0/stream_processor.py
python3 ex1/data_stream.py
python3 ex2/nexus_pipeline.py


Each script runs independently and demonstrates the concepts of its exercise.

🧩 Concepts Demonstrated

Abstract Base Classes (ABC)

Abstract methods (@abstractmethod)

Inheritance and method overriding

Subtype polymorphism

Duck typing (Protocol)

Batch processing

Pipeline orchestration

Error handling and recovery

Separation of concerns

Interface-based design

✨ Why This Project Matters

New processors, streams, or pipelines can be added without modifying existing code

The architecture scales naturally from simple logic to complex systems

Demonstrates clean, extensible design aligned with real-world backend and data engineering practices

Prioritizes clarity, maintainability, and explainability over clever tricks

This module represents a transition from writing Python code to designing Python systems.

🎯 One-Line Summary 

A scalable polymorphic data processing system built in Python using abstract base classes, method overriding, duck typing, and pipeline orchestration to eliminate conditionals and enable extensible, resilient architectures.

