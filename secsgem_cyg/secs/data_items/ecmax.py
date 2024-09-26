"""ECMAX data item."""
from .. import variables
from .base import DataItemBase


class ECMAX(DataItemBase):
    """Equipment constant maximum value.

    :Types:
       - :class:`Boolean <secsgem_cyg.secs.variables.Boolean>`
       - :class:`I8 <secsgem_cyg.secs.variables.I8>`
       - :class:`I1 <secsgem_cyg.secs.variables.I1>`
       - :class:`I2 <secsgem_cyg.secs.variables.I2>`
       - :class:`I4 <secsgem_cyg.secs.variables.I4>`
       - :class:`F8 <secsgem_cyg.secs.variables.F8>`
       - :class:`F4 <secsgem_cyg.secs.variables.F4>`
       - :class:`U8 <secsgem_cyg.secs.variables.U8>`
       - :class:`U1 <secsgem_cyg.secs.variables.U1>`
       - :class:`U2 <secsgem_cyg.secs.variables.U2>`
       - :class:`U4 <secsgem_cyg.secs.variables.U4>`
       - :class:`String <secsgem_cyg.secs.variables.String>`
       - :class:`Binary <secsgem_cyg.secs.variables.Binary>`

    **Used In Function**
        - :class:`SecsS02F30 <secsgem_cyg.secs.functions.SecsS02F30>`

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
