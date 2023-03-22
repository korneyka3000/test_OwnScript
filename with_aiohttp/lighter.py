import logging

from .colors import Colors
from .commands import CommandsInterface
from .server_connection import ConnectServer


class Lighter(ConnectServer, CommandsInterface):
    """Класс фонаря"""

    def __init__(self) -> None:
        CommandsInterface.__init__(self)
        self.__is_on = False
        self._color_options = Colors
        self._current_color = Colors.get_default_color()

    @property
    def supported_commands(self) -> dict:
        return self._supported_commands

    @supported_commands.setter
    def supported_commands(self, value):
        raise PermissionError(
            "Its impossible to add new commands to Lighter in this way"
        )

    @supported_commands.deleter
    def supported_commands(self):
        raise PermissionError("Its impossible to delete commands")

    @property
    def is_on(self):
        return self._Lighter__is_on

    @is_on.setter
    def is_on(self, value):
        raise PermissionError(
            "Its impossible to change state of Lighter, use methods(ON/OFF) instead"
        )

    @is_on.deleter
    def is_on(self):
        raise PermissionError("Its impossible to delete attribute")

    @property
    def current_color(self):
        return self._current_color

    @current_color.setter
    def current_color(self, value: str | None):
        if value:
            if color_to_set := self._color_options.members_dict().get(value):
                self._current_color = color_to_set.value
            else:
                logging.warning(f' Color "{value}" is not in the options')

    async def COLOR(self, metadata=None):
        if metadata:
            if metadata == self.current_color:
                return f"color is already {metadata}"
            else:
                self.current_color = metadata
                return f"color has been changed to {metadata}"
        index = self._color_options.members_list().index(self.current_color)
        if index >= (len(self._color_options.members_list()) - 1):
            self.current_color = self._color_options.get_default_color()
        else:
            self.current_color = self._color_options.members_list()[index + 1]
        return f"color has been changed to {self.current_color}"

    async def ON(self, metadata=None):
        """Turns ON the lighter"""
        if self.is_on is True:
            logging.warning("Lighter is already ON")
        self.__is_on = True
        return "lighter is on"

    async def OFF(self, metadata=None):
        """Turns OFF the lighter"""
        if self.is_on is False:
            logging.warning("Lighter is already OFF")
        self.__is_on = False
        return "lighter is off"

    async def command_executor(self, json_data: dict) -> str | None:
        """Checks if given command exists and execute it else do nothing"""
        metadata = json_data.get("metadata")
        if command := json_data.get("command"):
            if command in self.supported_commands:
                if command_to_execute := self.supported_commands.get(command):
                    result = await command_to_execute(metadata=metadata)
                    return result
