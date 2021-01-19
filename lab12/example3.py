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
    len_sub=len(sub_dna)
    len_dna=len(self.dna)
    for i in range(0,len_dna-len_sub+1):
      if self.dna[i:i+len_sub]== sub_dna:
        indexes.append(i)
    return indexes

d1=DNA("GATATATGCATATACTT")
print(d1.count_nucleotides())
print(d1.calculate_complement())
print(d1.find_motif("ATA"))
