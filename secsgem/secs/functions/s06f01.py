"""Class for stream 06 function 01."""

from secsgem.secs.data_items import SMPLN, STIME, SV, TRID
from secsgem.secs.functions.base import SecsStreamFunction


class SecsS06F01(SecsStreamFunction):
    """Trace data send.

    Args:
        value: parameters for this function (see example)

    Examples:
        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS06F01
        {
            TRID: I1/I2/I4/I8/U1/U2/U4/U8/A
            SMPLN: I1/I2/I4/I8/U1/U2/U4/U8
            STIME: A
            SV: [
                DATA: L/BOOLEAN/U1/U2/U4/U8/I1/I2/I4/I8/F4/F8/A/B
                ...
            ]
        }

        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS06F01({
        ...     "TRID": 1,
        ...     "SMPLN": 3,
        ...     "STIME": "TIME",
        ...     "SV": [1, 4]})
        S6F1
          <L [4]
            <I1 1 >
            <I1 3 >
            <A "TIME">
            <L [2]
              <U1 1 >
              <U1 4 >
            >
          > .

    Data Items:
        - :class:`TRID <secsgem.secs.data_items.TRID>`
        - :class:`SMPLN <secsgem.secs.data_items.SMPLN>`
        - :class:`STIME <secsgem.secs.data_items.STIME>`
        - :class:`SV <secsgem.secs.data_items.SV>`

    """

    _stream = 6
    _function = 1

    _data_format = [
        TRID,
        SMPLN,
        STIME,
        [SV]
    ]

    _to_host = True
    _to_equipment = False

    _has_reply = True
    _is_reply_required = False

    _is_multi_block = True
