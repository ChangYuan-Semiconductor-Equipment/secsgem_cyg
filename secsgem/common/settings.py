"""settings base class."""
from __future__ import annotations

import abc
import enum
import typing

from .timeouts import Timeouts

if typing.TYPE_CHECKING:
    from secsgem.secs.functions import StreamsFunctions

    from .connection import Connection
    from .protocol import Protocol


class DeviceType(enum.Enum):
    """Type of device (equipment or host)."""

    # This device is equipment
    EQUIPMENT = 0

    # This device is host.
    HOST = 1


class Settings(abc.ABC):
    r"""Settings base class.

    These attributes can be initialized in the constructor and accessed as property.

    """

    def __init__(self, **kwargs) -> None:
        """Initialize settings."""
        from secsgem.secs.functions import StreamsFunctions  # pylint: disable=import-outside-toplevel

        self._timeouts = Timeouts(**kwargs)
        self._device_type = kwargs.get("device_type", DeviceType.HOST)
        self._streams_functions = kwargs.get("streams_functions", StreamsFunctions())
        self._session_id = kwargs.get("session_id", 0)
        self._establish_communication_timeout = kwargs.get("establish_communication_timeout", 10)

    @property
    def address(self):
        raise NotImplementedError("针对hsms需要继承实现这个函数.")

    @property
    def port(self):
        raise NotImplementedError("针对hsms需要继承实现这个函数.")

    @property
    def timeouts(self) -> Timeouts:
        """Communication timeouts."""
        return self._timeouts

    @property
    def device_type(self) -> DeviceType:
        """Device type.

        Default: DeviceType.HOST.
        """
        return self._device_type

    @property
    def streams_functions(self) -> StreamsFunctions:
        """Container with streams/functions.

        Default: DeviceType.HOST.
        """
        return self._streams_functions

    @property
    def session_id(self) -> int:
        """Session / device ID to use for connection.

        Default: 0
        """
        return self._session_id

    @property
    def establish_communication_timeout(self) -> int:
        """Time to wait between CA requests.

        Default: 10
        """
        return self._establish_communication_timeout

    @establish_communication_timeout.setter
    def establish_communication_timeout(self, value: int) -> None:
        """Set time to wait between CA requests."""
        self._establish_communication_timeout = value

    @abc.abstractmethod
    def create_protocol(self) -> Protocol:
        """Protocol class for this configuration."""
        raise NotImplementedError(f"function 'create_protocol' is not implemented for '{self.__class__.__name__}'")

    @abc.abstractmethod
    def create_connection(self) -> Connection:
        """Connection class for this configuration."""
        raise NotImplementedError(f"function 'create_connection' is not implemented for '{self.__class__.__name__}'")

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Name of this configuration."""
        raise NotImplementedError(f"property 'name' is not implemented for '{self.__class__.__name__}'")

    @abc.abstractmethod
    def generate_thread_name(self, functionality: str) -> str:
        """Generate a unique thread name for this configuration and a provided functionality.

        Args:
            functionality: name of the functionality to generate thread name for

        Returns:
            generated thread name

        """
        raise NotImplementedError(f"function 'generate_thread_name' is not implemented for '{self.__class__.__name__}'")
