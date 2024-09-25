"""Class for stream 12 function 16."""

from secsgem.secs.data_items import BINLT, IDTYP, MID, STRP
from secsgem.secs.functions.base import SecsStreamFunction


class SecsS12F16(SecsStreamFunction):
    """map data type 2.

    Args:
        value: parameters for this function (see example)

    Examples:
        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS12F16
        {
            MID: A/B[80]
            IDTYP: B[1]
            STRP: I1/I2/I4/I8[2]
            BINLT: U1/A
        }

        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS12F16({
        ...     "MID": "materialID",
        ...     "IDTYP": secsgem.secs.data_items.IDTYP.WAFER,
        ...     "STRP": [0, 1],
        ...     "BINLT": [1, 2, 3, 4, 5, 6]})
        S12F16
          <L [4]
            <A "materialID">
            <B 0x0>
            <I1 0 1 >
            <U1 1 2 3 4 5 6 >
          > .

    Data Items:
        - :class:`MID <secsgem.secs.data_items.MID>`
        - :class:`IDTYP <secsgem.secs.data_items.IDTYP>`
        - :class:`STRP <secsgem.secs.data_items.STRP>`
        - :class:`BINLT <secsgem.secs.data_items.BINLT>`

    """

    _stream = 12
    _function = 16

    _data_format = [
        MID,
        IDTYP,
        STRP,
        BINLT
    ]

    _to_host = False
    _to_equipment = True

    _has_reply = False
    _is_reply_required = False

    _is_multi_block = True
