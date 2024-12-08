class Expr:
    def accept(self, visitor):
        raise NotImplementedError()

class ExprVisitor:
    def visit_binary(self, binary):
        raise NotImplementedError()

    def visit_grouping(self, grouping):
        raise NotImplementedError()

    def visit_literal(self, literal):
        raise NotImplementedError()

    def visit_unary(self, unary):
        raise NotImplementedError()

class Binary(Expr):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor):
        return visitor.visit_binary(self)

class Grouping(Expr):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        return visitor.visit_grouping(self)

class Literal(Expr):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visit_literal(self)

class Unary(Expr):
    def __init__(self, operator, right):
        self.operator = operator
        self.right = right

    def accept(self, visitor):
        return visitor.visit_unary(self)

