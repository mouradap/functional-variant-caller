import subprocess

def functional_mapping(r1, r2):
    snpeff_command = '''
<<<<<<< HEAD
        java -Xmx10g -jar {snpEff} -c snpEff.config GRCh37.75 {r1}_{r2}_BWA_sorted_PCR_RG_freebayes.vcf
        > {r1}_{r2}_BWA_sorted_PCR_RG_freebayes_snpEff.vcf
=======
        snpEff GRCh37.75 {r1}_{r2}_BWA_PCR_RG_freebayes.vcf
        > {r1}_{r2}_BWA_PCR_RG_freebayes_snpEff.vcf
>>>>>>> b270706962b0b4cd0457f7b2f375bb6990625bbc
        '''.format(
            snpeff=snpeff,
            r1=r1,
            r2=r2)

    print("Running snpEff command...")
    subprocess.run(snpeff_command, shell=True)
    print("Done!\n")
