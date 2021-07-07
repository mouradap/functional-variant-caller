from subprocess import run

def fastqc_analyzer(r1, r2, threads):
    fastqc_command = 'fastqc -t {threads} {r1} {r2}'.format(threads=threads, r1=r1, r2=r2) 

    run(fastqc_command, shell=True)