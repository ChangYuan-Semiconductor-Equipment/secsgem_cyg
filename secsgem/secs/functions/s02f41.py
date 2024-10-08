"""Class for stream 02 function 41."""

from secsgem.secs.data_items import CPNAME, CPVAL, RCMD
from secsgem.secs.functions.base import SecsStreamFunction


class SecsS02F41(SecsStreamFunction):
    """host command - send.

    Args:
        value: parameters for this function (see example)

    Examples:
        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS02F41
        {
            RCMD: U1/I1/A
            PARAMS: [
                {
                    CPNAME: U1/U2/U4/U8/I1/I2/I4/I8/A
                    CPVAL: BOOLEAN/U1/U2/U4/U8/I1/I2/I4/I8/A/B
                }
                ...
            ]
        }

        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS02F41({"RCMD": "COMMAND", "PARAMS": [{"CPNAME": "PARAM1", "CPVAL": "VAL1"},
        ...     {"CPNAME": "PARAM2", "CPVAL": "VAL2"}]})
        S2F41 W
          <L [2]
            <A "COMMAND">
            <L [2]
              <L [2]
                <A "PARAM1">
                <A "VAL1">
              >
              <L [2]
                <A "PARAM2">
                <A "VAL2">
              >
            >
          > .

    Data Items:
        - :class:`RCMD <secsgem.secs.data_items.RCMD>`
        - :class:`CPNAME <secsgem.secs.data_items.CPNAME>`
        - :class:`CPVAL <secsgem.secs.data_items.CPVAL>`

    """

    _stream = 2
    _function = 41

    _data_format = [
        RCMD,
        [
            [
                "PARAMS",
                CPNAME,
                CPVAL
            ]
        ]
    ]

    _to_host = False
    _to_equipment = True

    _has_reply = True
    _is_reply_required = True

    _is_multi_block = False
