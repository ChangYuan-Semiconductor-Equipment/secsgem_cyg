"""ATTRID data item."""
from .. import variables
from .base import DataItemBase


class ATTRID(DataItemBase):
    """Object attribute identifier.

    :Types:
       - :class:`U1 <secsgem_cyg.secs.variables.U1>`
       - :class:`U2 <secsgem_cyg.secs.variables.U2>`
       - :class:`U4 <secsgem_cyg.secs.variables.U4>`
       - :class:`U8 <secsgem_cyg.secs.variables.U8>`
       - :class:`String <secsgem_cyg.secs.variables.String>`

    **Used In Function**
        - :class:`SecsS14F01 <secsgem_cyg.secs.functions.SecsS14F01>`
        - :class:`SecsS14F02 <secsgem_cyg.secs.functions.SecsS14F02>`
        - :class:`SecsS14F03 <secsgem_cyg.secs.functions.SecsS14F03>`
        - :class:`SecsS14F04 <secsgem_cyg.secs.functions.SecsS14F04>`

    """

    __type__ = variables.Dynamic
    __allowedtypes__ = [
        variables.U1,
        variables.U2,
        variables.U4,
        variables.U8,
        variables.String
    ]
