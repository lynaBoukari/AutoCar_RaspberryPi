
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '58BE475FE8304B2ACDED6242F3DF6E5C'
    
_lr_action_items = {'STOP':([0,],[4,]),'FORWARD':([0,],[6,]),'REVERSE':([0,],[7,]),'TURNLEFT':([0,],[8,]),'TURNRIGHT':([0,],[9,]),'$end':([0,1,2,3,4,5,12,13,14,15,],[-9,0,-1,-2,-3,-4,-7,-8,-5,-6,]),'FLOAT':([6,7,8,9,],[10,11,12,13,]),'INT':([10,11,],[14,15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'commandDC':([0,],[2,]),'commandSERVO':([0,],[3,]),'empty':([0,],[5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> commandDC','prog',1,'p_prog','prog.py',47),
  ('prog -> commandSERVO','prog',1,'p_prog','prog.py',48),
  ('prog -> STOP','prog',1,'p_prog','prog.py',49),
  ('prog -> empty','prog',1,'p_prog','prog.py',50),
  ('commandDC -> FORWARD FLOAT INT','commandDC',3,'p_commandDC','prog.py',67),
  ('commandDC -> REVERSE FLOAT INT','commandDC',3,'p_commandDC','prog.py',68),
  ('commandSERVO -> TURNLEFT FLOAT','commandSERVO',2,'p_commandSERVO','prog.py',74),
  ('commandSERVO -> TURNRIGHT FLOAT','commandSERVO',2,'p_commandSERVO','prog.py',75),
  ('empty -> <empty>','empty',0,'p_empty','prog.py',83),
]