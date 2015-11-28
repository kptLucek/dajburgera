class BurgerPlace:
  def __init__(self, addr, name):
    splitted = addr.split(",")
    self.addr = addr
    self.street = splitted[0].rsplit(' ', 1)[0]
    self.bdgNumber = splitted[0].rsplit(None, 1)[-1]
    self.code = splitted[1].strip().split(' ')[0]
    self.city = splitted[1].strip().split(' ')[1]
    self.country = splitted[2].strip()
    self.name = name
  def __str__(self):
    return self.name + ", " + self.addr;
