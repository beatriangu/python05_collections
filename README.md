# 📦 Code Nexus — Polymorphic Data Processing
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![OOP](https://img.shields.io/badge/OOP-Object%20Oriented-success)
![Polymorphism](https://img.shields.io/badge/Concept-Polymorphism-orange)
![Status](https://img.shields.io/badge/Status-Learning%20Project-lightgrey)



A progressive Python project that demonstrates polymorphism in practice using
Abstract Base Classes, method overriding, and pipeline architecture.

The system evolves from single data processors, to batch streams, and finally to a
recoverable, chained processing pipeline.

🧠 Core Idea

Same interface, different behavior — without conditionals.

🏗️ Visual Architecture Overview
🔹 ex0 — Polymorphic Processors (single item)
            DataProcessor (ABC)
          ┌──────────┴──────────┐
      process(data)        validate(data)
                ▲
   ┌────────────┼───────────────┐
   │            │               │
NumericProcessor  TextProcessor   LogProcessor


✔ Same method call

✔ Different internal behavior

✔ No if, no type checks

🔹 ex1 — Polymorphic Streams (batch processing)
              DataStream (ABC)
               process_batch()
                     ▲
     ┌───────────────┼────────────────┐
     │               │                │
 SensorStream   TransactionStream   EventStream
     └───────────────┴────────────────┘
            StreamProcessor
        (polymorphic manager)


✔ Batch processing

✔ Filtering & statistics

✔ Manager depends on the interface, not the implementation

🔹 ex2 — Nexus Pipeline Integration (enterprise level)
            ProcessingStage (Protocol)
                   process()
                      ▲
      ┌───────────────┼───────────────────┐
      │               │                   │
  InputStage     TransformStage       OutputStage
                      │
              BackupTransformStage
                (used on failure)

            ProcessingPipeline (ABC)
        ┌───────────────┴────────────────┐
        │   stages + run() + stats        │
        │   abstract process()            │
        └───────────────▲────────────────┘
                        │ override
     ┌──────────────────┼──────────────────┐
     │                  │                  │
 JSONAdapter        CSVAdapter        StreamAdapter

                 NexusManager
     (chaining + recovery + orchestration)


✔ Pipeline chaining (A → B → C)

✔ Real error handling & recovery

✔ Duck typing for flexible stages

📁 Project Structure
.
├── ex0/  # Single-item processors
├── ex1/  # Batch streams
├── ex2/  # Pipeline integration & recovery
└── README.md

▶️ How to Run
python3 ex0/stream_processor.py
python3 ex1/data_stream.py
python3 ex2/nexus_pipeline.py

🧩 Concepts Demonstrated

Abstract Base Classes (ABC)

Abstract Methods (@abstractmethod)

Inheritance & Method Overriding

Subtype Polymorphism

Duck Typing (Protocol)

Batch Processing

Error Handling & Recovery

Separation of Concerns

✨ Why This Project Matters

Add new processors, streams, or pipelines without modifying existing code

Scale from simple logic to complex systems naturally

Apply clean, extensible architecture aligned with real-world backend design

🎯 One-Line Summary (Defense-Ready)

A scalable polymorphic data processing system built with abstract base classes, method overriding, duck typing, and pipeline orchestration in Python.

