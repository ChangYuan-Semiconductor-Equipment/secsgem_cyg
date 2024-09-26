"""V data item."""
from .. import variables
from .base import DataItemBase


class V(DataItemBase):  # pylint: disable=invalid-name
    """Variable data.

    :Types:
       - :class:`Array <secsgem_cyg.secs.variables.Array>`
       - :class:`Boolean <secsgem_cyg.secs.variables.Boolean>`
       - :class:`U1 <secsgem_cyg.secs.variables.U1>`
       - :class:`U2 <secsgem_cyg.secs.variables.U2>`
       - :class:`U4 <secsgem_cyg.secs.variables.U4>`
       - :class:`U8 <secsgem_cyg.secs.variables.U8>`
       - :class:`I1 <secsgem_cyg.secs.variables.I1>`
       - :class:`I2 <secsgem_cyg.secs.variables.I2>`
       - :class:`I4 <secsgem_cyg.secs.variables.I4>`
       - :class:`I8 <secsgem_cyg.secs.variables.I8>`
       - :class:`F4 <secsgem_cyg.secs.variables.F4>`
       - :class:`F8 <secsgem_cyg.secs.variables.F8>`
       - :class:`String <secsgem_cyg.secs.variables.String>`
       - :class:`Binary <secsgem_cyg.secs.variables.Binary>`

    **Used In Function**
        - :class:`SecsS06F11 <secsgem_cyg.secs.functions.SecsS06F11>`
        - :class:`SecsS06F16 <secsgem_cyg.secs.functions.SecsS06F16>`
        - :class:`SecsS06F20 <secsgem_cyg.secs.functions.SecsS06F20>`
        - :class:`SecsS06F22 <secsgem_cyg.secs.functions.SecsS06F22>`

    """

    __type__ = variables.Dynamic
    __allowedtypes__ = [
        variables.Array,
        variables.Boolean,
        variables.U1,
        variables.U2,
        variables.U4,
        variables.U8,
        variables.I1,
        variables.I2,
        variables.I4,
        variables.I8,
        variables.F4,
        variables.F8,
        variables.String,
        variables.Binary
    ]
