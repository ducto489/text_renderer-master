
from dataclasses import dataclass, field
from typing import List

@dataclass
class SimpleTextColorCfg:
    # ...existing code...
    text_color_cfg: List[FixedTextColorCfg] = field(default_factory=list)
    # ...existing code...