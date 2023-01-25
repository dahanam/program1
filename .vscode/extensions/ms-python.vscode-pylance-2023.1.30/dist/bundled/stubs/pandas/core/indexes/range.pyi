import numpy as np
from pandas.core.indexes.base import Index
from pandas.core.indexes.numeric import Int64Index

from pandas._typing import (
    HashableT,
    npt,
)

class RangeIndex(Int64Index):
    def __new__(
        cls,
        start: int | RangeIndex = ...,
        stop: int = ...,
        step: int = ...,
        dtype=...,
        copy: bool = ...,
        name=...,
    ): ...
    def __init__(
        self,
        start: int | RangeIndex = ...,
        stop: int = ...,
        step: int = ...,
        dtype=...,
        copy: bool = ...,
        name=...,
    ): ...
    @classmethod
    def from_range(cls, data, name=..., dtype=...): ...
    def __reduce__(self): ...
    def start(self): ...
    def stop(self): ...
    def step(self): ...
    @property
    def nbytes(self) -> int: ...
    def memory_usage(self, deep: bool = ...) -> int: ...
    @property
    def dtype(self) -> np.dtype: ...
    @property
    def is_unique(self) -> bool: ...
    @property
    def is_monotonic_increasing(self) -> bool: ...
    @property
    def is_monotonic_decreasing(self) -> bool: ...
    @property
    def has_duplicates(self) -> bool: ...
    def __contains__(self, key: int | np.integer) -> bool: ...
    def get_loc(self, key, tolerance=...): ...
    def get_indexer(self, target, method=..., limit=..., tolerance=...): ...
    def tolist(self): ...
    def copy(self, name=..., deep: bool = ..., dtype=..., **kwargs): ...
    def min(self, axis=..., skipna: bool = ..., *args, **kwargs): ...
    def max(self, axis=..., skipna: bool = ..., *args, **kwargs): ...
    def argsort(self, *args, **kwargs): ...
    def factorize(
        self, sort: bool = ..., use_na_sentinel: bool = ...
    ) -> tuple[npt.NDArray[np.intp], RangeIndex]: ...
    def equals(self, other): ...
    def intersection(self, other, sort: bool = ...): ...
    def join(
        self,
        other,
        *,
        how: str = ...,
        level=...,
        return_indexers: bool = ...,
        sort: bool = ...,
    ): ...
    def __len__(self) -> int: ...
    @property
    def size(self) -> int: ...
    def __getitem__(self, key): ...
    def __floordiv__(self, other): ...
    def all(self) -> bool: ...
    def any(self) -> bool: ...
    def union(
        self, other: list[HashableT] | Index, sort=...
    ) -> Index | Int64Index | RangeIndex: ...
