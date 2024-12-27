from dataclasses import dataclass

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

from PIL.ImageFont import FreeTypeFont

@dataclass
class FontText:
    font: FreeTypeFont
    text: str
    font_path: str
    horizontal: bool = True

    @property
    def xy(self):
        mask = self.font.getmask(self.text)
        left, top, right, bottom = mask.getbbox()
        return -left, -top

    @property
    def offset(self):
        mask = self.font.getmask(self.text)
        left, top, right, bottom = mask.getbbox()
        return (-left, -top)

    @property
    def size(self) -> [int, int]:
        """
        Get text size using matplotlib
        """
        fig, ax = plt.subplots()
        # Set font properties from self.font_path or fallback
        font_prop = FontProperties(fname=self.font_path, size=self.font.size)
        text_obj = ax.text(0, 0, self.text, fontproperties=font_prop)
        fig.canvas.draw()
        bbox = text_obj.get_window_extent(renderer=fig.canvas.get_renderer())
        width, height = bbox.width, bbox.height
        plt.close(fig)
        return int(width), int(height)
