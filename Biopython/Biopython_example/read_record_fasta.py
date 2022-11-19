from Bio import SeqIO # 导入序列读写模块
from Bio.SeqIO import parse # 导入Bio.SeqIO模块中可用的解析类。
from Bio.SeqRecord import SeqRecord # 导入Bio.SeqRecord模块中的SeqRecord类。该模块用于处理序列记录，而SeqRecord类用于表示序列文件中可用的特定序列。
from Bio.Seq import Seq # 导入Bio.Seq模块中的Seq类。此模块用于操纵序列数据，Seq类用于表示序列文件中可用的特定序列记录的序列数据。
file = open("/Users/liang.hanqing/Documents/jupyter/Biopython/examples/D. melanogaster male fru type-A mRNA.fasta")
records = parse(file, "fasta")
for record in records:  # 解析序列文件的内容，并将该内容作为SeqRecord对象的列表返回。
   print("Id: %s" % record.id)
   print("Name: %s" % record.name)
   print("Description: %s" % record.description)
   print("Annotations: %s" % record.annotations)
   print("Sequence Data: %s" % record.seq)
