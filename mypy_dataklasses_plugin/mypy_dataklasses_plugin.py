from mypy.plugin import Plugin, AttributeContext, FunctionContext
from typing import Callable, Dict, List, Optional, Tuple, Type, Union, Any
from mypy.types import Type as MypyType
from mypy.nodes import TypeInfo


class DataklassesPlugin(Plugin):

    def get_attribute_hook(self, fullname: str) -> Optional[Callable[[AttributeContext], MypyType]]:
        print(f"get_attribute_hook: {fullname}")
        return None

    def get_function_hook(self, fullname: str) -> Optional[Callable[[FunctionContext], MypyType]]:
        # TODO
        # 1 найти сигнатуру _init_
        #     1.1 поискать в self
        #     1.2 гуглить как достать сигнатуру init через self
        # 2 проанализировать сигнатуру _init на соостветсвие типизации
        # зы пока не удалось отладчиком поймать код внутри хука
        print(f"get_function_hook: {fullname}")
        return None

def plugin(version):
    return DataklassesPlugin


