"""ECID data item."""
from .. import variables
from .base import DataItemBase


class ECID(DataItemBase):
    """Equipment constant ID.

    :Types:
       - :class:`U1 <secsgem_cyg.secs.variables.U1>`
       - :class:`U2 <secsgem_cyg.secs.variables.U2>`
       - :class:`U4 <secsgem_cyg.secs.variables.U4>`
       - :class:`U8 <secsgem_cyg.secs.variables.U8>`
       - :class:`I1 <secsgem_cyg.secs.variables.I1>`
       - :class:`I2 <secsgem_cyg.secs.variables.I2>`
       - :class:`I4 <secsgem_cyg.secs.variables.I4>`
       - :class:`I8 <secsgem_cyg.secs.variables.I8>`
       - :class:`String <secsgem_cyg.secs.variables.String>`

    **Used In Function**
        - :class:`SecsS02F13 <secsgem_cyg.secs.functions.SecsS02F13>`
        - :class:`SecsS02F15 <secsgem_cyg.secs.functions.SecsS02F15>`
        - :class:`SecsS02F29 <secsgem_cyg.secs.functions.SecsS02F29>`
        - :class:`SecsS02F30 <secsgem_cyg.secs.functions.SecsS02F30>`

    """

    __type__ = variables.Dynamic
    __allowedtypes__ = [
        variables.U1,
        variables.U2,
        variables.U4,
        variables.U8,
        variables.I1,
        variables.I2,
        variables.I4,
        variables.I8,
        variables.String
    ]
