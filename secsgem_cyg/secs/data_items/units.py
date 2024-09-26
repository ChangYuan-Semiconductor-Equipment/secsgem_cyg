"""UNITS data item."""
from .. import variables
from .base import DataItemBase


class UNITS(DataItemBase):
    """Units identifier.

    :Type: :class:`String <secsgem_cyg.secs.variables.String>`

    **Used In Function**
        - :class:`SecsS01F12 <secsgem_cyg.secs.functions.SecsS01F12>`
        - :class:`SecsS01F22 <secsgem_cyg.secs.functions.SecsS01F22>`
        - :class:`SecsS02F30 <secsgem_cyg.secs.functions.SecsS02F30>`
        - :class:`SecsS02F48 <secsgem_cyg.secs.functions.SecsS02F48>`

    """

    __type__ = variables.String
