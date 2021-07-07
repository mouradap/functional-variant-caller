import subprocess

def variant_calling(ref_genome, r1, r2, target_file):
    seqtk_cleaning_command = '''
        seqtk randbase {ref_genome} > {ref_genome}_freebayes.fa
        '''.format(
            ref_genome=ref_genome
        )
    
    # samtools_sequence_indexer_command = '''
    #     samtools index {r1}_{r2}_BWA_sorted_PCR_RG.bam
    #     '''.format(
    #         r1=r1,
    #         r2=r2)

    samtools_reference_indexer_command = '''
        samtools faidx {ref_genome}_freebayes.fa
        '''.format(
            ref_genome=ref_genome)

    freebayes_variant_calling_command = '''
        freebayes -f {ref_genome}_freebayes.fa {r1}_{r2}_BWA_sorted_PCR_RG.bam
        --target {target_file}
        > {r1}_{r2}_BWA_sorted_PCR_RG_freebayes.vcf
        '''.format(
            r1=r1,
            r2=r2,
            ref_genome=ref_genome,
            target_file = target_file)

    # print("Indexing sorted BAM...")
    # subprocess.run(samtools_sequence_indexer_command, shell=True)
    # print("Done!\n")

    print("Cleaning with seqtk...")
    subprocess.run(seqtk_cleaning_command, shell=True)
    print("Done!\n")

    print("Indexing to fai...")
    subprocess.run(samtools_reference_indexer_command, shell=True)
    print("Done!\n")

    print("Calling variants with freebayes...")
    subprocess.run(freebayes_variant_calling_command, shell=True)
    print("Done!")

