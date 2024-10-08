"""Class for stream 12 function 19."""

from secsgem.secs.data_items import DATLC, MAPER
from secsgem.secs.functions.base import SecsStreamFunction


class SecsS12F19(SecsStreamFunction):
    """map error report - send.

    Args:
        value: parameters for this function (see example)

    Examples:
        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS12F19
        {
            MAPER: B[1]
            DATLC: U1
        }

        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS12F19({"MAPER": secsgem.secs.data_items.MAPER.INVALID_DATA, "DATLC": 0})
        S12F19
          <L [2]
            <B 0x1>
            <U1 0 >
          > .

    Data Items:
        - :class:`MAPER <secsgem.secs.data_items.MAPER>`
        - :class:`DATLC <secsgem.secs.data_items.DATLC>`

    """

    _stream = 12
    _function = 19

    _data_format = [
        MAPER,
        DATLC
    ]

    _to_host = True
    _to_equipment = True

    _has_reply = False
    _is_reply_required = False

    _is_multi_block = False
