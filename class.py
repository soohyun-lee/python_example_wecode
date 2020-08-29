Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Database:
  def __init__(self,name,size): ##생성자
    self.name = name
    self.size = size
    self.data_   = {}
    
  def insert(self, field, value): ##메소드
    if len(self.data_) < self.size:
      self.data_[field] = value
      
  def select(self, field):
    if field in self.data_:
      return self.data_[field]
    else:
      return None
    
  def update(self, field, value):
    if field in self.data_:
      self.data_[field] = value
  
  def delete(self, field):
    if field in self.data_:
      del self.data_[field]