"""Contains SECS I message class."""
from __future__ import annotations

import secsgem.common

from .header import SecsIHeader


class SecsIBlock(secsgem.common.Block[SecsIHeader]):
    """Data block for SECS I."""

    header_type = SecsIHeader
    length_format = "B"
    checksum_format = "H"


class SecsIMessage(secsgem.common.Message[SecsIBlock]):
    """Class for SECS I message.

    Contains all required data and functions.
    """

    block_size = 244
    block_type = SecsIBlock

    @property
    def header(self) -> SecsIHeader:
        """Get the header."""
        return self._blocks[-1].header

    @property
    def data(self) -> bytes:
        """Get the data."""
        return b"".join(block.data for block in self._blocks)

    @property
    def complete(self) -> bool:
        """Check if the message is complete."""
        return self.blocks[-1].header.last_block
