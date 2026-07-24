from dataclasses import dataclass, field
from typing import Any

@dataclass
class Post:
    id: str
    source: str

    title: str
    url: str

    body: str = ""

    images: list[str] = field(default_factory=list)
    thumbnail: str = ""

    author: str = ""
    timestamp: str = ""

    metadata: dict[str, Any] = field(default_factory=dict)
