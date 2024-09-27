"""BINLT data item."""
from .. import variables
from .base import DataItemBase


class BINLT(DataItemBase):
    """Bin list.

    :Types:
       - :class:`U1 <secsgem.secs.variables.U1>`
       - :class:`String <secsgem.secs.variables.String>`

    **Used In Function**
        - :class:`SecsS12F07 <secsgem.secs.functions.SecsS12F07>`
        - :class:`SecsS12F09 <secsgem.secs.functions.SecsS12F09>`
        - :class:`SecsS12F11 <secsgem.secs.functions.SecsS12F11>`
        - :class:`SecsS12F14 <secsgem.secs.functions.SecsS12F14>`
        - :class:`SecsS12F16 <secsgem.secs.functions.SecsS12F16>`
        - :class:`SecsS12F18 <secsgem.secs.functions.SecsS12F18>`

    """

    __type__ = variables.Dynamic
    __allowedtypes__ = [
        variables.U1,
        variables.String
    ]
