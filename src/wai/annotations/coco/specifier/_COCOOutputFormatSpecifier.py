from typing import Type, Tuple

from wai.annotations.core.component import Component
from wai.annotations.core.domain import DomainSpecifier
from wai.annotations.core.specifier import SinkStageSpecifier


class COCOOutputFormatSpecifier(SinkStageSpecifier):
    """
    Specifier of the components for writing the MS-COCO JSON-based
    object detection format.
    """
    @classmethod
    def description(cls) -> str:
        return "Writes image object-detection annotations in the MS-COCO JSON-format"

    @classmethod
    def components(cls) -> Tuple[Type[Component], ...]:
        from ..component import ToCOCOExternalFormat, COCOWriter
        return ToCOCOExternalFormat, COCOWriter

    @classmethod
    def domain(cls) -> Type[DomainSpecifier]:
        from wai.annotations.domain.image.object_detection import ImageObjectDetectionDomainSpecifier
        return ImageObjectDetectionDomainSpecifier
