import inspect
from abc import ABC, abstractmethod


class CommandsInterface(ABC):
    """Команды фонаря"""
    def __init__(self) -> None:
        commands: dict = dict(inspect.getmembers(self, inspect.ismethod))
        commands.pop("__init__")
        commands.pop("command_executor")
        self._supported_commands = commands

    @abstractmethod
    async def ON(self, metadata):
        pass

    @abstractmethod
    async def OFF(self, metadata):
        pass

    @abstractmethod
    async def COLOR(self, metadata):
        pass
