from dataclasses import dataclass

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
        Get text size without offset

        Returns:
            width, height
        """
        if self.horizontal:
            mask = self.font.getmask(self.text)
            left, top, right, bottom = mask.getbbox()
            return right - left, bottom - top
        else:
            masks = [self.font.getmask(c) for c in self.text]
            widths = [mask.getbbox()[2] - mask.getbbox()[0] for mask in masks]
            heights = [mask.getbbox()[3] - mask.getbbox()[1] for mask in masks]
            width = max(widths)
            height = sum(heights)
            return height, width
