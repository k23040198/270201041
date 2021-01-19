class DNA():
  def __init__(self,dna):
    self.dna=dna
    self.dna_dict={"A":0,"T":0,"G":0,"C":0}

  def count_nucleotides(self):
    for _ in self.dna:
      if _== "A":
        self.dna_dict["A"]+=1
      elif _== "T":
        self.dna_dict["T"]+=1
      elif _== "G":
        self.dna_dict["G"]+=1
      else:
        self.dna_dict["C"]+=1
    return self.dna_dict

  def calculate_complement(self):
    new_dna=""
    for _ in self.dna[::-1]:
      if _== "A":
        new_dna+="T"
      elif _== "T":
        new_dna+="A"
      elif _== "G":
        new_dna+="C"
      else:
        new_dna+="G"

    return new_dna
  
  def count_point_mutations(self,dna):
    differ=0
    for i in range(len(dna)):
      if self.dna[i]!= dna[i]:
        differ+=1
    return differ

  def  find_motif(self,sub_dna):
    indexes=[]
    def index(dna_):
      if len(dna_)> len(self.dna):
        return [0]
      else:
        if dna_ in self.dna:
          indexes.append(self.dna.index(dna_[0]))
          return index(dna_[self.dna.index(dna_[0]):])
    index(sub_dna)
    return indexes

d1=DNA("GAGCC")
print(d1.count_nucleotides())
print(d1.calculate_complement())
