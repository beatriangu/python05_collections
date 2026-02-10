🧭 MAP.md — Code Nexus · Polymorphic Data Processing
Python Module 05 · Polimorfismo, ABCs y Arquitectura de Pipelines

Este documento es mi mapa de aprendizaje y diseño.
No describe ejercicios sueltos: explica la evolución de una arquitectura.

Sirve para:

entender el módulo en profundidad,

justificar decisiones técnicas,

y demostrar pensamiento de diseño orientado a sistemas.

🌱 IDEA CENTRAL DEL MÓDULO

Pasar de:

❌ “si el dato es X hago A, si es Y hago B”
a
✅ “trato todos los datos igual; el comportamiento lo decide el objeto”

Misma interfaz, comportamientos distintos, sin condicionales.

El polimorfismo permite:

eliminar if / elif / isinstance,

desacoplar el sistema,

y escalar sin reescribir el core.

🧠 VISIÓN GLOBAL DEL RECORRIDO

El módulo progresa de forma incremental:

ex0 → procesar un dato
ex1 → procesar lotes (streams)
ex2 → orquestar pipelines completos y recuperables


No es un módulo de “colecciones”.
Es un módulo de pensamiento arquitectónico con Python.

🟢 ex0 — Polymorphic Processors (single item)
🎯 FOCO

Polimorfismo en su forma más pura.

📐 Arquitectura mental
DataProcessor (ABC)
 ├── process(data)
 ├── validate(data)
 └── format_output(result)

NumericProcessor
TextProcessor
LogProcessor

🧠 CONCEPTOS CLAVE

Abstract Base Classes (ABC)

@abstractmethod

Herencia

Subtype polymorphism

Method overriding

🧩 CLAVE MENTAL

👉 El código cliente no conoce la clase concreta.
👉 Solo confía en el contrato.

✔️ Mismo método
✔️ Distinta lógica
✔️ Cero condicionales

🔗 Prepara para → batch processing y managers polimórficos

🟢 ex1 — Polymorphic Streams (batch processing)
🎯 FOCO

Aplicar polimorfismo a colecciones de datos.

📐 Arquitectura mental
DataStream (ABC)
 ├── process_batch(data_batch)
 ├── filter_data()
 └── get_stats()

SensorStream
TransactionStream
EventStream

StreamProcessor
 └── opera solo contra DataStream

🧠 CONCEPTOS CLAVE

Polimorfismo a nivel batch

Diseño orientado a interfaces

Separación entre:

procesamiento

gestión

estadísticas

🧩 CLAVE MENTAL

👉 El manager no sabe qué stream procesa.
👉 Sabe qué interfaz cumple.

🔗 Depende de → ex0
🔗 Prepara para → pipelines y sistemas reales

🟢 ex2 — Nexus Pipeline Integration (enterprise level)
🎯 FOCO

Arquitectura real, extensible y resiliente.

📐 Arquitectura mental
ProcessingPipeline (ABC)
 ├── run()
 └── process()  ← override por adapter

JSONAdapter
CSVAdapter
StreamAdapter

Duck typing con Protocol
ProcessingStage (Protocol)
 └── process()

InputStage
TransformStage
OutputStage
BackupTransformStage

NexusManager
 ├── encadena pipelines
 ├── monitoriza ejecución
 └── gestiona recuperación

🧠 CONCEPTOS CLAVE

Duck typing (Protocol)

Polimorfismo por comportamiento (no herencia)

Encadenamiento de pipelines

Separación de etapas

Recovery real ante fallos

🧩 CLAVE FINAL

👉 No importa qué clase eres.
👉 Importa qué método ofreces.

El sistema:

fluye,

se recupera,

continúa.

🔁 EVOLUCIÓN DEL POLIMORFISMO
Nivel	Técnica	Ejercicio
Básico	Herencia + override	ex0
Batch	Interfaces + managers	ex1
Avanzado	Duck typing + pipelines	ex2
🧩 DECISIONES DE DISEÑO (CON INTENCIÓN)

ABC cuando el contrato debe ser fuerte

Protocol cuando solo importa el comportamiento

Managers que dependen de interfaces, no implementaciones

Sin prints en lógica → solo retornos

main() como orquestador

Extensibilidad > condicionales



🧠 MAPA GLOBAL
dato → processor → stream → pipeline → sistema


Cada paso añade escala, no complejidad accidental.


El módulo progresa desde el procesamiento de datos individuales hasta la orquestación de pipelines completos, utilizando clases abstractas, method overriding y polimorfismo —tanto por herencia como por duck typing— para construir sistemas extensibles, mantenibles y robustos sin condicionales por tipo.
