"""Class for stream 05 function 11."""

from secsgem.secs.data_items import EXID, EXMESSAGE, EXTYPE, TIMESTAMP
from secsgem.secs.functions.base import SecsStreamFunction


class SecsS05F11(SecsStreamFunction):
    """exception clear - notify.

    Args:
        value: parameters for this function (see example)

    Examples:
        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS05F11
        {
            TIMESTAMP: A[32]
            EXID: A[20]
            EXTYPE: A
            EXMESSAGE: A
        }

        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS05F11({
        ...     "TIMESTAMP": "161006221500",
        ...     "EXID": "EX123",
        ...     "EXTYPE": "ALARM",
        ...     "EXMESSAGE": "Exception"})
        S5F11
          <L [4]
            <A "161006221500">
            <A "EX123">
            <A "ALARM">
            <A "Exception">
          > .

    Data Items:
        - :class:`TIMESTAMP <secsgem.secs.data_items.TIMESTAMP>`
        - :class:`EXID <secsgem.secs.data_items.EXID>`
        - :class:`EXTYPE <secsgem.secs.data_items.EXTYPE>`
        - :class:`EXMESSAGE <secsgem.secs.data_items.EXMESSAGE>`

    """

    _stream = 5
    _function = 11

    _data_format = [
        TIMESTAMP,
        EXID,
        EXTYPE,
        EXMESSAGE
    ]

    _to_host = True
    _to_equipment = False

    _has_reply = True
    _is_reply_required = False

    _is_multi_block = False
