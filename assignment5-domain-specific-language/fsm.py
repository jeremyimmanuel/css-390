'''
Jeremy Tandjung
CSS 390
Finite-State Machine Generator
'''
class Machine(object):

    def __init__(self, funcName):
        self._header = ''
        self._footer = ''
        self._states = []
        self._edges = []
        self._func = funcName
    
    def edge(self, name: str, next_state: str, action_string  = ''):
        t = (name, next_state, action_string)
        self._edges.append(t)
        return t

    def edges(self, *argv):
        arr = []

        for arg in argv:
            arr.append(self.edge(arg[0], arg[1]))
        
        return arr

    def state(self, name: str, action = '', edges = ()):
        self._states.append((name, action, edges))

    def header(self, text: str):
        self._header = text
    
    def footer(self, text: str):
        self._footer = text

    def printEventEnum(self):
        print('enum Event {')
        s = set()
        for e in self._edges:
            if e[0] not in s:            
                print(f'  {e[0]}_EVENT,')
                s.add(e[0])
        print(f'  INVALID_EVENT')
        print('};')
        

    def printEventName(self):
        print('const char * EVENT_NAMES[] = {')
        s = set()
        for e in self._edges:
            if e[0] not in s:
                print(f'  "{e[0]}",')
                s.add(e[0])
        print('};')

    def printStates(self):
        print('enum State {')
        for s in self._states:
            print(f'  {s[0]}_STATE,')
        print('};')

    def printS2E(self):
        print('Event string_to_event(string event_string) {')
        s = set()
        for e in self._edges:
            if e[0] not in s:
                print('  if (event_string == "%s") {return %s;}' % (e[0], e[0]+'_EVENT'))
                s.add(e[0])

        print('  return INVALID_EVENT;\n}')

    def printFunc(self):
        print('int %s(State initial_state) {' % self._func)
        print(''' \tState state = initial_state;
\tEvent event;
\twhile (true) {
\t\tswitch(state) {''')
        print()
        for s in self._states:
            self.printStateCase(s)
        print('\t\t}\n\t}\n}')

    def printEventCase(self, event: tuple):
        print('\t\t\t\t\tcase %s_EVENT:' % event[0])
        if event[2] != '':
            print('\t\t\t\t\t%s' % event[2].strip())

        print('\t\t\t\t\t\tstate = %s_STATE;\n\t\t\t\t\t\tbreak;' % event[1])
        print()

        
    def printStateCase(self, state: tuple):
        print('\t\t\tcase %s_STATE:' % state[0])
        print('\t\t\t\tcerr << "state %s" << endl;' % state[0])
        if state[1] != '':
            print('\t\t\t\t%s' % state[1].strip('"'))
            

        if len(state[2]) == 0:
            print('''\t\t\t\tcout << "Input is valid float" << endl;
            \t\t\t\treturn 1;
            ''')
        print('\t\t\t\tevent = get_next_event();')
        print('\t\t\t\tcerr << "event" << EVENT_NAMES[event] << endl;')
        print('\t\t\t\tswitch (event) {')
        print()
        if len(state[2]) > 0:
            for e in state[2]: #
                self.printEventCase(e)
        
        print('''
        default:
            cerr << "INVALID EVENT" << event << " in state %s" << endl;
            return -1;
        }
        break;\n
        ''' % state[0])
        
        




    def gen(self):
        print(self._header)
        self.printStates()
        print()
        self.printEventEnum()
        print()
        self.printEventName()
        print()
        print('Event get_next_event();')
        print()
        self.printS2E()
        print()
        self.printFunc()
        print(self._footer)
    