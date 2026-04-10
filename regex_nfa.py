import graphviz
import sys


class State:
    counter = 0

    def __init__(self):
        self.id = State.counter
        State.counter += 1
        self.vis = None
        self.trans = []
        self.eps = []
        self.start = False
        self.final = False


class RegexToNFA:

    def __init__(self, regex):
        State.counter = 0
        self.regex = regex.replace(" ", "")
        self.states = []

    # -------- Tokenizing --------
    def tokenize(self):
        tokens = []
        i = 0

        while i < len(self.regex):
            c = self.regex[i]

            if c == '\\' and i + 1 < len(self.regex):
                tokens.append(('char', self.regex[i + 1]))
                i += 2
            elif c in '()|*+?':
                tokens.append((c, c))
                i += 1
            else:
                tokens.append(('char', c))
                i += 1

        return tokens

    # -------- Parsing --------
    def parse(self):
        self.tokens = self.tokenize()
        self.pos = 0
        return self.expr()

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos][0]
        return None

    def eat(self, t=None):
        tok = self.tokens[self.pos]
        if t and tok[0] != t:
            raise Exception("Unexpected token")
        self.pos += 1
        return tok

    def expr(self):
        node = self.concat()
        while self.peek() == '|':
            self.eat('|')
            node = ('|', node, self.concat())
        return node

    def concat(self):
        node = self.factor()
        while self.peek() in ('char', '('):
            node = ('.', node, self.factor())
        return node

    def factor(self):
        node = self.atom()
        while self.peek() in ('*', '+', '?'):
            op = self.eat()[0]
            node = (op, node)
        return node

    def atom(self):
        if self.peek() == '(':
            self.eat('(')
            node = self.expr()
            self.eat(')')
            return node
        return ('char', self.eat('char')[1])

    # -------- NFA --------
    def new_state(self):
        s = State()
        self.states.append(s)
        return s

    def build(self, node):
        t = node[0]

        if t == 'char':
            s1 = self.new_state()
            s2 = self.new_state()
            s1.trans.append((node[1], s2))
            return s1, s2

        if t == '.':
            l1, l2 = self.build(node[1])
            r1, r2 = self.build(node[2])
            l2.eps.append(r1)
            return l1, r2

        if t == '|':
            l1, l2 = self.build(node[1])
            r1, r2 = self.build(node[2])

            s = self.new_state()
            e = self.new_state()

            s.eps += [l1, r1]
            l2.eps.append(e)
            r2.eps.append(e)

            return s, e

        if t == '*':
            s1, s2 = self.build(node[1])
            s = self.new_state()
            e = self.new_state()

            s.eps += [s1, e]
            s2.eps += [s1, e]

            return s, e

        if t == '+':
            s1, s2 = self.build(node[1])
            s = self.new_state()
            e = self.new_state()

            s.eps.append(s1)
            s2.eps += [s1, e]

            return s, e

        if t == '?':
            s1, s2 = self.build(node[1])
            s = self.new_state()
            e = self.new_state()

            s.eps += [s1, e]
            s2.eps.append(e)

            return s, e

    # -------- Convert --------
    def convert(self):
        tree = self.parse()
        start, end = self.build(tree)
        start.start = True
        end.final = True
        return self.order()

    def order(self):
        start = [s for s in self.states if s.start][0]
        visited = set()
        q = [start]
        res = []

        while q:
            s = q.pop(0)
            if s.id in visited:
                continue

            visited.add(s.id)
            res.append(s)

            for _, t in s.trans:
                q.append(t)
            for t in s.eps:
                q.append(t)

        for i, s in enumerate(res):
            s.vis = i

        return res

    # -------- Print --------
    def table(self, states):
        print("\nState | Input | Next")
        print("----------------------")

        for s in states:
            name = "->q" + str(s.vis) if s.start else "q" + str(s.vis)

            for t in s.eps:
                print(name, "| ε | q" + str(t.vis))

            for c, t in s.trans:
                print(name, "|", c, "| q" + str(t.vis))

        print("Final:",
              [f"q{s.vis}" for s in states if s.final])

    # -------- Graph --------
    def draw(self, states):
        dot = graphviz.Digraph(format='png')

        for s in states:
            if s.final:
                dot.node(f"q{s.vis}", shape='doublecircle')
            else:
                dot.node(f"q{s.vis}")

        for s in states:
            for t in s.eps:
                dot.edge(f"q{s.vis}", f"q{t.vis}", label='ε')
            for c, t in s.trans:
                dot.edge(f"q{s.vis}", f"q{t.vis}", label=c)

        dot.render("nfa_graph", view=True)


# -------- MAIN --------
if __name__ == "__main__":
    if len(sys.argv) > 1:
        r = sys.argv[1]
    else:
        r = input("regex: ")

    conv = RegexToNFA(r)
    st = conv.convert()

    conv.table(st)
    conv.draw(st)