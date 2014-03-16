"""BlocksWorld.py
   The classical robot planning program from Artificial Intelligence,
   used to demonstrate the T* system.

   Steven Tanimoto, 21 November 2005.

   Each state represents a configuration of three blocks, A, B, and C.
   They are initially piled up in the reverse order.  Although it's
   not represented in this program, the goal is usually to get them
   piled up in the opposite order.

   INITIAL STATE:

   [C]`
   [B]
   [A]
   -----------
   
   The available operators are the following.  The program allows the
   user to apply the operators and see the resulting states in a tree.

   Put A on B
   Put A on C
   Put B on A
   Put B on C
   Put C on A
   Put C on B
   Put A on table
   Put B on table
   Put C on table

Status: Working.  
"""

import TStar05b as TStar



def register_t_star_modifications():
  """This method sets various symbols within the TStar module
     to refer to their definitions related to the Blocks World
     application in this file. These definitions are given below
     this method."""
  TStar.__dict__.update({
    'TITLE':" Blocks-World State-Space Search with T*",
    'NODE_CLASS': BW_Node,
    'INITIAL_DATA': INITIAL_DATA
    })

# Some globals used for conveniently describing the states and
# operations:
A = 1; B = 2; C = 3 ; D = 4 ; E = 5 ; F = 6,
BLOCKS = [A,B,C,D,E,F] # used by BW_Node.paint_content

INITIAL_DATA = [(B,A),(C,B)] # B is on A, and C is on B.
    
class BW_Node(TStar.Node):
    # The following 3 methods override the parent methods to
    # change the application domain to the Blocks World.
    def domain_specific_init(self, state):
        self.display_elements = []

    def paint_content(self,w,h,a_canvas):
        """Adds the node's blocks and labels to the canvas
           at the right place."""
        self.has_painted_content=True
        block_x = range(4); block_y = range(4)
        x = 0
        # First assign x and y coords to blocks on the table:
        global BLOCKS
        unlocated = BLOCKS[:]
        for u in BLOCKS:
            if is_on_table(u, self.s.data):
                block_x[u] = x
                x += 1
                block_y[u] = 0
                unlocated.remove(u)
        # Then assign coords to the other block using the
        # constraints that they are "on" other blocks.
        while not unlocated==[]:
            unl = unlocated[:]
            for u in unl:
               for pair in self.s.data:
                    # Consider pairs starting with u.
                    (uu, v) = pair
                    if not uu == u: continue
                    if not v in unlocated:
                        # Good, u is on v, and v has coordinates.
                        block_x[u] = block_x[v]   # u gets v's x coord.
                        block_y[u] = block_y[v]+1 # u is 1 unit higher than v.
                        unlocated.remove(u) # u has now been 'located'
                        break;
        # Now plot the blocks and the letters in them.
        for block in BLOCKS:
            letter = ['A','B','C'][block-1]
            self.draw_block(letter, block_x[block], block_y[block], a_canvas, w, h)
    def unpaint_content(self,a_canvas):
        """deletes the node's blocks and labels from the canvas."""
        if self.has_painted_content:
            #a_canvas.delete(self.p)
            for elt in self.display_elements:
                a_canvas.delete(elt)
            self.display_elements = []
        self.has_painted_content=False
    def draw_block(self, letter, lx, ly, a_canvas, w, h):
        """Helper function for paint_content."""
        e = 20 # box spacing between centers
        m = 15 # size of box
        q = 5  # bottom margin
        if letter == "A":
          self.display_elements.append(
              a_canvas.create_rectangle(self.x+5-w/2   + lx*e, self.y+h/2-q-m - ly*e,
                                      self.x+5-w/2+m + lx*e, self.y+h/2-q   - ly*e,fill="White"))
        if letter == "B":
          self.display_elements.append(
              a_canvas.create_rectangle(self.x+5-w/2   + lx*e, self.y+h/2-q-m - ly*e,
                                      self.x+5-w/2+m + lx*e, self.y+h/2-q   - ly*e,fill="Orange"))
        if letter == "C":
          self.display_elements.append(
              a_canvas.create_rectangle(self.x+5-w/2   + lx*e, self.y+h/2-q-m - ly*e,
                                      self.x+5-w/2+m + lx*e, self.y+h/2-q   - ly*e,fill="Yellow"))
        self.display_elements.append(
            a_canvas.create_text(self.x+5-(3*w/8)+ lx*e, self.y+m/2-q+m+3 - ly*e))
        return

