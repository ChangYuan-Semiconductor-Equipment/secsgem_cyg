"""Wrapper for GEM data value."""
from __future__ import annotations

import secsgem.secs


class DataValue:
    """Data value definition."""

    def __init__(self,
                 dvid: int | str,
                 name: str,
                 value_type: type[secsgem.secs.variables.Base],
                 use_callback: bool = True,
                 **kwargs):
        """Initialize a data value.

        You can manually set the secs-type of the id with the 'id_type' keyword argument.

        Custom parameters can be set with the keyword arguments,
        they will be passed to the GemEquipmentHandlers callback
        :func:`secsgem.gem.equipmenthandler.GemEquipmentHandler.on_dv_value_request`.

        If use_callbacks is disabled, you can set the value with the value property.

        Args:
            dvid: ID of the data value
            name: long name of the data value
            value_type: type of the data value
            use_callback: use the GemEquipmentHandler callbacks to get variable (True) or use internal value
            **kwargs: additional attributes for object

        """
        self._dvid = dvid
        self._name = name
        self._value_type = value_type
        self._use_callback = use_callback
        self.value = 0

        self._id_type: type[secsgem.secs.variables.Base]

        if isinstance(self._dvid, int):
            self._id_type = secsgem.secs.variables.U4
        else:
            self._id_type = secsgem.secs.variables.String

        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def dvid(self) -> int | str:
        """Get the data value id."""
        return self._dvid

    @property
    def name(self) -> str:
        """Get the data value name."""
        return self._name

    @property
    def value_type(self) -> type[secsgem.secs.variables.Base]:
        """Get the data value type."""
        return self._value_type

    @property
    def use_callback(self) -> bool:
        """Get if data value uses callback."""
        return self._use_callback

    @property
    def id_type(self) -> type[secsgem.secs.variables.Base]:
        """Get the data value id type."""
        return self._id_type
