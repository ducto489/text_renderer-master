import inspect
import os
from pathlib import Path
import imgaug.augmenters as iaa

from text_renderer.effect import *
from text_renderer.corpus import *

from text_renderer.config import (
    RenderCfg,
    NormPerspectiveTransformCfg,
    GeneratorCfg,
)
from text_renderer.layout.same_line import SameLineLayout
from text_renderer.layout.extra_text_line import ExtraTextLineLayout

CURRENT_DIR = Path(os.path.abspath(os.path.dirname(__file__)))
OUT_DIR = CURRENT_DIR / "output"
DATA_DIR = CURRENT_DIR
BG_DIR = DATA_DIR / "bg"
CHAR_DIR = DATA_DIR / "char"
FONT_DIR = DATA_DIR / "font"
FONT_LIST_DIR = DATA_DIR / "font_list"
TEXT_DIR = DATA_DIR / "text"

font_cfg = dict(
    font_dir=FONT_DIR,
    font_list_file=FONT_LIST_DIR / "font_list.txt",
    font_size=(30, 31),
)

def get_word_corpus(**kwargs):
    cfg = {
        'text_paths': [TEXT_DIR / "vie_text.txt"],
        'num_word': (1, 4),
        **font_cfg,
        **kwargs
    }
    return WordCorpus(WordCorpusCfg(**cfg))

def base_cfg(
    name: str, corpus, corpus_effects=None, layout_effects=None, layout=None, gray=True, perspective_transform=None
):
    return GeneratorCfg(
        num_image=1000,
        save_dir=OUT_DIR / name,
        render_cfg=RenderCfg(
            bg_dir=BG_DIR,
            perspective_transform=perspective_transform,
            gray=gray,
            layout_effects=layout_effects,
            layout=layout,
            corpus=corpus,
            corpus_effects=corpus_effects,
        ),
    )


def no_effect():
    return base_cfg(
        inspect.currentframe().f_code.co_name,
        corpus=get_word_corpus(),
        corpus_effects=Effects(
            [
                Padding(p=1, w_ratio=[0.5, 0.51], h_ratio=[0.7, 0.71], center=True),
            ]
        ),
    )

def compact():
    return base_cfg(
        inspect.currentframe().f_code.co_name,
        corpus=get_word_corpus(char_spacing=-0.05),
        corpus_effects=Effects(
            [
                Padding(p=1, w_ratio=[0.5, 0.51], h_ratio=[0.7, 0.71], center=True),
            ]
        ),
    )
    
def large_spacing():
    return base_cfg(
        inspect.currentframe().f_code.co_name,
        corpus=get_word_corpus(char_spacing=0.3),
        corpus_effects=Effects(
            [
                Padding(p=1, w_ratio=[0.5, 0.51], h_ratio=[0.7, 0.71], center=True),
            ]
        ),
    )

def perspective_transform():
    return base_cfg(
        inspect.currentframe().f_code.co_name,
        corpus=get_word_corpus(),
        corpus_effects=Effects(
            [
                Padding(p=1, w_ratio=[0.5, 0.51], h_ratio=[0.7, 0.71], center=True),
            ]
        ),
        perspective_transform=NormPerspectiveTransformCfg(20, 20, 1.5)
    )

def imgaug_emboss_example():
    return base_cfg(
        inspect.currentframe().f_code.co_name,
        corpus=get_word_corpus(),
        corpus_effects=Effects(
            [
                Padding(p=1, w_ratio=[0.2, 0.21], h_ratio=[0.7, 0.71], center=True),
                ImgAugEffect(aug=iaa.Emboss(alpha=(0.9, 1.0), strength=(1.5, 1.6))),
            ]
        ),
    )

# fmt: off
# The configuration file must have a configs variable
configs = [
    no_effect(),
    compact(),
    large_spacing(),
    perspective_transform(),
    imgaug_emboss_example()
]
# fmt: on
