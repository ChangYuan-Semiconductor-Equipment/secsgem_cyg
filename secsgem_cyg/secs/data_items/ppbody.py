"""PPBODY data item."""
from .. import variables
from .base import DataItemBase


class PPBODY(DataItemBase):
    """Status variable ID.

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
       - :class:`Binary <secsgem_cyg.secs.variables.Binary>`

    **Used In Function**
        - :class:`SecsS07F03 <secsgem_cyg.secs.functions.SecsS07F03>`
        - :class:`SecsS07F06 <secsgem_cyg.secs.functions.SecsS07F06>`

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
        variables.String,
        variables.Binary
    ]
