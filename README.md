📦 Data Processor Foundation
Python Module 0X – Polymorphism & Abstract Base Classes

This project implements a data processing system using
Object-Oriented Programming, Abstract Base Classes, and Polymorphism in Python.

The goal is to demonstrate how different types of data can be processed through a common interface, while keeping a clean and extensible design.

🚀 Features

Use of an abstract base class (DataProcessor, DataStream)

Multiple specialized processors and streams:

NumericProcessor

TextProcessor

LogProcessor

SensorStream

TransactionStream

EventStream

Type-specific data validation

Batch processing with filtering and statistics

Polymorphic processing through a shared interface

Clear separation between:

business logic

output presentation

🧠 Concepts Applied

Abstract Base Classes (ABC)

Abstract Methods (@abstractmethod)

Inheritance

Polymorphism

Common Interface

Separation of Concerns

Error Handling

Batch Processing

🏗️ Project Structure
.
├── ex0/
│   └── stream_processor.py
├── ex1/
│   └── data_stream.py
└── README.md

⚙️ How It Works
🔹 Exercise 0 — Single Data Processing
1️⃣ Abstract Base Class
class DataProcessor(ABC):
    @abstractmethod
    def process(self, data):
        pass

    @abstractmethod
    def validate(self, data):
        pass


Defines a common contract that all subclasses must follow.

2️⃣ Specialized Subclasses

Each subclass implements its own logic:

NumericProcessor → processes numeric collections

TextProcessor → processes text strings

LogProcessor → processes log entries

All share the same interface:

process(data)
validate(data)

3️⃣ Two Execution Modes

🟢 Individual Processing

demo_single_processors()


Used to test each processor independently.

🔵 Polymorphic Processing

demo_polymorphism()


Treats all processors as DataProcessor objects,
demonstrating true polymorphism:

for proc, item in zip(processors, inputs):
    result = proc.process(item)
    print(result)

🔹 Exercise 1 — Batch Stream Processing

In this exercise, the system is extended to support data streams and batch processing.

1️⃣ Abstract Stream Class
class DataStream(ABC):
    @abstractmethod
    def process_batch(self, data_batch):
        pass

2️⃣ Specialized Streams

SensorStream → environmental data

TransactionStream → financial data

EventStream → system events

Each stream processes a batch of data and returns an analysis string.

3️⃣ Stream Manager

A StreamProcessor class manages and processes different streams polymorphically:

processor.register(stream)
processor.process(stream, batch)


This demonstrates polymorphism at a higher abstraction level.

▶️ How to Run
Exercise 0
python3 ex0/stream_processor.py

Exercise 1
python3 ex1/data_stream.py

📤 Example Output (Exercise 0)
=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===

Initializing Numeric Processor...
Output: Processed 5 numeric values, sum=15, avg=3.0

Initializing Text Processor...
Output: Processed text: 17 characters, 3 words

Initializing Log Processor...
Output: [ALERT] ERROR level detected: Connection timeout

=== Polymorphic Processing Demo ===
Result 1: Output: Processed 3 numeric values, sum=6, avg=2.0
Result 2: Output: Processed text: 12 characters, 2 words
Result 3: [INFO] INFO level detected: System ready

🗺️ Visual Design
                DataProcessor (abstract)
                 ├── process(data)
                 └── validate(data)
                        ▲
        ┌───────────────┼────────────────┐
        │               │                │
NumericProcessor   TextProcessor   LogProcessor
(process numbers) (process text)  (process logs)

                same interface
                (polymorphism)

                DataStream (abstract)
                 └── process_batch(data)
                        ▲
        ┌───────────────┼────────────────┐
        │               │                │
   SensorStream   TransactionStream   EventStream
        │               │                │
        └───────────────┴────────────────┘
               StreamProcessor
          (polymorphic manager)

🔁 Things to Revisit

Difference between:

abstract class

interface

standard inheritance

When to override a base class method

Alternative polymorphism strategies in Python (duck typing)

Best practices for separating logic from output (print)

Scaling from single-item processing to batch streams

📚 Learning Goals

Understand how polymorphism works in Python

Learn how to use abstract base classes correctly

Design extensible systems without modifying existing code

Write cleaner and more maintainable object-oriented code

Apply polymorphism to both single-item and batch processing

✨ This project is part of the Python Module 0X learning path and serves as a foundation for more advanced object-oriented design exercises.

