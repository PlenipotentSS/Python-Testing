"""MissAndCann.py
   An application ot T* to the Missionaries and Cannibals Puzzle

   S. Tanimoto, 23 November 2005, modified 4 Jan. 2006

   State representation by a vector (m, c, b), where
     m = number of missionaries on left bank
     c = number of cannibals on left bank
     b = 0 if boat is at left bank, 1 if at right bank

     State display:
     +---+---+---+
     |MMM|B  |   |
     |CCC|   |   |
     +---+---+---+
"""
import TStar05b as TStar
INITIAL_STATE = None

INITIAL_DATA = (3,3,0)
def register_t_star_modifications():
  TStar.__dict__.update({
    'TITLE':" Missionaries and Cannibals State-Space Search with T*",
    'NODE_CLASS': MC_Node,
    'INITIAL_DATA': INITIAL_DATA,
    'HEADLINE':"###Missionaries and Cannibals Tree Description File",
    'TREE_FILE_TYPE':"mct",
    'ROOT_DATA_FILE_TYPE':"mcs",
    'ROOT_DATA_TYPE_DESCRIPTION':"Missionaries and Cannibals State"
    })

class MC_Node(TStar.Node):
    width = 100
    # The following 3 methods override the parent methods to
    # change the application domain to the Blocks World.
    def domain_specific_init(self, state):
        self.display_elements = []

    def paint_content(self,w,h,a_canvas):
        """Adds the node's displayable image to the canvas
           at the right place."""
        self.has_painted_content=True
        Left_M_str = 'M'*self.s.data[0]
        Right_M_str = 'M'*(3-self.s.data[0])
        Left_C_str = 'C'*self.s.data[1]
        Right_C_str = 'C'*(3-self.s.data[1])
        self.display_elements.append(
            a_canvas.create_text(self.x-w/2+25,
                                 self.y-h/2+15,
                                 text=str(Left_M_str)))
        self.display_elements.append(
            a_canvas.create_text(self.x-w/2+25,
                                 self.y,
                                 text=str(Left_C_str)))
        self.display_elements.append(
            a_canvas.create_text(self.x+w/2-25,
                                 self.y-h/2+15,
                                 text=str(Right_M_str)))
        self.display_elements.append(
            a_canvas.create_text(self.x+w/2-25,
                                 self.y,
                                 text=str(Right_C_str)))
        boat_dx = -w/4
        if self.s.data[2]: boat_dx = w/4
        self.display_elements.append(
            a_canvas.create_text(self.x+boat_dx,
                                 self.y+h/2-15,
                                 text='B'))
        boat_x = -w/4
        
    def unpaint_content(self,a_canvas):
        """negates the node's image from the canvas."""
        if self.has_painted_content:
            for elt in self.display_elements:
                a_canvas.delete(elt)
            self.display_elements = []
        self.has_painted_content=False
        return

register_t_star_modifications()

# Operators:
'''
cross river with 1 M
cross river with 2 M
etc.
'''
def cross_with(dm,dc,w):
    M = w[0]
    C = w[1]
    result = None
    if dc > dm: return None
    boat_on_right = w[2]
    if not boat_on_right:
        if dm <= M and dc <= C and (M == dm or M - dm >= C - dc) and\
           (3 - M + dm ==0 or 3 - M + dm >= 3 - C + dc) :
            result = (M - dm, C - dc, 1)
    else:
        if (dm <= (3-M)) and (dc <= (3-C)) and\
           (3 - M - dm == 0 or 3 - M - dm >= 3 - C - dc) and\
           (M + dm) >= C + dc:
            result = (M + dm, C + dc, 0)
    return result

class cross_river_fn:
    def __init__(self,dm,dc):
        self.dm = dm
        self.dc = dc
    def __call__(self, s):
        if isinstance(s,TStar.State):
            return cross_with(self.dm, self.dc, s.data)
        else: return cross_with(self.dm, self.dc, s)
        
ops = []
for dm in range(4)[1:]:
    for dc in range(dm+1):
        if dm + dc > 3: continue
        print 'Generating operator with (m,c)=(',dm,',',dc,')'
        op = TStar.Operator(
            'Cross river with '+str(dm)+' missionaries and '+\
                            str(dc)+' cannibals',
            cross_river_fn(dm,dc),
            precondition=cross_river_fn(dm,dc))
        ops.append(op)
print map(lambda op: op.name, ops)
TStar.register_operators(ops)

TStar.setup_and_run()
