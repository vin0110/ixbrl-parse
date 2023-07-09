import warnings
from copy import deepcopy
from datetime import date
from typing import Any, Dict, List, Optional

from bs4 import Tag

from ixbrlparse.components import ixbrlContext
from ixbrlparse.components.constants import NAME_SPLIT_EXPECTED
from ixbrlparse.components.transform import get_format, ixbrlFormat


class ixbrlNonNumeric:  # noqa: N801
    def __init__(
        self,
        context: Optional[ixbrlContext | str] = None,
        name: Optional[str] = None,
        format_: Optional[str] = None,
        value: Optional[str] = None,
        soup_tag: Optional[Tag] = None,
    ) -> None:
        if isinstance(name, str):
            name_split: List[str] = name.split(":", maxsplit=1)
            if len(name_split) == NAME_SPLIT_EXPECTED:
                self.schema = name_split[0]
                self.name = name_split[1]
            else:
                self.schema = "unknown"
                self.name = name_split[0]

        self.context = context
        self.format: Optional[ixbrlFormat] = None
        self.text: Optional[str] = value
        self.value = value
        if isinstance(format_, str) and format_ != "" and self.text is not None:
            try:
                self.format = get_format(format_)(format_=format_)
                self.value = self.format.parse_value(self.text)
            except NotImplementedError:
                msg = f"Format {format_} not implemented - value '{value}' not parsed"
                warnings.warn(msg, stacklevel=2)
        self.soup_tag = soup_tag

    def to_json(self) -> Dict[str, Any]:
        values = {k: deepcopy(v) for k, v in self.__dict__.items() if k != "soup_tag"}
        if isinstance(self.value, date):
            values["value"] = self.value.isoformat()
        if isinstance(self.format, ixbrlFormat):
            values["format"] = self.format.to_json()
        if isinstance(self.context, ixbrlContext):
            values["context"] = self.context.to_json()
        return values
