        | 0     | 时间设置成功                                 | :const:`secsgem.secs.data_items.TIACK.ACK`              |
        +-------+--------------------------------------------+---------------------------------------------------------+
        | 1     | 时间设置失败                                 | :const:`secsgem.secs.data_items.TIACK.TIME_SET_FAIL`    |
        +-------+--------------------------------------------+---------------------------------------------------------+

    **Used In Function**
        - :class:`SecsS02F46 <secsgem.secs.functions.SecsS02F46>`

    """

    __type__ = variables.Binary
    __count__ = 1

    ACK = 0
    TIME_SET_FAIL = 1
