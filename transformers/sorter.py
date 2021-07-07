import subprocess

def bam_sorting(r1, r2, picard):
    # picard_sort_sam_command = '''
    #     java -Xmx10g -jar {picard} SortSam VALIDATION_STRINGENCY=SILENT
    #     I={r1}_{r2}_BWA.bam o="{r1}_{r2}_BWA_sorted.bam" SORT_ORDER=coordinate'''.format(
    #     r1=r1,
    #     r2=r2,
    #     picard=picard)
    picard_mark_duplicates_command = '''
        java -Xmx10g -jar {picard} MarkDuplicates VALIDATION_STRINGENCY=SILENT
        I={r1}_{r2}_BWA_sorted.bam o="{r1}_{r2}_BWA_sorted_PCR.bam"
        REMOVE_DUPLICATES=true M="{r1}_{r2}_BWA_sorted_PCR.metrics'''.format(
        r1=r1,
        r2=r2,
        picard=picard)
    picard_addreplace_readgroups_command = '''
        java -Xmx10g -jar {picard} AddOrReplaceReadGroups VALIDATION_STRINGENCY=SILENT
        I={r1}_{r2}_BWA_sorted_PCR.bam o="{r1}_{r2}_BWA_sorted_PCR_RG.bam"
        SO=coordinate RGID=HISeq RGLB=NIST RGPL=illumina RGPU=R1
        RGSM=NA12878 CREATE_INDEX=true'''.format(
        r1=r1,
        r2=r2,
        picard=picard)
    # print("Sorting BAM file with picard...")
    # subprocess.run(picard_sort_sam_command, shell=True)
    # print("Done!\n")

    print("Marking duplicates...")
    subprocess.run(picard_mark_duplicates_command, shell=True)
    print("Done!\n")

    print("Adding Read Goups...")
    subprocess.run(picard_addreplace_readgroups_command, shell=True)
    print("Done!")

