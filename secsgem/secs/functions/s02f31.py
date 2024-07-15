from secsgem.secs import SecsStreamFunction
from secsgem.secs.data_items import TIME


class SecsS02F31(SecsStreamFunction):
    _stream = 2
    _function = 31

    _dataFormat = TIME

    _toHost = False
    _toEquipment = True

    _hasReply = True
    _isReplyRequired = True

    _isMultiBlock = True
