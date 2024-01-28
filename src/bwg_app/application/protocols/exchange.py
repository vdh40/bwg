from typing import Protocol, Sequence

from bwg_app.application.dto.course import CourseDtoIn
from bwg_app.application.dto.currency import CurrencyDtoIn


class ExchangeProtocol(Protocol):
    def get_all_currencies(self) -> Sequence[CurrencyDtoIn]:
        pass

    def get_course(self, left_currency_code: str, right_currency_code: str) -> CourseDtoIn | None:
        pass
