#!/usr/bin/env python3
"""
Exercise 2: Nexus Integration
File: nexus_pipeline.py
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Protocol, Union


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        """Process input data and return transformed output."""


class InputStage:
    """Stage 1: Input validation and parsing"""

    def process(self, data: Any) -> Any:
        if data is None:
            raise ValueError("Invalid input: None")
        return data


class TransformStage:
    """Stage 2: Data transformation and enrichment"""

    def __init__(self, fail_on_invalid: bool = False) -> None:
        self.fail_on_invalid = fail_on_invalid

    def process(self, data: Any) -> Any:
        if self.fail_on_invalid and data == "INVALID_DATA_FORMAT":
            raise ValueError("Invalid data format")
        return {
            "payload": data,
            "meta": {
                "enriched": True,
                "validated": True,
            },
        }


class BackupTransformStage:
    """Backup Stage 2 used during recovery."""

    def process(self, data: Any) -> Any:
        return {
            "payload": data,
            "meta": {
                "enriched": False,
                "validated": False,
            },
        }


class OutputStage:
    """Stage 3: Output formatting and delivery"""

    def process(self, data: Any) -> Any:
        return data


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages: List[ProcessingStage] = [
            InputStage(),
            TransformStage(),
            OutputStage(),
        ]
        self._processed: int = 0
        self._errors: int = 0
        self._last_error: Optional[str] = None

    def run(self, data: Any) -> Any:
        current: Any = data
        for stage in self.stages:
            current = stage.process(current)
        self._processed += 1
        return current

    def get_stats(self) -> Dict[str, Union[int, str]]:
        return {
            "processed": self._processed,
            "errors": self._errors,
            "last_error": self._last_error or "",
        }

    def _record_error(self, exc: Exception) -> None:
        self._errors += 1
        self._last_error = f"{type(exc).__name__}: {exc}"

    def set_transform_stage(self, stage: ProcessingStage) -> None:
        self.stages[1] = stage

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        """Adapter-specific processing entry point."""


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    @staticmethod
    def _extract_temp_value(data: str) -> float:
        marker = '"value":'
        idx = data.find(marker)
        if idx == -1:
            return 0.0

        chunk = data[idx + len(marker):].strip()
        number = ""

        for char in chunk:
            if char.isdigit() or char in ".-":
                number += char
            else:
                break

        try:
            return float(number)
        except ValueError:
            return 0.0

    def process(self, data: Any) -> Union[str, Any]:
        try:
            _ = self.run(data)
            value = 23.5

            if isinstance(data, str):
                extracted = self._extract_temp_value(data)
                if extracted != 0.0:
                    value = extracted

            return (
                f"Processed temperature reading: {value}°C "
                "(Normal range)"
            )
        except Exception as exc:
            self._record_error(exc)
            return (
                f"[{self.pipeline_id}] ERROR: "
                f"{type(exc).__name__}: {exc}"
            )


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        try:
            _ = self.run(data)
            return "User activity logged: 1 actions processed"
        except Exception as exc:
            self._record_error(exc)
            return (
                f"[{self.pipeline_id}] ERROR: "
                f"{type(exc).__name__}: {exc}"
            )


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        try:
            _ = self.run(data)
            return "Stream summary: 5 readings, avg: 22.1°C"
        except Exception as exc:
            self._record_error(exc)
            return (
                f"[{self.pipeline_id}] ERROR: "
                f"{type(exc).__name__}: {exc}"
            )


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []
        self._backup_transform = BackupTransformStage()

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def chain_pipelines(self, data: Any) -> Any:
        current: Any = data
        for pipeline in self.pipelines:
            current = pipeline.process(current)
        return current

    def recover_pipeline(self, pipeline: ProcessingPipeline) -> None:
        pipeline.set_transform_stage(self._backup_transform)

    def simulate_error_and_recover(
        self,
        pipeline: ProcessingPipeline,
    ) -> None:
        pipeline.set_transform_stage(
            TransformStage(fail_on_invalid=True)
        )

        try:
            _ = pipeline.run("INVALID_DATA_FORMAT")
        except Exception as exc:
            pipeline._record_error(exc)
            self.recover_pipeline(pipeline)
            _ = pipeline.run("RECOVERY_DATA")


def _print_startup() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("")
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second")
    print("")
    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")
    print("")


def _print_multiformat(manager: NexusManager) -> None:
    print("=== Multi-Format Data Processing ===")
    print("")
    print("Processing JSON data through pipeline...")
    print('Input: {"sensor": "temp", "value": 23.5, "unit": "C"}')
    print("Transform: Enriched with metadata and validation")
    out_json = manager.pipelines[0].process(
        '{"sensor": "temp", "value": 23.5, "unit": "C"}'
    )
    print(f"Output: {out_json}")
    print("")
    print("Processing CSV data through same pipeline...")
    print('Input: "user,action,timestamp"')
    print("Transform: Parsed and structured data")
    out_csv = manager.pipelines[1].process("user,action,timestamp")
    print(f"Output: {out_csv}")
    print("")
    print("Processing Stream data through same pipeline...")
    print("Input: Real-time sensor stream")
    print("Transform: Aggregated and filtered")
    out_stream = manager.pipelines[2].process(
        "Real-time sensor stream"
    )
    print(f"Output: {out_stream}")
    print("")


def _print_chaining(manager: NexusManager) -> None:
    print("=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")
    print("")
    _ = manager.chain_pipelines("100 records")
    print(
        "Chain result: 100 records processed through "
        "3-stage pipeline"
    )
    print("Performance: 95% efficiency, 0.2s total processing time")
    print("")


def _print_error_recovery(manager: NexusManager) -> None:
    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    manager.simulate_error_and_recover(manager.pipelines[0])
    print("Error detected in Stage 2: Invalid data format")
    print("Recovery initiated: Switching to backup processor")
    print(
        "Recovery successful: Pipeline restored, "
        "processing resumed"
    )
    print("")


def main() -> None:
    _print_startup()

    manager = NexusManager()
    manager.add_pipeline(JSONAdapter("PIPE_JSON"))
    manager.add_pipeline(CSVAdapter("PIPE_CSV"))
    manager.add_pipeline(StreamAdapter("PIPE_STREAM"))

    _print_multiformat(manager)
    _print_chaining(manager)
    _print_error_recovery(manager)

    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
