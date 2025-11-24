"""
model package
-------------
Exposes LegalPipeline and Translator for easy importing.
"""

from .pipeline import LegalPipeline
from .translator import Translator

__all__ = ["LegalPipeline", "Translator"]