register_t_star_modifications()

def is_on(x, y, bw):
    "Tests whether x is on y in the current blocks world."
    return (x, y) in bw
def is_clear(x, bw):
    "Tests whether x is clear of objects on top of it."
    for pair in bw:
        if pair[1]==x: return False
    return True
def is_on_something(x, bw):
    "Tests whether x is on any other block."
    for pair in bw:
        if x==pair[0]: return True
    return False
def put_on(x,y, bw):
    """Copies current bw list (within the take_off method),
    making sure x is removed from any block it was already on,
    and then puts x on y.  It could be that x was on y and so,
    this ends up simply returning an equivalent blocks world to bw."""
    nw = take_off(x, bw)
    nw.append((x,y))
    return nw
def take_off(x, bw):
    """Copies the current bw list, and removes from the copy the
    first pair starting with x. (There should be at most one.)"""
    nw = bw[:]
    for (f,g)in bw:
        if x==f: nw.remove((f,g)); return nw
    return nw
def is_on_table(x,bw):
    """Returns True if x is not on any other block."""
    return not is_on_something(x,bw)

"""Note that the following operators are somewhat verbosely
represented.  They could have been generated by a function or two,
but the more verbose form is less abstract and therefore a little
easier to read."""

try_a_on_b = TStar.Operator("Try A on B",
               lambda w: put_on(A,B,w),
               precondition=lambda s: is_clear(A,s.data) and
                      is_clear(B,s.data))
try_a_on_c = TStar.Operator("Try A on C",
               lambda w: put_on(A,C,w),
               precondition=lambda s: is_clear(A,s.data) and
                      is_clear(C,s.data))
try_b_on_a = TStar.Operator("Try B on A",
               lambda w: put_on(B,A,w),
               precondition=lambda s: is_clear(B,s.data) and
                      is_clear(A,s.data))
try_b_on_c = TStar.Operator("Try B on C",
               lambda w: put_on(B,C,w),
               precondition=lambda s: is_clear(B,s.data) and
                      is_clear(C,s.data))
try_c_on_a = TStar.Operator("Try C on A",
               lambda w: put_on(C,A,w),
               precondition=lambda s: is_clear(C,s.data) and
                      is_clear(A,s.data))
try_c_on_b = TStar.Operator("Try C on B",
               lambda w: put_on(C,B,w),
               precondition=lambda s: is_clear(C,s.data) and
                      is_clear(B,s.data))
try_a_on_table = TStar.Operator("Try A on Table",
               lambda w: take_off(A,w),
               precondition=lambda s: is_clear(A,s.data) and
                          is_on_something(A,s.data))
try_b_on_table = TStar.Operator("Try B on Table",
               lambda w: take_off(B,w),
               precondition=lambda s: is_clear(B,s.data) and
                          is_on_something(B,s.data))
try_c_on_table = TStar.Operator("Try C on Table",
               lambda w: take_off(C,w),
               precondition=lambda s: is_clear(C,s.data) and
                          is_on_something(C,s.data))

TStar.register_operators([try_a_on_b, try_a_on_c,
                    try_b_on_a, try_b_on_c,
                    try_c_on_a, try_c_on_b,
                    try_a_on_table, try_b_on_table, try_c_on_table])


TStar.setup_and_run()

"""Here's the display algorithm for each states of the blocks world:

Unlocated = [A, B, C] # We don't yet know the coordinates of any blocks
Set X to 0
for e in unlocated:
   if e is on table:
       set e.x = X
       set X = X + 1 
       remove e from Unlocated.
while unlocated not empty,
   for e in unlocated,
      if e is on f and f is located,
         set e.x = f.x
         set e.y = f.y + 1
         remove e from located

"""
