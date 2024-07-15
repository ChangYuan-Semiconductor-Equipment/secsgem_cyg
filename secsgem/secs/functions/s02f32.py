from secsgem.secs.functions.base import SecsStreamFunction
from secsgem.secs.data_items.tiack import TIACK


class SecsS02F32(SecsStreamFunction):
    _stream = 2
    _function = 32

    _dataFormat = TIACK

    _toHost = True
    _toEquipment = False

    _hasReply = False
    _isReplyRequired = False

    _isMultiBlock = False
