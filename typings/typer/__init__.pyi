from collections.abc import Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")
T = TypeVar("T")


class Exit(Exception):
    def __init__(self, code: int = ...) -> None: ...


class Typer:
    def __init__(
        self,
        *,
        add_completion: bool = ...,
        no_args_is_help: bool = ...,
    ) -> None: ...
    def command(
        self,
        name: str | None = ...,
    ) -> Callable[[Callable[P, R]], Callable[P, R]]: ...
    def __call__(self) -> None: ...


def Option(
    default: T,
    *,
    exists: bool = ...,
    file_okay: bool = ...,
    resolve_path: bool = ...,
) -> T: ...


def echo(message: object, *, err: bool = ...) -> None: ...
