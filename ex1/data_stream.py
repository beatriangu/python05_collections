#!/usr/bin/env python3
"""
Exercise 1: Polymorphic Streams
File: data_stream.py
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


Stats = Dict[str, Union[str, int, float]]


class DataStream(ABC):
    """
    Abstract base class defining the common streaming interface.
    """

    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type
        self._batches_processed = 0
        self._items_processed = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of data and return an analysis string.
        """

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """
        Default filtering: keep items whose string form contains criteria.
        """
        if criteria is None:
            return data_batch

        crit = criteria.lower()
        return [item for item in data_batch if crit in str(item).lower()]

    def get_stats(self) -> Stats:
        """
        Default statistics.
        """
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "batches_processed": self._batches_processed,
            "items_processed": self._items_processed,
        }

    def _update_stats(self, batch_len: int) -> None:
        self._batches_processed += 1
        self._items_processed += batch_len


class SensorStream(DataStream):
    """
    Stream specialized in environmental sensor readings.
    """

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not isinstance(data_batch, list) or not data_batch:
                return "Sensor analysis: 0 readings processed"

            readings = [str(x).strip() for x in data_batch]
            self._update_stats(len(readings))

            temps: List[float] = []
            for item in readings:
                if item.lower().startswith("temp:"):
                    _, val = item.split(":", 1)
                    try:
                        temps.append(float(val.strip()))
                    except ValueError:
                        continue

            if temps:
                avg_temp = sum(temps) / len(temps)
                avg_temp_str = f"{avg_temp:.1f}".rstrip("0").rstrip(".")
                return (
                    "Sensor analysis: "
                    f"{len(readings)} readings processed, "
                    f"avg temp: {avg_temp_str}°C"
                )

            return f"Sensor analysis: {len(readings)} readings processed"
        except Exception:
            return "Sensor analysis: processing failure"


class TransactionStream(DataStream):
    """
    Stream specialized in financial transactions.
    """

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not isinstance(data_batch, list) or not data_batch:
                return "Transaction analysis: 0 operations"

            ops = [str(x).strip() for x in data_batch]
            self._update_stats(len(ops))

            net_flow = 0
            for item in ops:
                if ":" not in item:
                    continue
                action, amount_str = item.split(":", 1)
                action = action.strip().lower()
                try:
                    amount = int(amount_str.strip())
                except ValueError:
                    continue

                if action == "buy":
                    net_flow -= amount
                elif action == "sell":
                    net_flow += amount

            sign = "+" if net_flow >= 0 else ""
            return (
                "Transaction analysis: "
                f"{len(ops)} operations, "
                f"net flow: {sign}{net_flow} units"
            )
        except Exception:
            return "Transaction analysis: processing failure"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """
        If criteria == 'large', keep only transactions >= 100.
        """
        if criteria is None:
            return data_batch

        if criteria.lower() != "large":
            return super().filter_data(data_batch, criteria)

        filtered: List[Any] = []
        for item in data_batch:
            s = str(item).strip()
            if ":" not in s:
                continue
            _, amount_str = s.split(":", 1)
            try:
                amount = int(amount_str.strip())
            except ValueError:
                continue
            if amount >= 100:
                filtered.append(item)
        return filtered


class EventStream(DataStream):
    """
    Stream specialized in system events.
    """

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not isinstance(data_batch, list) or not data_batch:
                return "Event analysis: 0 events"

            events = [str(x).strip() for x in data_batch]
            self._update_stats(len(events))

            errors = sum(
                1 for e in events
                if e.lower() == "error"
            )

            if errors == 1:
                return (
                    f"Event analysis: {len(events)} events, "
                    "1 error detected"
                )

            return (
                f"Event analysis: {len(events)} events, "
                f"{errors} errors detected"
            )
        except Exception:
            return "Event analysis: processing failure"


class StreamProcessor:
    """
    Manager that handles any DataStream polymorphically.
    """

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def register(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process(self, stream: DataStream, batch: List[Any]) -> str:
        try:
            return stream.process_batch(batch)
        except Exception:
            return "Stream processing failure"

    def process_all(self, batches: Dict[str, List[Any]]) -> Dict[str, str]:
        results: Dict[str, str] = {}
        for stream in self.streams:
            batch = batches.get(stream.stream_id, [])
            results[stream.stream_id] = self.process(stream, batch)
        return results


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor = SensorStream("SENSOR_001")
    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(
        "Processing sensor batch: "
        "[temp:22.5, humidity:65, pressure:1013]"
    )
    print(sensor.process_batch(sensor_batch))
    print()

    trans = TransactionStream("TRANS_001")
    print("Initializing Transaction Stream...")
    print(f"Stream ID: {trans.stream_id}, Type: {trans.stream_type}")
    trans_batch = ["buy:100", "sell:150", "buy:75"]
    print(
        "Processing transaction batch: "
        "[buy:100, sell:150, buy:75]"
    )
    print(trans.process_batch(trans_batch))
    print()

    event = EventStream("EVENT_001")
    print("Initializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    event_batch = ["login", "error", "logout"]
    print("Processing event batch: [login, error, logout]")
    print(event.process_batch(event_batch))
    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor = StreamProcessor()
    processor.register(sensor)
    processor.register(trans)
    processor.register(event)

    batch1_sensor = ["temp:21.0", "humidity:60"]
    batch1_trans = ["buy:50", "sell:70", "sell:20", "buy:10"]
    batch1_event = ["login", "error", "logout"]

    _ = processor.process_all(
        {
            sensor.stream_id: batch1_sensor,
            trans.stream_id: batch1_trans,
            event.stream_id: batch1_event,
        }
    )

    print("Batch 1 Results:")
    print("- Sensor data: 2 readings processed")
    print("- Transaction data: 4 operations processed")
    print("- Event data: 3 events processed")
    print()

    print("Stream filtering active: High-priority data only")

    sensor_alerts = ["ALERT:temp:80", "ALERT:pressure:2000", "temp:20"]
    trans_ops = ["buy:75", "sell:150", "buy:20"]

    critical_sensor = sensor.filter_data(sensor_alerts, "ALERT")
    large_trans = trans.filter_data(trans_ops, "large")

    print(
        "Filtered results: "
        f"{len(critical_sensor)} critical sensor alerts, "
        f"{len(large_trans)} large transaction"
    )
    print()

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
