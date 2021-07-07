import subprocess

def reference_indexing(reference_genome, threads):
    bwa_index_command = 'bwa index {ref_genome}'.format(ref_genome=reference_genome, threads=threads)
    samtools_index_command = 'samtools faidx {ref_genome}'.format(ref_genome=reference_genome)
    print("Indexing with bwa index...")
    subprocess.run(bwa_index_command, shell=True)
    print("Done!\n")

    print("Creating fai...")
    subprocess.run(samtools_index_command, shell=True)
    print("Done!")

