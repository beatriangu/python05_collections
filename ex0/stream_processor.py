#!/usr/bin/env python3
"""
Module: Code Nexus - Data Processor Foundation
Exercise: 0 - stream_processor

Description:
Build a polymorphic data processing system using method overriding.
A base abstract DataProcessor defines a common interface, and
specialized processors implement type-specific behavior.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """
    Abstract base processor defining the common processing interface.
    """

    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Process data and return a result string.
        """

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validate if data is appropriate for this processor.
        """

    def format_output(self, result: str) -> str:
        """
        Default output formatting. Subclasses may override.
        """
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """
    Processor specialized in numeric collections (list/tuple of int/float).
    """

    def validate(self, data: Any) -> bool:
        if not isinstance(data, (list, tuple)):
            return False
        if len(data) == 0:
            return False
        return all(isinstance(x, (int, float)) for x in data)

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                return self.format_output("Error: invalid numeric data")

            values = list(data)
            total = sum(values)
            avg = total / len(values)
            return self.format_output(
                f"Processed {len(values)} numeric values, "
                f"sum={total}, avg={avg}"
            )
        except Exception as exc:
            return self.format_output(
                f"Error: processing failure ({exc})"
            )


class TextProcessor(DataProcessor):
    """
    Processor specialized in text strings.
    """

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and len(data) > 0

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                return self.format_output("Error: invalid text data")

            chars = len(data)
            words = len(data.split())
            return self.format_output(
                f"Processed text: {chars} characters, "
                f"{words} words"
            )
        except Exception as exc:
            return self.format_output(
                f"Error: processing failure ({exc})"
            )


class LogProcessor(DataProcessor):
    """
    Processor specialized in log entries, detecting levels like
    INFO/WARNING/ERROR.
    """

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def format_output(self, result: str) -> str:
        """
        Override default formatting to emphasize log alerts.
        """
        return result

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                return self.format_output("Error: invalid log entry")

            raw = data.strip()
            level, message = raw.split(":", 1)
            level = level.strip().upper()
            message = message.strip()

            if level == "ERROR":
                tag = "[ALERT]"
            elif level == "WARNING":
                tag = "[WARN]"
            else:
                tag = "[INFO]"

            return self.format_output(
                f"{tag} {level} level detected: {message}"
            )
        except ValueError:
            return self.format_output(
                "Error: log entry format must be 'LEVEL: message'"
            )
        except Exception as exc:
            return self.format_output(
                f"Error: processing failure ({exc})"
            )


def _print_validation(label: str, ok: bool) -> None:
    status = "verified" if ok else "Failed"
    print(f"Validation: {label} data {status}")
