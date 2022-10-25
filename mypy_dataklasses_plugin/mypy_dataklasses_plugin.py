from mypy.plugin import Plugin, AttributeContext, FunctionContext, ClassDefContext
from typing import Callable, Dict, List, Optional, Tuple, Type, Union, Any
from mypy.types import Type as MypyType, NoneType, ProperType
from mypy.nodes import TypeInfo, Argument, ArgKind, AssignmentStmt, PlaceholderNode, NameExpr, Var
from mypy.plugins.common import add_method, get_proper_type


class DataklassesPlugin(Plugin):

    def get_class_decorator_hook(self, fullname: str, ) -> Optional[Callable[[ClassDefContext], None]]:
        if fullname == 'dataklasses.dataklass':
            return _analyze_dataklass_decorator
        return None


def _analyze_dataklass_decorator(ctx: ClassDefContext) -> None:
    info = ctx.cls.info
    attributes = _collect_attributes(info)
    if '__init__' not in info.names:
        arguments = [
            Argument(
                variable=Var(arg_name, arg_type),
                type_annotation=arg_type,
                initializer=None,
                kind=ArgKind.ARG_POS,
            )
            for arg_name, arg_type in attributes
        ]
        add_method(ctx, "__init__", args=arguments, return_type=NoneType())


def _collect_attributes(info: TypeInfo) -> List[Tuple[str, ProperType]]:
    attributes = []
    for stmt in info.defn.defs.body:
        if not (isinstance(stmt, AssignmentStmt) and stmt.new_syntax):
            continue
        lhs = stmt.lvalues[0]
        if not isinstance(lhs, NameExpr):
            continue

        sym = info.names.get(lhs.name)
        if sym is None:
            # There was probably a semantic analysis error.
            continue

        node = sym.node
        assert not isinstance(node, PlaceholderNode)
        assert isinstance(node, Var)

        typ = get_proper_type(node.type)
        assert typ is not None

        attributes.append((lhs.name, typ))
    return attributes


def plugin(version: str) -> Type[Plugin]:
    return DataklassesPlugin
