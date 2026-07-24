from abc import ABC, abstractmethod
from typing import List

from bot.models.post import Post


class BaseModule(ABC):
    @abstractmethod
    def fetch(self) -> List[Post]:
        """Fetch posts from the source."""
        pass
