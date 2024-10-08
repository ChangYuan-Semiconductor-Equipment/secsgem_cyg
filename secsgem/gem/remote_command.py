"""Wrapper for GEM remote command."""
from __future__ import annotations

import enum
import typing

from secsgem.secs.variables import U4, Base, String

if typing.TYPE_CHECKING:
    from .collection_event import CollectionEventId


class RemoteCommandId(enum.Enum):
    """Default IDs for remote commands."""
    START = "START"
    STOP = "STOP"

class RemoteCommand:  # pylint: disable=too-few-public-methods
    """Remote command definition."""

    def __init__(self,
                 rcmd: int | str | RemoteCommandId,
                 name: str,
                 params: list[str],
                 ce_finished: int | str | CollectionEventId,
                 **kwargs):
        """Initialize a remote command.

        You can manually set the secs-type of the id with the 'id_type' keyword argument.

        Custom parameters can be set with the keyword arguments,
        they will be passed to the GemEquipmentHandlers callback
        :func:`secsgem.gem.equipmenthandler.GemEquipmentHandler._on_rcmd_<remote_command>`.

        :param rcmd: ID of the status variable
        :type rcmd: various
        :param name: long name of the status variable
        :type name: string
        :param params: array of available parameter names
        :type params: list
        :param ce_finished: collection event to trigger when remote command was finished
        :type ce_finished: types supported by data item CEID
        """
        self.rcmd = rcmd
        self.name = name
        self.params = params
        self.ce_finished = ce_finished

        self.id_type: type[Base]

        if isinstance(self.rcmd, int):
            self.id_type = U4
        else:
            self.id_type = String

        for key, value in kwargs.items():
            setattr(self, key, value)
