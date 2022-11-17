from Bio import SeqIO #导入序列读写模块
from Bio.SeqIO import parse
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
file = open("/Users/liang.hanqing/Documents/jupyter/Biopython/examples/D. melanogaster male fru type-A mRNA.fasta")
records = parse(file, "fasta")
for record in records:
   print("Id: %s" % record.id)
   print("Name: %s" % record.name)
   print("Description: %s" % record.description)
   print("Annotations: %s" % record.annotations)
   print("Sequence Data: %s" % record.seq)
