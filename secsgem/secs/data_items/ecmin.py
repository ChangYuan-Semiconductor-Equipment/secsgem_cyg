"""ECMIN data item."""
from .. import variables
from .base import DataItemBase


class ECMIN(DataItemBase):
    """Equipment constant minimum value.

    :Types:
       - :class:`Boolean <secsgem.secs.variables.Boolean>`
       - :class:`I8 <secsgem.secs.variables.I8>`
       - :class:`I1 <secsgem.secs.variables.I1>`
       - :class:`I2 <secsgem.secs.variables.I2>`
       - :class:`I4 <secsgem.secs.variables.I4>`
       - :class:`F8 <secsgem.secs.variables.F8>`
       - :class:`F4 <secsgem.secs.variables.F4>`
       - :class:`U8 <secsgem.secs.variables.U8>`
       - :class:`U1 <secsgem.secs.variables.U1>`
       - :class:`U2 <secsgem.secs.variables.U2>`
       - :class:`U4 <secsgem.secs.variables.U4>`
       - :class:`String <secsgem.secs.variables.String>`
       - :class:`Binary <secsgem.secs.variables.Binary>`

    **Used In Function**
        - :class:`SecsS02F30 <secsgem.secs.functions.SecsS02F30>`

    """

    __type__ = variables.Dynamic
    __allowedtypes__ = [
        variables.Boolean,
        variables.I8,
        variables.I1,
        variables.I2,
        variables.I4,
        variables.F8,
        variables.F4,
        variables.U8,
        variables.U1,
        variables.U2,
        variables.U4,
        variables.String,
        variables.Binary
    ]
