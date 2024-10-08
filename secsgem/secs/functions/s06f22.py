"""Class for stream 06 function 22."""

from secsgem.secs.data_items import VID, V
from secsgem.secs.functions.base import SecsStreamFunction


class SecsS06F22(SecsStreamFunction):
    """annotated individual report data.

    Args:
        value: parameters for this function (see example)

    Examples:
        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS06F22
        [
            {
                VID: U1/U2/U4/U8/I1/I2/I4/I8/A
                V: L/BOOLEAN/U1/U2/U4/U8/I1/I2/I4/I8/F4/F8/A/B
            }
            ...
        ]

        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS06F22([{"VID": "VID1", "V": "ASD"}, {"VID": 2, "V": 1337}])
        S6F22
          <L [2]
            <L [2]
              <A "VID1">
              <A "ASD">
            >
            <L [2]
              <U1 2 >
              <U2 1337 >
            >
          > .

    Data Items:
        - :class:`VID <secsgem.secs.data_items.VID>`
        - :class:`V <secsgem.secs.data_items.V>`

    """

    _stream = 6
    _function = 22

    _data_format = [
        [
            VID,
            V
        ]
    ]

    _to_host = True
    _to_equipment = False

    _has_reply = False
    _is_reply_required = False

    _is_multi_block = True
