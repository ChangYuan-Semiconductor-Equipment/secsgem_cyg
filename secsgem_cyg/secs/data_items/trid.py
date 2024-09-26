"""TRID data item."""
from .. import variables
from .base import DataItemBase


class TRID(DataItemBase):
    """Trace request ID.

    :Types:
       - :class:`I1 <secsgem_cyg.secs.variables.I1>`
       - :class:`I2 <secsgem_cyg.secs.variables.I2>`
       - :class:`I4 <secsgem_cyg.secs.variables.I4>`
       - :class:`I8 <secsgem_cyg.secs.variables.I8>`
       - :class:`U1 <secsgem_cyg.secs.variables.U1>`
       - :class:`U2 <secsgem_cyg.secs.variables.U2>`
       - :class:`U4 <secsgem_cyg.secs.variables.U4>`
       - :class:`U8 <secsgem_cyg.secs.variables.U8>`
       - :class:`String <secsgem_cyg.secs.variables.String>`

    **Used In Function**
        - :class:`SecsS02F23 <secsgem_cyg.secs.functions.SecsS02F23>`
        - :class:`SecsS06F01 <secsgem_cyg.secs.functions.SecsS06F01>`

    """

    __type__ = variables.Dynamic
    __allowedtypes__ = [
        variables.I1,
        variables.I2,
        variables.I4,
        variables.I8,
        variables.U1,
        variables.U2,
        variables.U4,
        variables.U8,
        variables.String
    ]
